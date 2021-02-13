from django.http import Http404
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel


def on_not_found(self, model, *identifers):
    prefix = repr(model) if model is not None else "item"
    str_msg = "The item is currently unavailable or you do not have permission."
    #"{} {} does not exist, is currently unavailable or you do not have permission.".format(prefix, identifers)
    raise Http404(str_msg)


class auth_user_model:
    def __init__(self, db, request, ctx):

        """ checks the user id in the request #253 check user id
        :param:db: the database context
        :param:request: the application request
        """
        
        # TODO: #329 set auth_user_id or user_id
        self.user_id = request.user.id

        self.auth_user_id = request.user.id

        if request.user.id is not None:
            self.user_name = request.user.first_name

        #329 ensure Institute is part of Department Model
        #teacher = TeacherPermissionModel(teacher_id=0, teacher_name="", ctx=ctx, scheme_of_work = SchemeOfWorkModel(ctx.scheme_of_work_id, "", department_id=ctx.department_id, institute_id=ctx.institute_id))

        #if ctx is not None:
        #    teacher = TeacherModel.get_model(db, teacher_id=self.user_id, ctx=ctx)
        
        self.department_id = ctx.department_id
        self.institute_id = ctx.institute_id
        self.scheme_of_work_id = ctx.scheme_of_work_id
        

    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}"