from unittest import TestCase, skip
from unittest.mock import MagicMock
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT
from tests.test_helpers.mocks import fake_ctx_model


class test_cls_teacher_permission__check_permission__when_department_head(TestCase):

    def setUp(self):
        # act
        #fake_user_model = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        #fake_user_model.get_username = MagicMock(return_value="Dave Russell")
        self.test = Model(teacher_id=6079, teacher_name="Dave Russell", scheme_of_work=SchemeOfWorkModel(11), ctx=fake_ctx_model(),
            department_permission=DEPARTMENT.HEAD)
        self.test.is_authorised = True


    def tearDown(self):
        pass


    def test_check__none_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))


    def test_check__student_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.STUDENT))


    def test_check__teacher_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.TEACHER))


    def test_check__teacher_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.HEAD))


    def test_should_be_false__when_is_authorised__false(self):
        # arrange

        self.test.is_authorised = False
        
        # assert
        self.assertFalse(self.test.check_permission(DEPARTMENT.HEAD))
        self.assertFalse(self.test.check_permission(DEPARTMENT.TEACHER))
        self.assertFalse(self.test.check_permission(DEPARTMENT.STUDENT))
        self.assertFalse(self.test.check_permission(DEPARTMENT.NONE))