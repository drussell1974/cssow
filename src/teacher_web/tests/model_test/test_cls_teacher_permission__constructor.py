from unittest import TestCase, skip
from unittest.mock import MagicMock
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON
from tests.test_helpers.mocks import fake_ctx_model

class test_cls_teacher_permission__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        #fake_user_model = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        #fake_user_model.get_username = MagicMock(return_value="Dave Russell")
        self.test = Model(teacher_id=6079, teacher_name="Dave Russell", join_code="ABCDEFGH", scheme_of_work=SchemeOfWorkModel(11, name="KS3 Computing", study_duration=3, start_study_in_year=7), ctx=fake_ctx_model())

        # assert
        self.assertEqual(6079, self.test.teacher_id)
        self.assertEqual(11, self.test.scheme_of_work_id)
        self.assertEqual(SCHEMEOFWORK.NONE, self.test.scheme_of_work_permission)
        self.assertEqual(LESSON.NONE, self.test.lesson_permission)
