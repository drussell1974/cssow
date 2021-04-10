from shared.models.core.basemodel import BaseContextModel, BaseModel, try_int
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy

class AcademicYearPeriodContextModel(BaseContextModel):
    
    def __init__(self, id_, academic_year, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, display_name=academic_year, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=ctx)
        self.year = academic_year


    @classmethod
    def empty(cls, academic_year, published=STATE.PUBLISH, ctx=None):
        model = cls(id_=0, academic_year=academic_year, published=published, ctx=ctx)
        return model


    @classmethod
    def get_context_array(cls, db, institute_id, department_id, selected_year, auth_user_id):
        
        model = cls.empty(selected_year)

        result = BaseContextModel.get_context_array(db, model, "academic_year_period__get_context_array", handle_log_info, department_id, selected_year)
        #result.institute_id = institute_id
        #result.department_id = department_id

        return result if result is not None else None


    @classmethod
    def cached_array(cls, request, db, institude_id, department_id, selected_year, auth_user_id):
        
        periods_array = []
        
        cache_obj = CacheProxy.session_cache_array(request, db, "academic_year_periods_array", cls.get_context_array, institude_id, department_id, selected_year, auth_user_id)

        if cache_obj is not None:
            periods_array = cache_obj
        
        return periods_array


class AcademicYearPeriod(BaseModel):
    def __init__(self, time, name, is_from_db, created_by_id=0, created_by_name="", auth_ctx=None):
        super().__init__(time.__hash__, name, created="", created_by_id=created_by_id, created_by_name=created_by_name, published=1, is_from_db=is_from_db, ctx=auth_ctx)
        self.time = time
        self.name = name


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate class code
        self._validate_required_string("time", self.time, 1, 5)
        self._validate_regular_expression("time", self.time, "^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", "must hh:mm")
        
        # Validate class name
        self._validate_required_string("name", self.name, 1, 20)
        
        return self.is_valid


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """
    
        if self.time is not None:
            self.time = sql_safe(self.time)

        if self.name is not None:
            self.name = sql_safe(self.name)


    def is_new(self):
        return (self.is_from_db == False)


    def __dict__(self):
        # handle keyvalue pair
        return ( str(self.time), self.name )
    

    @classmethod
    def get_all(cls, db, auth_ctx):
        """ get the periods for the academic year """
        
        rows = AcademicYearPeriodDataAccess.get_all(db, auth_ctx.department_id, auth_ctx.selected_year, auth_ctx.auth_user_id)
        results = []
        for row in rows:
            results.append(
                AcademicYearPeriod(row[0], row[1], is_from_db=True)
            )

        return results 


class AcademicYearPeriodDataAccess:

    @classmethod
    def get_all(cls, db, department_id, start_date, auth_user_id):

        execHelper = ExecHelper()

        str_select = "academic_year_period__get_all"
        params = (department_id, start_date, auth_user_id)

        rows = []
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows
        