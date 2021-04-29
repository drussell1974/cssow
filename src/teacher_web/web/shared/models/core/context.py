from datetime import datetime
from django.conf import settings
from django.urls import reverse
from shared.models.cls_academic_year import AcademicYearModel
from shared.models.cls_academic_year_period import AcademicYearPeriodModel
from shared.models.cls_institute import InstituteContextModel, InstituteModel
from shared.models.cls_department import DepartmentContextModel, DepartmentModel
from shared.models.cls_notification import NotifyModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel, SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.core.log_handlers import handle_log_info
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
        
        raise DeprecationWarning("Needs implementing")

        self.start_date=request.session["academic_year.start_date"]
        self.end_date=request.session["academic_year.end_date"]
        self.periods=request.session["academic_year.periods"]


class AuthCtx(Ctx):

    @classmethod
    def get_selected_year(cls, request, session_key, academic_years):
        def inner(academic_years):
            now = datetime.now()
            curr = now.year
            for ay in academic_years:
                curr = ay.start_date.year # the last selected year will be returned if a matching one is not found
                if now > ay.start_date and now < ay.end_date:
                    return ay.start_date.year
            # otherwise return the last academic year or the current year
            return curr
        
        if session_key not in request.session:
            request.session[session_key] = inner(academic_years)
        
        return request.session[session_key]
        
    
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
        
        self.institute = InstituteContextModel.cached(request, db, self.institute_id, self.auth_user_id)
        
        self.scheme_of_work = SchemeOfWorkContextModel.cached(request, db, self.institute_id, self.department_id, self.scheme_of_work_id, self.auth_user_id)

        if institute_id > 0:        
            #432 get academic years and periods
            self.academic_years = AcademicYearModel.get_all(db, institute_id, self)
            
            # use session to get selected year or default to current year
            self.selected_year = self.get_selected_year(request, "academic_year__selected_id", self.academic_years)
        
            self.academic_year = AcademicYearModel.get_model(db, institute_id, for_academic_year=self.selected_year, auth_ctx=self)
        
            # default

            if self.academic_year is None:
                self.academic_year = AcademicYearModel.default(for_academic_year=self.selected_year)

        self.periods = AcademicYearPeriodModel.get_all(db, institute_id, self)

        # default TeacherPermissionModel
        self.teacher_permission = TeacherPermissionModel.default(self.institute, self.department, None, self)
    
        ''' if the current user created the institute or department they are DEPARTMENT ADMIN '''
        if self.auth_user_id is not None and self.auth_user_id > 0:
            self.teacher_permission = TeacherPermissionModel.get_model(self.db, teacher_id=self.auth_user_id, scheme_of_work=self.scheme_of_work, auth_user=self)
            
            
    def check_permission(self, min_permission):
        """ check if the teacher has enough priviliges """

        #367 move checks to functions and allow where department requires no permissions or where department id is zero
        
        # TODO: change to self.institute_id == 0

        if min_permission == DEPARTMENT.NONE or self.department_id == 0:
            return True
        elif self.teacher_permission is None:
            return False
        else:
            return self.teacher_permission.check_permission(min_permission)


    @classmethod
    def check_setup_and_notify(cls, db, request, auth_ctx):
        if auth_ctx.institute_id > 0 and auth_ctx.department_id > 0:
            department = DepartmentModel.get_model(db, department_id=auth_ctx.department_id, auth_user=auth_ctx)

            # inform owner the should create topics
            no_of_topics = DepartmentModel.get_number_of_topics(db, auth_ctx.department_id, auth_ctx)
            if no_of_topics == 0:
                NotifyModel.create(
                    db=db,
                    title="Create topics",
                    message=f"You must create topics for {department.name} before you can create lessons and pathways.",
                    action_url=reverse('department_topic.index', args=[auth_ctx.institute_id, auth_ctx.department_id]),
                    auth_ctx=auth_ctx,
                    handle_log_info=handle_log_info
                )

            # inform owner they should create pathways
            no_of_pathways = DepartmentModel.get_number_of_pathways(db, auth_ctx.department_id, auth_ctx)
            if no_of_pathways == 0:
                NotifyModel.create(
                    db=db,
                    title="Create pathway",
                    message=f"Create pathways for {department.name} to allow objectives progress between different key stages.",
                    action_url=reverse('ks123pathways.index', args=[auth_ctx.institute_id, auth_ctx.department_id]),
                    auth_ctx=auth_ctx,
                    handle_log_info=handle_log_info
                )

            no_of_schemes_of_work = DepartmentModel.get_number_of_schemes_of_work(db, auth_ctx.department_id, auth_ctx)
            if no_of_schemes_of_work == 0:
                # if there are no schemes of work prompt owner to create one
                NotifyModel.create(
                    db=db,
                    title="Create scheme of work",
                    message=f"Create your first scheme of work for {department.name}.",
                    action_url=reverse('schemesofwork.index', args=[auth_ctx.institute_id, auth_ctx.department_id]),
                    auth_ctx=auth_ctx,
                    handle_log_info=handle_log_info
                )
            else:
                # ... otherwise, check if there are curriculum content for the scheme of work
                for schemeofwork_model in SchemeOfWorkModel.get_my(db, auth_ctx.institute, auth_ctx.department, auth_ctx):
                    # after creating a scheme of work notify the user they must create curriculum content before create lessons
                    no_of_content = SchemeOfWorkModel.get_number_of_contents(db, schemeofwork_model["id"], auth_ctx)
                    if no_of_content == 0:
                        NotifyModel.create(
                            db=db,
                            title="Create scheme of work",
                            message=f"You must define the curriculum content for {schemeofwork_model['name']} before you can create lessons",
                            action_url=reverse('content.index', args=[auth_ctx.institute_id, auth_ctx.department_id, schemeofwork_model["id"]]),
                            auth_ctx=auth_ctx,
                            handle_log_info=handle_log_info
                        )