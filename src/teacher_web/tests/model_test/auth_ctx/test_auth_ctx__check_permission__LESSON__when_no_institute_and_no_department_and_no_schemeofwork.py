from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import init_TestAuthCtx
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import LESSON
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model

class test_auth_ctx__check_permission__LESSON__when_no_institute_and_no_department_and_no_schemeofwork(TestCase):
    """ Simulates Web site level (no parameters) http://teacher.daverussell.co.uk/ - e.g. for creating new scheme of work """

    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass


    def test_when_user_is_authenticated(self):
        # arrange
        self.test = init_TestAuthCtx(institute_id=0, department_id=0, fake_request_user_id=6079)
        
        # act and assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))
        self.assertTrue(self.test.check_permission(LESSON.EDITOR))
        self.assertTrue(self.test.check_permission(LESSON.OWNER))


    def test_when_user_is_visitor(self):
        # arrange

        self.test = init_TestAuthCtx(institute_id=0, department_id=0, fake_request_user_id=None)
  
        # act and assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))
        self.assertTrue(self.test.check_permission(LESSON.EDITOR))
        self.assertTrue(self.test.check_permission(LESSON.OWNER))
