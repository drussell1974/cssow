from datetime import datetime
from django.conf import settings
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE

class AcademicYear:

    @classmethod
    def get_options(cls, db, institute_id, department_id):
        """ session helper to determine academic year """
        
        academic_year = {}

        start_year = datetime.now().year if datetime.now().month >= 9 else datetime.now().year - 1   
        
        for i in range(-1, 2):
            display = f"{start_year+i}/{start_year+i+1}"
            start_date = datetime(year=start_year+i, month=9, day=1)
            end_date = datetime(year=start_year+i+1, month=8, day=30)

            academic_year[i] = { "display":display, "start":start_date.strftime(settings.ISOFORMAT), "end": end_date.strftime(settings.ISOFORMAT) }

        return academic_year


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


class AuthCtx(Ctx):
    
    def __init__(self, db, request, institute_id, department_id, start_date="2021-06-09T17:20", end_date=None, **view_params):
        super().__init__(institute_id=institute_id, department_id=department_id, **view_params)

        self.db = db
        self.request = request
        
        #432 get years (from session or database)
        academic_year = AcademicYear.get_options(db, institute_id, department_id)

        #432 store in session
        self.request.session["academic_year"] = academic_year
        #432 get set start and end from selected year
        selected_year = self.request.session.get("academic_year__selected_id", 0) # default current (offset zero)
        
        self.request.session["academic_year__display"] = academic_year[selected_year]["display"]
        self.request.session["academic_year.start_date"] = academic_year[selected_year]["start"]
        self.request.session["academic_year.end_date"] = academic_year[selected_year]["end"] 

        self.auth_user_id = request.user.id
        self.academic_year = AcademicYearCtx(request)

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


class AcademicYearCtx:
    def __init__(self, request):
        self.start_date=request.session["academic_year.start_date"]
        self.end_date=request.session["academic_year.end_date"]
