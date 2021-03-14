from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import init_TestAuthCtx
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model

class test_auth_ctx__check_permission__when_no_institute_and_no_department__SCHEMEOFWORK(TestCase):

    def setUp(self):

        # arrange
        
        self.test = init_TestAuthCtx(institute_id=0, department_id=0, fake_request_user_id=6079)


    def tearDown(self):
        pass
    

    def test_should_return_false__when_user_is_authenticated__permissions_required__SCHEMEOFWORK_NONE(self):
        
        # act
        actual_result = self.test.check_permission(SCHEMEOFWORK.NONE)

        # assert
        self.assertTrue(actual_result)


    def test_should_return_false__when_user_is_authenticated__and__permissions_required__SCHEMEOFWORK_VIEWER(self):
        
        # act
        actual_result = self.test.check_permission(SCHEMEOFWORK.VIEWER)

        # assert
        self.assertTrue(actual_result)



    def test_should_return_false__when_user__is_authenticated__and__permissions_required__SCHEMEOFWORK_EDITOR(self):
        
        # act
        actual_result = self.test.check_permission(SCHEMEOFWORK.EDITOR)

        # assert
        self.assertTrue(actual_result)


    def test_should_return_false__when_user__is_authenticated__and__permissions_required__SCHEMEOFWORK_OWNER(self):
        
        # act
        actual_result = self.test.check_permission(SCHEMEOFWORK.OWNER)
        
        # assert
        self.assertTrue(actual_result)