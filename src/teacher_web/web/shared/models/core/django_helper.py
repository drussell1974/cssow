from django.http import Http404
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel


def on_not_found(self, model, *identifers):
    str_msg = "The item is currently unavailable or you do not have permission."
    raise Http404(str_msg)


class auth_user_model:
    
    # TODO: #329 rename to auth_ctx_wrapper

    def __init__(self, db, request, ctx):
        """ checks the user id in the request #253 check user id
        :param:db: the database context
        :param:request: the application request
        """
        self.view_ctx = ctx

        self.department_id = ctx.department_id
        self.institute_id = ctx.institute_id
        self.scheme_of_work_id = ctx.scheme_of_work_id

        # TODO: #329 set auth_user_id or user_id
        self.user_id = request.user.id
        self.auth_user_id = request.user.id

        if request.user.id is not None:
            self.user_name = request.user.first_name
        

    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}"