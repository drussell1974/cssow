from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import init_TestAuthCtx
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model


class test_auth_ctx__check_permission__when_institute_and_department_exist__DEPARTMENT__creator(TestCase):

    def setUp(self):
        
        # arrange
        self.test = init_TestAuthCtx(institute_id=12767111276711, department_id=67, fake_request_user_id=6079)


    def tearDown(self):
        pass
        
    
    def test_should_return_false__when_user_is_authenticated__and__permissions_required__DEPARTMENT_NONE(self):
        
        # act
        actual_result = self.test.check_permission(DEPARTMENT.NONE)

        # assert
        self.assertTrue(actual_result)


    def test_should_return_false__when_user_is_authenticated__and__permissions_required__DEPARTMENT_STUDENT(self):

        # act
        actual_result = self.test.check_permission(DEPARTMENT.STUDENT)

        # assert
        self.assertFalse(actual_result)
        

    def test_should_return_false__when_user__is_authenticated__and__permissions_required__DEPARTMENT_HEAD(self):
        
        # act
        actual_result = self.test.check_permission(DEPARTMENT.HEAD)

        # assert
        self.assertFalse(actual_result)


    def test_should_return_false__when_user__is_authenticated__and__permissions_required__DEPARTMENT_ADMIN(self):
        
        # act
        actual_result = self.test.check_permission(DEPARTMENT.ADMIN)

        # assert
        self.assertFalse(actual_result)
    