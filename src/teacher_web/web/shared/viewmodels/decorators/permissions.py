from django.http import HttpResponseRedirect
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.models.cls_teacher_permission import TeacherPermissionModel

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


class check_teacher_permission:
    """ checks the teachers permission on the scheme of work and redirect if user does not have permission """

    def __init__(self, permission, redirect_to_url="/"):
        """ SCHEMEOFWORK_ACCESS and LESSON_ACCESS decorator argument """
        self._permission = permission
        self._auth_user = 0
        self._scheme_of_work_id = 0
        self._redirect_to_url = redirect_to_url


    def getkeyargs(self, key, default_value = None):
        if key in self.kwargs.keys():
            return self.kwargs[key]
        elif default_value is not None:
            return default_value
        else:
            raise KeyError(f"'{key}' value must be passed as a keyword argument")


    def __call__(self, func):
        """ the parent function """

        def inner(*args, **kwargs):
            self.kwargs = kwargs
            self.db = self.getkeyargs("db") # db cannot be a positional argument
            self._auth_user = self.getkeyargs("auth_user") # auth_user cannot be a positiional argument
            self._lesson_id = self.getkeyargs("lesson_id", default_value=DEFAULT_LESSON_ID)
            self._scheme_of_work_id = self.getkeyargs("scheme_of_work_id", default_value=DEFAULT_SCHEME_OF_WORK_ID)
            
            if self._scheme_of_work_id == DEFAULT_SCHEME_OF_WORK_ID:
                # try the model
                model = self.getkeyargs("model")
                if model is not None:
                    self._scheme_of_work_id = model.scheme_of_work_id

            '''
            if self._lesson_id == DEFAULT_LESSON_ID:
                # try the model
                model = self.getkeyargs("model")
                if model is not None:
                    self._scheme_of_work_id = model.lesson_id
            '''
            
            str_err = f"You do not have permission to {str(self._permission).split('.')[1]} this {str(self._permission).split('.')[0]} ({self._scheme_of_work_id})" 
            
            model = TeacherPermissionModel.get_model(self.db, scheme_of_work_id=self._scheme_of_work_id, auth_user=self._auth_user)
            if model.check_permission(self._permission) == False:           
                raise PermissionError(str_err) 

            # call decorated function
            func(*args, **kwargs)
            
        return inner
