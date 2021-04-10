from datetime import datetime
from unittest.mock import Mock, patch
from shared.models.cls_academic_year import AcademicYearModel
from shared.models.cls_academic_year_period import AcademicYearPeriodModel
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionDataAccess
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import *

def get_fake_TeacherData(permission):
    
    department_permission = permission if type(permission) is DEPARTMENT else DEPARTMENT.NONE
    scheme_of_work_permission = permission if type(permission) is SCHEMEOFWORK else SCHEMEOFWORK.NONE
    lesson_permission = permission if type(permission) is LESSON else LESSON.NONE

    return [
            (777, "Fusce von Pulvinar" # teacher [0] [1]
            , 11, "Computer Science" # scheme of work [2] [3]
            , 67, "Computer Science" # department [4] [5]
            , 12767111276711, "Lorem Ipsum" # institute [6] [7]
            , scheme_of_work_permission # scheme_of_work_permission [8]
            , lesson_permission # lesson_permission [9]
            , department_permission # department_permission [10]
            , 1 # is_authorised [11]
            )]
            

def init_TestAuthCtx(institute_id, department_id, scheme_of_work_id = 0, fake_request_user_id = 0, fake_teacher_data=None):
    
    def get_hod():
        return 345

    def get_creator():
        return 346

    @patch.object(DepartmentContextModel, "cached", return_value=DepartmentContextModel(department_id, "Computer Science", hod_id=get_hod(), created_by_id=get_creator()))
    @patch.object(DepartmentContextModel, "from_dict", return_value=DepartmentContextModel(department_id, "Computer Science", hod_id=get_hod(), created_by_id=get_creator()))
    @patch.object(InstituteContextModel, "cached", return_value=InstituteContextModel(institute_id, "Lorem Ipsum", created_by_id=get_creator()))
    @patch.object(InstituteContextModel, "from_dict", return_value=InstituteContextModel(institute_id, "Lorem Ipsum", created_by_id=get_creator()))
    @patch.object(SchemeOfWorkContextModel, "cached", return_value=SchemeOfWorkContextModel(scheme_of_work_id, "CPU Architecture"))
    @patch.object(SchemeOfWorkContextModel, "from_dict", return_value=SchemeOfWorkContextModel(scheme_of_work_id, "CPU Architecture"))
    @patch.object(TeacherPermissionDataAccess, "get_model", return_value=get_fake_TeacherData(fake_teacher_data))
    @patch.object(AcademicYearModel, "get_model", return_value = fake_academic_year())
    @patch.object(AcademicYearModel, "get_all", return_value = fake_academic_years())
    @patch.object(AcademicYearPeriodModel, "get_all", return_value = fake_academic_year_periods())
    def inner_TestAuthCtx(institute_id, department_id, fake_request_user_id, mock_department_cached=None, mock_department_from_dict=None, mock_institute_cached=None, mock_institute_dict=None, mock_schemeofwork_cached=None, mock_schemeofwork_dict=None, mock_teacher_data=None, mock_academic_year=None, mock_academic_years=None, mock_academic_periods=None):
        
        # arrange
        
        mock_db = Mock()
        mock_db.cursor = Mock()

        mock_request = Mock()
        mock_request.user = Mock(id=fake_request_user_id)
        mock_request.session = Mock()
        mock_request.session = {
            "academic_year.start_date": datetime(year=2020, month=9, day=1),
            "academic_year.end_date": datetime(year=2021, month=7, day=15)
        }
        
        auth_ctx = AuthCtx(mock_db, mock_request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

        return auth_ctx


    return inner_TestAuthCtx(institute_id, department_id, fake_request_user_id)
