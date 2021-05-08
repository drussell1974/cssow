from unittest import TestCase
from unittest.mock import MagicMock
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK
from tests.test_helpers.mocks import fake_ctx_model

class test_cls_teacher_permission__check_permission__when_sow_edit(TestCase):

    def setUp(self):
        # act
        ''' The scheme of work owner '''
        #fake_user_model = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        self.test = Model(teacher_id=6079, teacher_name="Dave Russell", join_code="ABCDEFGH", scheme_of_work=SchemeOfWorkModel(11, name="KS3 Computing", study_duration=3, start_study_in_year=7), ctx=fake_ctx_model(), 
            scheme_of_work_permission=SCHEMEOFWORK.OWNER)
        self.test.is_authorised = True


    def tearDown(self):
        pass


    def test_check__none_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))


    def test_check__owner_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.OWNER))


    def test_check__edit_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.EDITOR))


    def test_check__view_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.VIEWER))


    def test_should_be_false__when_is_authorised__false(self):
        # arrange

        self.test.is_authorised = False
        
        # assert
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.VIEWER))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.OWNER))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.NONE))