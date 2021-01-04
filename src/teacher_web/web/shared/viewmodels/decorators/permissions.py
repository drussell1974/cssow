from shared.models.enums.permissions import TEACHER_SCHEMEOFWORK, TEACHER_LESSON 

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


def check_teacher_permission(func, redirect_to_url):
    """ checks the teachers permission on the scheme of work and redirect if user does not have permission """
    def inner(*args, **kwargs):

        raise KeyError(kwargs)
        for arg in kwargs:
            pass
            # TODO: 206 1. check if teacher has permission on scheme_of_work
            # TODO: 206 2. check if teacher has permission on lesson_id
            # TODO: 206 redirect to url
            # TODO: 206 return True if allowed
        return False
    return inner