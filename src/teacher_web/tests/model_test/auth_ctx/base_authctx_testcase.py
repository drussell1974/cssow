from unittest.mock import Mock, patch
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx


def get_TestAuthCtx(institute_id, department_id, scheme_of_work_id = 0, fake_request_user_id = 0, fake_user_is_hod=False, fake_user_is_creator=False):
    
    def get_hod():
        return fake_request_user_id if fake_user_is_hod == True else 345

    def get_creator():
        return fake_request_user_id if fake_user_is_creator == True else 345

    @patch.object(DepartmentContextModel, "cached", return_value=DepartmentContextModel(department_id, "Computer Science", hod_id=get_hod(), created_by_id=get_creator()))
    @patch.object(DepartmentContextModel, "from_dict", return_value=DepartmentContextModel(department_id, "Computer Science", hod_id=get_hod(), created_by_id=get_creator()))
    @patch.object(InstituteContextModel, "cached", return_value=InstituteContextModel(institute_id, "Lorem Ipsum", created_by_id=get_creator()))
    @patch.object(InstituteContextModel, "from_dict", return_value=InstituteContextModel(institute_id, "Lorem Ipsum", created_by_id=get_creator()))
    @patch.object(SchemeOfWorkContextModel, "cached", return_value=SchemeOfWorkContextModel(scheme_of_work_id, "CPU Architecture"))
    @patch.object(SchemeOfWorkContextModel, "from_dict", return_value=SchemeOfWorkContextModel(scheme_of_work_id, "CPU Architecture"))
    def _get_TestAuthCtx(institute_id, department_id, fake_request_user_id, mock_department_cached=None, mock_department_from_dict=None, mock_institute_cached=None, mock_institute_dict=None, mock_schemeofwork_cached=None, mock_schemeofwork_dict=None):
        
        # arrange
        
        mock_db = Mock()
        mock_db.cursor = Mock()

        mock_request = Mock()
        mock_request.user = Mock(id=fake_request_user_id)

        return AuthCtx(mock_db, mock_request, institute_id=institute_id, department_id=department_id)


    return _get_TestAuthCtx(institute_id, department_id, fake_request_user_id)