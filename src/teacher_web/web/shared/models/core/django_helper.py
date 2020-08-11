def auth_user_id(request):
    """ checks the user id in the request #253 check user id
    :param:request: the application request
    """
    return request.user.id if request.user.id is not None else 0
