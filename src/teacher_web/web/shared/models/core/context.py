from datetime import datetime
from django.conf import settings
from shared.models.cls_academic_year import AcademicYearModel
from shared.models.cls_academic_year_period import AcademicYearPeriodModel
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE


class Ctx:
    
    def __init__(self, institute_id, department_id, **view_params):
        self.institute_id = institute_id
        self.department_id = department_id
        self.scheme_of_work_id = view_params.get("scheme_of_work_id",0)
        self.lesson_id = view_params.get("lesson_id",0)
        self.auth_user_id = view_params.get("auth_user_id",0)
        self.user_name = "Not logged in"
        # public member
        self.can_view = STATE.PUBLISH


class AcademicYearCtx:
    def __init__(self, request):
        self.start_date=request.session["academic_year.start_date"]
        self.end_date=request.session["academic_year.end_date"]
        self.periods=request.session["academic_year.periods"]


class AuthCtx(Ctx):

    @staticmethod
    def current_year(academic_years):
        now = datetime.now()
        for ay in academic_years:
            if ay.start_date > now and ay.end_date < now:
                return ay.start_date.year
        # otherwise return current year
        return datetime.now().year

    
    def __init__(self, db, request, institute_id, department_id, **view_params):
        super().__init__(institute_id=institute_id, department_id=department_id, **view_params)

        self.db = db
        self.request = request
        self.selected_year = 0
        self.auth_user_id = request.user.id   

        if request.user.id is not None:
            self.user_name = request.user.first_name
            # logged in member can view internal and public published
            self.can_view = STATE.PUBLISH_INTERNAL

        # NOTE: get department then get institute to promote can_view

        self.department = DepartmentContextModel.cached(request, db, self.institute_id, self.department_id, self.auth_user_id)
        # TODO: #323 check ownership and set can_view
        
        self.institute = InstituteContextModel.cached(request, db, self.institute_id, self.auth_user_id)
        # TODO: #323 check ownership and set can_view
        
        self.scheme_of_work = SchemeOfWorkContextModel.cached(request, db, self.institute_id, self.department_id, self.scheme_of_work_id, self.auth_user_id)
        # TODO: #323 check ownership and set can_view
        
        #432 get years academic years
        
        self.academic_years = AcademicYearModel.get_all(db, self)
        
        # get the selected year or find the current academic year

        self.selected_year = self.request.session.get("academic_year__selected_id", AuthCtx.current_year(self.academic_years)) # default to current year
        
        self.academic_year = AcademicYearModel.get_model(db, self.selected_year, self)

        # TODO: verify
        #self.request.session["academic_year.start_date"] = self.academic_year.start_date
        #self.request.session["academic_year.end_date"] = self.academic_year.end_date
        
        #432 store in cache
        #self.request.session["academic_year__display"] = self.academic_year.display_name
        
        self.periods = AcademicYearPeriodModel.get_all(db, self)

        # default TeacherPermissionModel
        self.teacher_permission = TeacherPermissionModel.default(self.institute, self.department, None, self)
    
        ''' if the current user created the institute or department they are DEPARTMENT ADMIN '''
        if self.auth_user_id is not None and self.auth_user_id > 0:
            self.teacher_permission = TeacherPermissionModel.get_model(self.db, teacher_id=self.auth_user_id, scheme_of_work=self.scheme_of_work, auth_user=self)
            
            
    def check_permission(self, min_permission):
        """ check if the teacher has enough priviliges """

        #367 move checks to functions and allow where department requires no permissions or where department id is zero

        if min_permission == DEPARTMENT.NONE or self.department_id == 0:
            return True
        elif self.teacher_permission is None:
            return False
        else:
            return self.teacher_permission.check_permission(min_permission)


    def __repr__(self):
        return f"user={self.auth_user_id},{self.user_name}, institute_id={self.institute_id}, department_id={self.department_id}"

