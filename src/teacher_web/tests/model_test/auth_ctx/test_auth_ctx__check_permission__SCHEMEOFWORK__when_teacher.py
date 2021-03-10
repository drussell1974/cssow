from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import get_TestAuthCtx, get_fake_TeacherData
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model


class test_auth_ctx__check_permission__SCHEMEOFWORK__when_teacher(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    
    def test_should_return_false__when_user_is_authenticated__no_permission_data(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = []
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)
        
        # act and assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.VIEWER))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.OWNER))
    

    def test_should_return_false__when_user_is_authenticated__SCHEMEOFWORK_EDITOR(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = get_fake_TeacherData(scheme_of_work_permission=SCHEMEOFWORK.EDITOR)
        
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)
        
        # act and assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.VIEWER))
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.OWNER))


    def test_should_return_false__when_user_is_authenticated__SCHEMEOFWORK_NONE(self):
        # arrange
        # return matching teacher_data
        fake_teacher_data = get_fake_TeacherData(scheme_of_work_permission=SCHEMEOFWORK.NONE)

        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)
        
        # act and assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.VIEWER))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.OWNER))


    def test_should_return_false__when_user_is_authenticated__SCHEMEOFWORK_OWNER(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = get_fake_TeacherData(scheme_of_work_permission=SCHEMEOFWORK.OWNER)
        
        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)

        # act and assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.VIEWER))
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.OWNER))
    

    def test_should_return_false__when_user_is_authenticated__SCHEMEOFWORK_VIEWER(self):
        # arrange
        # return matching teacher_data
        fake_teacher_data = get_fake_TeacherData(scheme_of_work_permission=SCHEMEOFWORK.VIEWER)

        self.test = get_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)

        # act and assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.VIEWER))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.OWNER))
    