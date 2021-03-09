from unittest import TestCase
from unittest.mock import Mock, patch
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx

@patch.object(DepartmentContextModel, "cached", return_value=DepartmentContextModel(0, "", hod_id=0, created_by_id=0))
@patch.object(DepartmentContextModel, "from_dict", return_value=DepartmentContextModel(0, "", hod_id=0, created_by_id=0))
@patch.object(InstituteContextModel, "cached", return_value=InstituteContextModel(0, "", created_by_id=0))
@patch.object(InstituteContextModel, "from_dict", return_value=InstituteContextModel(0, "", created_by_id=0))
@patch.object(SchemeOfWorkContextModel, "cached", return_value=SchemeOfWorkContextModel(0, "").__dict__)
@patch.object(SchemeOfWorkContextModel, "from_dict", return_value=SchemeOfWorkContextModel(0, ""))
class test_auth_ctx__check_permission__DEPARTMENT_NONE(TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    
    def test_should_return_false__when_user_none(self, mock_department_cached, mock_department_from_dict, mock_institute_cached, mock_institute_dict, mock_schemeofwork_cached, mock_schemeofwork_dict):
        
        # arrange
        
        db = Mock()
        db.cursor = Mock()

        mock_request = Mock()
        mock_request.user = Mock(id=None)

        test = AuthCtx(db, mock_request, institute_id=0, department_id=0)

        with patch.object(TeacherPermissionModel, "get_model", return_value=TeacherPermissionModel.default(mock_institute_dict, mock_department_from_dict, None, test)):
            # act
            actual_result = test.check_permission(DEPARTMENT.NONE)

            # assert
            self.assertTrue(actual_result)
