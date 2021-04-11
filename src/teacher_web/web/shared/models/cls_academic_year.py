from datetime import datetime
from django.conf import settings
from shared.models.core.basemodel import BaseContextModel, BaseModel, try_int
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.cls_academic_year_period import AcademicYearPeriodModel
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy

class AcademicYearModel(BaseModel):

    def __init__(self, start_date, end_date, is_from_db, created_by_id=0, created_by_name="", published=STATE.PUBLISH, auth_ctx=None):
        if type(start_date) is str:
            start_date = datetime.strptime(start_date, settings.ISOFORMAT)
        if type(end_date) is str:
            end_date = datetime.strptime(end_date, settings.ISOFORMAT)
        
        super().__init__(start_date.year, f"{start_date.year}/{end_date.year}", created="", created_by_id=created_by_id, created_by_name=created_by_name, published=1, is_from_db=is_from_db, ctx=auth_ctx)
        
        self.start_date = start_date
        self.end_date = end_date
        self.year = start_date.year
        self.start = start_date.strftime(settings.ISOFORMAT)
        self.end = end_date.strftime(settings.ISOFORMAT)
        self.display = f"{start_date.year}/{end_date.year}"
        self.periods = []


    @classmethod
    def default(cls, for_academic_year=datetime.now().year, published=STATE.PUBLISH, ctx=None):
        """ a default academic year runs from 01-Sept-YYYY - 30-Jul-YYYY+1 """

        start_year = for_academic_year if datetime.now().month >= 9 else for_academic_year - 1
        model = cls(start_date=datetime(start_year, 9, 1), end_date=datetime(start_year+1, 7, 30), published=published, is_from_db=False, auth_ctx=ctx)
        return model


    def __dict__(self):
        # handle keyvalue pair
        return ( self.year, self.display )


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)
        
        return self.is_valid


    @classmethod
    def get_all(cls, db, institute_id, auth_ctx):
        """ get the periods for the academic year """
        
        rows = AcademicYearDataAccess.get_all(db, institute_id, auth_ctx.auth_user_id)
        results = []
        for row in rows:
            # check current year
            model = AcademicYearModel(row[0], row[1], is_from_db=True)

            model.periods = AcademicYearPeriodModel.get_all(db, institute_id, auth_ctx=auth_ctx)

            results.append(model)

        return results


    @classmethod
    def get_model(cls, db, institute_id, for_academic_year, auth_ctx):
        """ get the periods for the academic year """
        
        model = None

        rows = AcademicYearDataAccess.get_model(db, institute_id, for_academic_year, auth_ctx.auth_user_id)
        
        for row in rows:
            # check current year
            model = AcademicYearModel(row[1], row[2], is_from_db=True)

            model.periods = AcademicYearPeriodModel.get_all(db, auth_ctx.institute_id,  auth_ctx=auth_ctx)

            return model

        return model


class AcademicYearDataAccess:

    @classmethod
    def get_all(cls, db, institute_id, auth_user_id):

        execHelper = ExecHelper()

        str_select = "academic_year__get_all"
        params = (institute_id, auth_user_id)

        rows = []
        
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows


    @classmethod
    def get_model(cls, db, institute_id, for_academic_year, auth_user_id):

        execHelper = ExecHelper()

        str_select = "academic_year__get_model"
        params = (institute_id, for_academic_year, auth_user_id)

        rows = []
        
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows