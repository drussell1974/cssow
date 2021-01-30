from django.db import connection as db
from django.shortcuts import redirect
from shared.models.core.log_handlers import handle_log_info, handle_log_warning, handle_log_error
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

UNAUTHORISED_USER_ID = None
DEFAULT_SCHEME_OF_WORK_ID = 0
DEFAULT_LESSON_ID = 0

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

    def __init__(self, permission, login_url):
        """ SCHEMEOFWORK_ACCESS and LESSON_ACCESS decorator argument """
        self._permission = permission
        self._auth_user = 0
        self._scheme_of_work_id = 0
        self._redirect_to_url = login_url


    def __call__(self, func):
        """ the parent function """

        def inner(*args, **kwargs):
            ''' request must be the first argument in the view function '''
            self._auth_user = args[0].user.id
            self._return_url = args[0].path
            
            ''' scheme_of_work_id must be included in the view function or default '''
            self.kwargs = kwargs
            self._scheme_of_work_id = self.getkeyargs("scheme_of_work_id", default_value=DEFAULT_SCHEME_OF_WORK_ID)
            ''' teacher_id and auth_user are the same in this call'''
            model = TeacherPermissionModel.get_model(db, SchemeOfWorkModel(self._scheme_of_work_id), teacher_id=self._auth_user, auth_user=self._auth_user)
            handle_log_info(db, self._scheme_of_work_id, f"auth_user_id:{self._auth_user} - d:{model.department_permission},s:{model.scheme_of_work_permission},l:{model.lesson_permission}")
            if model.check_permission(self._permission) == False: 
                ''' redirect if user does not have permissions for this scheme of work '''
                str_err = \
                        f"You do not have {str(self._permission).split('.')[1]} permission for "\
                        f"this {str(self._permission).split('.')[0]} ({self._auth_user}, {self._scheme_of_work_id}) redirect to {self._redirect_to_url}. "

                return self.redirect_handler(str_err) 

            # call decorated function
            return func(*args, **kwargs)
            
        return inner

    def getkeyargs(self, key, default_value = None):
        if key in self.kwargs.keys():
            return self.kwargs[key]
        elif default_value is not None:
            return default_value
        else:
            raise KeyError(f"'{key}' value must be passed as a keyword argument")


    def redirect_handler(self, error_message):
        handle_log_warning(db, self._scheme_of_work_id, msg="permission denied", details=error_message)
        return redirect(f"{self._redirect_to_url}?next={self._return_url}")