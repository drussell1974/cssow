from shared.models.core.basemodel import BaseContextModel, BaseModel, try_int
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy


class AcademicYearPeriodModel(BaseModel):
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
    def get_all(cls, db, institute_id, auth_ctx):
        """ get the periods for the academic year """
        
        rows = AcademicYearPeriodDataAccess.get_all(db, institute_id, auth_ctx.selected_year, auth_ctx.auth_user_id)
        results = []
        for row in rows:
            results.append(
                AcademicYearPeriodModel(row[0], row[1], is_from_db=True)
            )

        return results


class AcademicYearPeriodDataAccess:

    @classmethod
    def get_all(cls, db, institute_id, start_date, auth_user_id):

        execHelper = ExecHelper()

        str_select = "academic_year_period__get_all"
        params = (institute_id, start_date, auth_user_id)

        rows = []
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows
        