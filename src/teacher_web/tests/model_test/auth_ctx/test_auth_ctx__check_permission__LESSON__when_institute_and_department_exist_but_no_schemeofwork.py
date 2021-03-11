from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import get_TestAuthCtx
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import LESSON
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model


class test_auth_ctx__check_permission__LESSON__when_institute_and_department_exist_but_no_schemeofwork(TestCase):
    """ Simulates Department level, with institute_id and department_id http://teacher.daverussell.co.uk/insitute/2/department/5/schemesofwork - e.g. for creating new scheme of work """

    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    
    def test_when_user_is_authenticated(self):
        # arrange
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=0, fake_request_user_id=6079)

        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertFalse(self.test.check_permission(LESSON.VIEWER))
        self.assertFalse(self.test.check_permission(LESSON.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))


    def test_when_user_visitor(self):
        # arrange
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=0, fake_request_user_id=None)

        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertFalse(self.test.check_permission(LESSON.VIEWER))
        self.assertFalse(self.test.check_permission(LESSON.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))


    def test_when_user_is_authenticated__and__is_head_of_department(self):
        # arrange
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=0, fake_request_user_id=6079, fake_user_is_hod=True)
        
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))
        self.assertTrue(self.test.check_permission(LESSON.EDITOR))
        self.assertTrue(self.test.check_permission(LESSON.OWNER))


    def test_when_user_is_authenticated__and__is_creator(self):
        # arrange
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=0, fake_request_user_id=6079, fake_user_is_creator=True)
        
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))
        self.assertTrue(self.test.check_permission(LESSON.EDITOR))
        self.assertTrue(self.test.check_permission(LESSON.OWNER))