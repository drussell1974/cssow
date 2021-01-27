from unittest import TestCase, skip
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT

class test_cls_teacher_permission__check_permission__when_department_none(TestCase):

    def setUp(self):
        # act
        self.test = Model(auth_user=2, auth_user_name="", scheme_of_work=SchemeOfWorkModel(11),
            department_permission=DEPARTMENT.NONE)

        pass

    def tearDown(self):
        pass


    def test_check__none_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(DEPARTMENT.NONE))


    def test_check__student_returns_false(self):
        # assert
        self.assertFalse(self.test.check_permission(DEPARTMENT.STUDENT))


    def test_check__teacher_returns_false(self):
        # assert
        self.assertFalse(self.test.check_permission(DEPARTMENT.TEACHER))
        

    def test_check__teacher_returns_false(self):
        # assert
        self.assertFalse(self.test.check_permission(DEPARTMENT.HEAD))
