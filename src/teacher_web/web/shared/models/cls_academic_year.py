from datetime import datetime
from django.conf import settings
from shared.models.core.basemodel import BaseContextModel, BaseModel, try_int
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.cls_academic_year_period import AcademicYearPeriod
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy

class AcademicYearContextModel(BaseContextModel):
    
    @classmethod
    def default(cls, published=STATE.PUBLISH, ctx=None):
        start_year = datetime.now().year if datetime.now().month >= 9 else datetime.now().year - 1
        model = cls(0, start_date=datetime(start_year, 9, 1), end_date=datetime(start_year+1, 7, 30), published=published, ctx=ctx)
        return model


    def __init__(self, id_, start_date, end_date, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, display_name=f"{start_date.year}/{end_date.year}", created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=ctx)
        self.start_date = start_date
        self.end_date = end_date


    @classmethod
    def get_context_model(cls, db, institute_id, department_id, selected_year, auth_user_id):
        
        empty_model = cls.default()

        result = BaseContextModel.get_context_model(db, empty_model, "academic_year__get_context_model", handle_log_info, department_id, selected_year)
        result.institute_id = institute_id
        result.department_id = department_id

        return result if result is not None else None


    @classmethod
    def cached(cls, request, db, institude_id, department_id, selected_year, auth_user_id):

        academic_year = cls.default()
        
        cache_obj = CacheProxy.session_cache(request, db, "academic_year", cls.get_context_model, institude_id, department_id, selected_year, auth_user_id)

        if cache_obj is not None:
            academic_year.from_dict(cache_obj)

        return academic_year        


    @classmethod
    def get_context_array(cls, db, institute_id, department_id, auth_user_id):
        
        model = cls.default()

        result = BaseContextModel.get_context_array(db, model, "academic_year__get_context_array", handle_log_info, department_id)
        #result.institute_id = institute_id
        #result.department_id = department_id

        return result if result is not None else None


    @classmethod
    def cached_array(cls, request, db, institude_id, department_id, auth_user_id):


        academic_years = []
        
        cache_obj = CacheProxy.session_cache_array(request, db, "academic_year_array", cls.get_context_array, institude_id, department_id, auth_user_id)

        if cache_obj is not None:
            academic_years = cache_obj
        
        return academic_years     

class AcademicYearModel(BaseModel):

    def __init__(self, start_date, end_date, is_from_db, created_by_id=0, created_by_name="", auth_ctx=None):
        super().__init__(start_date.year, f"{start_date.year}/{end_date.year}", created="", created_by_id=created_by_id, created_by_name=created_by_name, published=1, is_from_db=is_from_db, ctx=auth_ctx)
        self.year = start_date.year
        self.start = start_date.strftime(settings.ISOFORMAT)
        self.end = end_date.strftime(settings.ISOFORMAT)
        self.display = f"{start_date.year}/{end_date.year}"
        self.periods = []

    def __dict__(self):
        # handle keyvalue pair
        return ( self.year, self.display )


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)
        
        return self.is_valid


    @classmethod
    def get_all(cls, db, auth_ctx):
        """ get the periods for the academic year """
        
        rows = AcademicYearDataAccess.get_all(db, auth_ctx.department_id, auth_ctx.auth_user_id)
        results = []
        for row in rows:
            # check current year
            model = AcademicYearModel(row[0], row[1], is_from_db=True)

            model.periods = AcademicYearPeriod.get_all(db, auth_ctx=auth_ctx)

            results.append(model)

        return results


class AcademicYearDataAccess:

    @classmethod
    def get_all(cls, db, department_id, auth_user_id):

        execHelper = ExecHelper()

        str_select = "academic_year__get_all"
        params = (department_id, auth_user_id)

        rows = []
        
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows