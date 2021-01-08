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
        self._redirect_to_url = redirect_to_url


    def __call__(self, func):
        """ the parent function """

        def inner(*args, **kwargs):
            print("call innert")
            for arg in args:
                print(arg)
                
            for arg in kwargs:
                print(arg)  
            '''
            scheme_of_work_id = kwargs["scheme_of_work_id"]
            lesson_id = kwargs["lesson_id"]
            '''
            model = TeacherPermissionModel.get_model(self.db, 0, 0)
            if model.check_permission(self._permission) == False:
                print(f"redirecting to {self._redirect_to_url}")
                return HttpResponseRedirect(self._redirect_to_url)
            else:
                print("user {selfpermission ")
                
        return inner
