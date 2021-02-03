from unittest import TestCase
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
        self.test = Model(teacher_id=2, teacher_name="Mr Russell", scheme_of_work=SchemeOfWorkModel(11))

        # assert
        self.assertEqual(2, self.test.teacher_id)
        self.assertEqual(11, self.test.scheme_of_work.id)
        self.assertEqual(SCHEMEOFWORK.NONE, self.test.scheme_of_work_permission)
        self.assertEqual(LESSON.NONE, self.test.lesson_permission)
