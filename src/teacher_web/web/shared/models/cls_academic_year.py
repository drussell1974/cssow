from datetime import datetime
from django.conf import settings
from shared.models.core.basemodel import BaseContextModel, BaseModel, try_int
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.cls_academic_year_period import AcademicYearPeriodModel
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy

class AcademicYearModel(BaseModel):

    def init_dates(self, start_date, end_date):
        
        if type(start_date) is str:
            self.start = start_date # set start string property
            self.start_date = datetime.strptime(start_date, settings.ISOFORMAT) # set start_date datetime property    
        elif type(start_date) is datetime:
            self.start = start_date.strftime(settings.ISOFORMAT) # set start string property
            self.start_date = start_date # set start_date date property
        
        if type(end_date) is str:
            self.end = end_date  # set start string property
            self.end_date = datetime.strptime(end_date, settings.ISOFORMAT) # set start_date datetime property
        elif type(end_date) is datetime:
            self.end = end_date.strftime(settings.ISOFORMAT)  # set start string property
            self.end_date = end_date # set end_date datetime property
        #raise KeyError(type(self.start_date))
            

    def __init__(self, start_date, end_date, is_from_db, created_by_id=0, created_by_name="", published=STATE.PUBLISH, auth_ctx=None):
        #self.start_date = start_date
        #self.end_date = end_date
        self.init_dates(start_date, end_date)
        
        super().__init__(self.start_date.year, f"{self.start_date.year}/{self.end_date.year}", created="", created_by_id=created_by_id, created_by_name=created_by_name, published=1, is_from_db=is_from_db, ctx=auth_ctx)
        
        self.year = self.start_date.year
        self.display = f"{self.start_date.year}/{self.end_date.year}"
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
        #self.is_valid = True
        # Validate
        #self._validate_required_string("start", self.start, 1, 19)
        self._validate_range("start_date", value_to_validate=self.start_date, low=datetime(year=1700, month=1, day=1), high=datetime(year=2099, month=12, day=31))
        #self._validate_required_string("end", self.end, 1, 19)
        self._validate_range("end_date", value_to_validate=self.end_date, low=datetime(year=1700, month=1, day=1), high=datetime(year=2099, month=12, day=31))
        
        return self.is_valid


    @classmethod
    def save(cls, db, academic_year, institute_id, published, auth_ctx):
        if academic_year.is_valid:
            return AcademicYearDataAccess.insert(db, academic_year.year, academic_year.start_date, academic_year.end_date, institute_id, published, auth_ctx.auth_user_id)
        
        return academic_year


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

            model.periods = AcademicYearPeriodModel.get_all(db, auth_ctx.institute_id, auth_ctx=auth_ctx)

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


    @classmethod
    def insert(cls, db, year, start_date, end_date, institute_id, published, auth_user_id):

        execHelper = ExecHelper()

        str_insert = "academic_year__insert"
        params = (year, start_date, end_date, institute_id, published, auth_user_id)

        new_id = execHelper.insert(db, str_insert, params, handle_log_info)
        
        return new_id