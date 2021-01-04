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
