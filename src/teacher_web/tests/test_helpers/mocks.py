from unittest.mock import Mock, MagicMock
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.core.context import AuthCtx, Ctx

mock_scheme_of_work = SchemeOfWorkModel(99, name="A-Level Computer Science", auth_user=Ctx(1276711, 826))

def fake_ctx_model(dep=DEPARTMENT.NONE, sow=SCHEMEOFWORK.NONE, les=LESSON.NONE, trace=False):
    
    mock_request = MagicMock()
    mock_request.user = MagicMock(id=6079)
    mock_request.session = {}

    mock_db = Mock()
    mock_db.cursor = MagicMock()
    
    institute = InstituteModel(127671276711, name="Lorum Ipsum")
    
    department = DepartmentModel(67, name="Computer Science", institute=institute, is_from_db=True)
    
    if trace == True:
        KeyError(department.id)

    scheme_of_work = SchemeOfWorkModel(12323232, name="GCSE Computer Science", auth_user=Ctx(1276711, 826))

    auth_ctx = AuthCtx(mock_db, mock_request, institute_id=institute.id, department_id=department.id, scheme_of_work_id=scheme_of_work.id)
    auth_ctx.department_permission = dep
    auth_ctx.scheme_of_work_permission = sow
    auth_ctx.lesson_permission = les

    return auth_ctx

'''
def fake_teacher_model(auth_user_id = 6079, department_permission=DEPARTMENT.HEAD, scheme_of_work_permission=SCHEMEOFWORK.OWNER, lesson_permission=LESSON.OWNER, is_authorised=False):

    permission_ctx = TeacherPermissionModel(teacher_id=9999, teacher_name="Dave Russell", scheme_of_work=mock_scheme_of_work, is_from_db=True, ctx=fake_ctx_model())
    
    permission_ctx.is_authorised = is_authorised
    permission_ctx.department_permission = department_permission
    permission_ctx.scheme_of_work_permission = scheme_of_work_permission
    permission_ctx.lesson_permission = lesson_permission
    permission_ctx.auth_user_id = auth_user_id
    
    return permission_ctx
'''

def fake_teacher_permission_model(is_from_db=True, is_authorised=True):

    mock_request = MagicMock()
    mock_request.user = MagicMock(id=6079)
    mock_request.session = {}

    mock_db = Mock()
    mock_db.cursor = MagicMock()
    
    institute = InstituteModel(127671276711, name="Lorum Ipsum")
    
    department = DepartmentModel(67, "Computer Science", institute=institute, is_from_db=True)

    scheme_of_work = SchemeOfWorkModel(14, name="A-Level Computer Science", is_from_db=is_from_db, auth_user=AuthCtx(mock_db, mock_request, institute.id, department.id))
    
    auth_ctx = AuthCtx(mock_db, mock_request, institute_id=127671276711, department_id=34, scheme_of_work_id=14)

    return TeacherPermissionModel(teacher_id=56, teacher_name="Jane Mellor" , scheme_of_work=scheme_of_work, is_from_db=is_from_db, ctx=auth_ctx, scheme_of_work_permission=SCHEMEOFWORK.OWNER, lesson_permission=LESSON.OWNER, department_permission=DEPARTMENT.HEAD, is_authorised=is_authorised)
