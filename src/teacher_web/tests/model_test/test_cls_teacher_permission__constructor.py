from unittest import TestCase
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON

class test_cls_teacher_permission__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = Model(auth_user=2,scheme_of_work_id=11)

        # assert
        self.assertEqual(2, self.test.auth_user)
        self.assertEqual(11, self.test.scheme_of_work_id)
        self.assertEqual(SCHEMEOFWORK.NONE, self.test.scheme_of_work_permission)
        self.assertEqual(LESSON.NONE, self.test.lesson_permission)
