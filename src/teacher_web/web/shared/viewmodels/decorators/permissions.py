from django.db import connection as db
from django.http import HttpResponseRedirect
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.models.cls_teacher_permission import TeacherPermissionModel

def unauthorise_request(func):
    """
    changes to request.user.id to UNAUTHORISED_USER_ID 
    """
    
    UNAUTHORISED_USER_ID = None
    
    def inner(*args, **kwargs):
        for arg in args:   
            if hasattr(arg, 'user') and hasattr(arg.user, 'id'):
                arg.user.id = UNAUTHORISED_USER_ID
        return func(*args, **kwargs)
    return inner


class check_teacher_permission:
    """ checks the teachers permission on the scheme of work and redirect if user does not have permission """

    def __init__(self, permission, redirect_to_url):
        """ SCHEMEOFWORK_ACCESS and LESSON_ACCESS decorator argument """
        self._permission = permission
        self._auth_user = 0
        self._scheme_of_work_id = 0
        self._redirect_to_url = redirect_to_url


    def __call__(self, func):
        """ the parent function """

        def inner(*args, **kwargs):
            if "auth_user" in kwargs.keys():
                self._auth_user = kwargs["auth_user"]
            if "scheme_of_work_id" in kwargs.keys():
                self._scheme_of_work_id = kwargs["scheme_of_work_id"]
            model = TeacherPermissionModel.get_model(db, self._auth_user, self._scheme_of_work_id)
            if model.check_permission(self._permission) == False:            
                raise PermissionError(f"You do not have permission to {str(self._permission).split('.')[1]} view this {str(self._permission).split('.')[0]}") 

            # call decorated function
            func(*args, **kwargs)
            
        return inner
