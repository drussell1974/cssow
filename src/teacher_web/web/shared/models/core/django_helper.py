from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel


def auth_user_model(db, request, institute_id=0, department_id=0):
    """ checks the user id in the request #253 check user id
    :param:db: the database context
    :param:request: the application request
    """
    return TeacherModel.get_model(db, teacher_id=request.user.id, department_id=department_id)