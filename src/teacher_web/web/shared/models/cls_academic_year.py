from datetime import datetime
from django.conf import settings

class AcademicYearPeriod:
    def __init__(self, period, time):
        self.period = period
        self.time = time


class AcademicYear:

    def __init__(self, start_date, end_date):
        self.start = start_date.strftime(settings.ISOFORMAT)
        self.end = end_date.strftime(settings.ISOFORMAT)
        self.display = f"{start_date.year}/{end_date.year}" # TODO: get year


    @classmethod
    def get_all(cls, db, auth_ctx): # institute_id, department_id):
        """ get academic year """
        
        academic_year = {}

        # the current academic year is zero

        start_year = datetime.now().year if datetime.now().month >= 9 else datetime.now().year - 1   
        
        for i in range(-1, 2):
            
            start_date = datetime(year=start_year+i, month=9, day=1)
            end_date = datetime(year=start_year+i+1, month=8, day=30)

            academic_year[i] = AcademicYear(start_date, end_date).__dict__

            academic_year[i]["periods"] = dict(AcademicYear.get_periods(db=db, academic_year=academic_year[i], auth_ctx=auth_ctx))

        return academic_year

    
    @classmethod
    def get_periods(cls, db, academic_year, auth_ctx):
        """ get the periods for the academic year """
        return [
                ("09:00", "Period 1"), 
                ("10:00", "Period 2"), 
                ("11:00", "Break"), 
                ("11:15", "Period 3"), 
                ("12:15", "Lunch"), 
                ("13:15", "Period 4"), 
                ("14:15", "Period 5"), 
                ("15:15", "Period 6"), 
                ("16:15", "Homework club")
        ]