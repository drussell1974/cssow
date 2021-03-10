from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import get_TestAuthCtx
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model

class test_auth_ctx__check_permission__DEPARTMENT__when_no_institute_and_no_department_and_no_schemeofwork(TestCase):
    """ Simulates Web site level (no parameters) http://teacher.daverussell.co.uk/ - e.g. for creating new scheme of work """

    def setUp(self):
        pass

    def tearDown(self):
        pass
    

    def test_when_user_is_creator(self):
        # arrange
        self.test = get_TestAuthCtx(institute_id=0, department_id=0, fake_request_user_id=6079, fake_user_is_creator=True)
        
        # act and assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))
        self.assertTrue(self.test.check_permission(DEPARTMENT.STUDENT))
        self.assertTrue(self.test.check_permission(DEPARTMENT.HEAD))
        self.assertTrue(self.test.check_permission(DEPARTMENT.ADMIN))


    def test_when_user_is_head_of_department(self):
        # arrange
        self.test = get_TestAuthCtx(institute_id=0, department_id=0, fake_request_user_id=6079, fake_user_is_hod=True)
        
        # act and assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))
        self.assertTrue(self.test.check_permission(DEPARTMENT.STUDENT))
        self.assertTrue(self.test.check_permission(DEPARTMENT.HEAD))
        self.assertTrue(self.test.check_permission(DEPARTMENT.ADMIN))


    def test_when_user_is_authenticated(self):
        # arrange
        
        self.test = get_TestAuthCtx(institute_id=0, department_id=0, fake_request_user_id=6079)
        
        # act and assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))
        self.assertTrue(self.test.check_permission(DEPARTMENT.STUDENT))
        self.assertTrue(self.test.check_permission(DEPARTMENT.HEAD))
        self.assertTrue(self.test.check_permission(DEPARTMENT.ADMIN))


    def test_when_user_is_visitor(self):
        # arrange
        
        self.test = get_TestAuthCtx(institute_id=0, department_id=0, fake_request_user_id=None)
        
        # act and assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))
        self.assertTrue(self.test.check_permission(DEPARTMENT.STUDENT))
        self.assertTrue(self.test.check_permission(DEPARTMENT.HEAD))
        self.assertTrue(self.test.check_permission(DEPARTMENT.ADMIN))
