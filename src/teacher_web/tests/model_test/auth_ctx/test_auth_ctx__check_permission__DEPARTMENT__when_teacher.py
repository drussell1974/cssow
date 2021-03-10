from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import get_TestAuthCtx, get_fake_TeacherData
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model


class test_auth_ctx__check_permission__DEPARTMENT__when_teacher(TestCase):
    """ get fake data from sow_department__has__teacher from database """
    
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    
    def test_when_user_is_authenticated__no_permission_data(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = []
        
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)

        # act
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))
        self.assertFalse(self.test.check_permission(DEPARTMENT.STUDENT))
        self.assertFalse(self.test.check_permission(DEPARTMENT.TEACHER))
        self.assertFalse(self.test.check_permission(DEPARTMENT.HEAD))
        self.assertFalse(self.test.check_permission(DEPARTMENT.ADMIN))

    
    def test_when_user_is_authenticated__DEPARTMENT__assigned_head_of_department(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = []
        
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data, fake_user_is_hod=False, fake_user_is_creator=False)

        # act
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))
        self.assertFalse(self.test.check_permission(DEPARTMENT.STUDENT))
        self.assertFalse(self.test.check_permission(DEPARTMENT.TEACHER))
        self.assertFalse(self.test.check_permission(DEPARTMENT.HEAD))
        self.assertFalse(self.test.check_permission(DEPARTMENT.ADMIN))
