
class AcademicYearPeriod:
    def __init__(self, period, time):
        self.period = period
        self.time = time

    
    @classmethod
    def get_all(cls, db, academic_year, auth_ctx):
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