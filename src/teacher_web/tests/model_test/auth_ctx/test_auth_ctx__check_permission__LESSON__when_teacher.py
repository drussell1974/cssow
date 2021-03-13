from unittest import TestCase, skip
from unittest.mock import Mock, patch
from .base_authctx_testcase import init_TestAuthCtx, get_fake_TeacherData
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import LESSON, DEPARTMENT
from shared.models.enums.publlished import STATE
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import fake_ctx_model


class test_auth_ctx__check_permission__LESSON__when_teacher(TestCase):
    """ get data fake data from sow_scheme_of_work__has__teacher from database """
    
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    
    def test_when_user_is_authenticated__no_data(self):
        # arrange
        
        ''' return matching teacher_data '''
           
        fake_teacher_data = DEPARTMENT.NONE

        self.test = init_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)
        
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertFalse(self.test.check_permission(LESSON.VIEWER))
        self.assertFalse(self.test.check_permission(LESSON.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))
     
     
    def test_when_user_is_authenticated__LESSON_NONE(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = LESSON.NONE
        
        self.test = init_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)

        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertFalse(self.test.check_permission(LESSON.VIEWER))
        self.assertFalse(self.test.check_permission(LESSON.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))


    def test_when_user_is_authenticated__LESSON_VIEWER(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = LESSON.VIEWER
        
        self.test = init_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)
        
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))
        self.assertFalse(self.test.check_permission(LESSON.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))
        

    def test_when_user_is_authenticated__LESSON_EDITOR(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = LESSON.EDITOR
        
        self.test = init_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)
        
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))
        self.assertTrue(self.test.check_permission(LESSON.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))
    

    def test_when_user_is_authenticated__LESSON_OWNER(self):
        # arrange
        # return matching teacher_data        
        fake_teacher_data = LESSON.OWNER
        
        self.test = init_TestAuthCtx(institute_id=12767111276711, department_id=67, scheme_of_work_id=11, fake_request_user_id=6079, fake_teacher_data=fake_teacher_data)
        
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))
        self.assertTrue(self.test.check_permission(LESSON.EDITOR))
        self.assertTrue(self.test.check_permission(LESSON.OWNER))
    