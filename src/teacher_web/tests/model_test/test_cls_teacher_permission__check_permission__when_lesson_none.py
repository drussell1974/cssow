from unittest import TestCase, skip
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON


class test_cls_teacher_permission__check_permission__when_lesson_none(TestCase):

    def setUp(self):
        # act
        self.test = Model(auth_user=2,scheme_of_work_id=11, 
            lesson_permission=LESSON.NONE)

        pass

    def tearDown(self):
        pass


    def test_check__none_returns_true(self):
        # assert
        self.assertTrue(self.test.check_lesson_permission(LESSON.NONE))


    def test_check__edit_returns_false(self):
        # assert
        self.assertFalse(self.test.check_lesson_permission(LESSON.EDIT))
        

    def test_check__add_returns_false(self):
        # assert
        self.assertFalse(self.test.check_lesson_permission(LESSON.ADD))


    def test_check__view_returns_false(self):
        # assert
        self.assertFalse(self.test.check_lesson_permission(LESSON.VIEW))
