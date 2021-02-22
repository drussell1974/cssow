from django.db import connection as db
from django.shortcuts import redirect
from django.urls import reverse
from shared.models.core.django_helper import on_not_found
from shared.models.core.log_handlers import handle_log_info, handle_log_warning, handle_log_error
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.models.core.context import AuthCtx
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

DEFAULT_INSTITUTE_ID = 0
DEFAULT_DEPARTMENT_ID = 0
DEFAULT_SCHEME_OF_WORK_ID = 0
DEFAULT_LESSON_ID = 0
UNAUTHORISED_USER_ID = None


def unauthorise_request(func):
    """
    changes to request.user.id to UNAUTHORISED_USER_ID 
    """
        
    def inner(*args, **kwargs):
        for arg in args:   
            if hasattr(arg, 'user') and hasattr(arg.user, 'id'):
                arg.user.id = UNAUTHORISED_USER_ID
        return func(*args, **kwargs)
    return inner


class min_permission_required:
    """ checks the teachers permission on the scheme of work and redirect if user does not have permission """

    def __init__(self, permission, login_url, login_route_name = None):
        """ SCHEMEOFWORK_ACCESS and LESSON_ACCESS decorator argument """
        self._permission = permission
        self._auth_user = 0
        self._redirect_to_url = login_url
        self._redirect_to_route_name = login_route_name


    def __call__(self, func):
        """ the parent function """

        def inner(*args, **kwargs):
            ''' request must be the first argument in the view function '''
            request = args[0]
            
            self.kwargs = kwargs

            self._return_url = request.path
            #auth_user = request.user

            str_err = f"You do not have {str(self._permission).split('.')[1]} permission"
            
            ''' TODO: #329 get permission from context from database (handle DEFAULT values) '''
            
            department_id = self.getkwargs("department_id", default_value=DEFAULT_DEPARTMENT_ID)
            institute_id = self.getkwargs("institute_id", default_value=DEFAULT_INSTITUTE_ID)            
            scheme_of_work_id = self.getkwargs("scheme_of_work_id", default_value=DEFAULT_SCHEME_OF_WORK_ID)
            
            auth_ctx = AuthCtx(db, request, **kwargs)
            
            ''' TODO: get light weight '''

            scheme_of_work = SchemeOfWorkModel.get_model(db, scheme_of_work_id, auth_ctx)
            
            if scheme_of_work is None:
                # create empty scheme of work with scheme_of_work_id = 0
                scheme_of_work = SchemeOfWorkModel.empty(ctx=auth_ctx)
                
            ''' teacher_id and auth_user are the same in this call '''
            # get the permissions for the current user
            model = TeacherPermissionModel.get_model(db, teacher_id=auth_ctx.auth_user_id, scheme_of_work=scheme_of_work, auth_user=auth_ctx)

            if model.check_permission(self._permission) == False:
                ''' redirect if user does not have permissions for this scheme of work '''
                str_err = str_err + f" for this {str(self._permission).split('.')[0]} ({scheme_of_work_id}) redirect to {self._redirect_to_url}."
                
                return self.redirect_handler(str_err, institute_id, department_id, scheme_of_work_id=scheme_of_work_id, permission=self._permission) 

            self.setkwargs("ctx", value=auth_ctx)
            
            # call decorated function
            return func(*args, **kwargs)
            
        return inner


    def setkwargs(self, key, value):
        if key in self.kwargs.keys():
            self.kwargs[key] = value


    def getkwargs(self, key, default_value = None):
        if key in self.kwargs.keys():
            return self.kwargs[key]
        elif default_value is not None:
            return default_value
        else:
            raise KeyError(f"'{key}' value must be passed as a keyword argument")


    def redirect_handler(self, error_message, institute_id, department_id, scheme_of_work_id, permission):
        handle_log_warning(db, scheme_of_work_id, msg="permission denied", details=error_message)
        if self._redirect_to_route_name is not None and scheme_of_work_id > 0:
            self._redirect_to_url = reverse("team-permissions.login-as", args=[institute_id, department_id, scheme_of_work_id, str(permission)])
        
        return redirect(f"{self._redirect_to_url}?next={self._return_url}")
        