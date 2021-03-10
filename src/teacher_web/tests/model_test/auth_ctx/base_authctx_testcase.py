from unittest.mock import Mock, patch
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionDataAccess
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx

def get_fake_TeacherData(department_permission=DEPARTMENT.NONE, scheme_of_work_permission=SCHEMEOFWORK.NONE, lesson_permission=LESSON.NONE):
    return [
            (777, "Fusce von Pulvinar" # teacher [0] [1]
            , 11, "Computer Science" # scheme of work [2] [3]
            , 67, "Computer Science" # department [4] [5]
            , 12767111276711, "Lorem Ipsum" # institute [6] [7]
            , int(scheme_of_work_permission) # scheme_of_work_permission [8]
            , int(lesson_permission) # lesson_permission [9]
            , int(department_permission) # department_permission [10]
            , 1 # is_authorised [11]
            )]

    return []

def get_TestAuthCtx(institute_id, department_id, scheme_of_work_id = 0, fake_request_user_id = 0, fake_user_is_hod=False, fake_user_is_creator=False, fake_teacher_data=None):
    
    def get_hod():
        return fake_request_user_id if fake_user_is_hod == True else 345

    def get_creator():
        return fake_request_user_id if fake_user_is_creator == True else 346

    @patch.object(DepartmentContextModel, "cached", return_value=DepartmentContextModel(department_id, "Computer Science", hod_id=get_hod(), created_by_id=get_creator()))
    @patch.object(DepartmentContextModel, "from_dict", return_value=DepartmentContextModel(department_id, "Computer Science", hod_id=get_hod(), created_by_id=get_creator()))
    @patch.object(InstituteContextModel, "cached", return_value=InstituteContextModel(institute_id, "Lorem Ipsum", created_by_id=get_creator()))
    @patch.object(InstituteContextModel, "from_dict", return_value=InstituteContextModel(institute_id, "Lorem Ipsum", created_by_id=get_creator()))
    @patch.object(SchemeOfWorkContextModel, "cached", return_value=SchemeOfWorkContextModel(scheme_of_work_id, "CPU Architecture"))
    @patch.object(SchemeOfWorkContextModel, "from_dict", return_value=SchemeOfWorkContextModel(scheme_of_work_id, "CPU Architecture"))
    @patch.object(TeacherPermissionDataAccess, "get_model", return_value=fake_teacher_data)
    def _get_TestAuthCtx(institute_id, department_id, fake_request_user_id, mock_department_cached=None, mock_department_from_dict=None, mock_institute_cached=None, mock_institute_dict=None, mock_schemeofwork_cached=None, mock_schemeofwork_dict=None, mock_teacher_data=None):
        
        # arrange
        
        mock_db = Mock()
        mock_db.cursor = Mock()

        mock_request = Mock()
        mock_request.user = Mock(id=fake_request_user_id)

        auth_ctx = AuthCtx(mock_db, mock_request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
        
        if fake_teacher_data is not None:
            TeacherPermissionDataAccess.get_model.assert_called()
        else:
            TeacherPermissionDataAccess.get_model.assert_not_called()

        return auth_ctx


    return _get_TestAuthCtx(institute_id, department_id, fake_request_user_id)