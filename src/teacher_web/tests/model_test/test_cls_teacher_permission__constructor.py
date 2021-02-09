from unittest import TestCase
from unittest.mock import MagicMock
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON

class test_cls_teacher_permission__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        fake_user_model = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science"))
        fake_user_model.get_username = MagicMock(return_value="Dave Russell")
        self.test = Model(teacher=fake_user_model, scheme_of_work=SchemeOfWorkModel(11))

        # assert
        self.assertEqual(6079, self.test.teacher.id)
        self.assertEqual(11, self.test.scheme_of_work.id)
        self.assertEqual(SCHEMEOFWORK.NONE, self.test.scheme_of_work_permission)
        self.assertEqual(LESSON.NONE, self.test.lesson_permission)
