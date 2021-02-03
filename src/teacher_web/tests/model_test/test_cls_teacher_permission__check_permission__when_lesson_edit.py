from unittest import TestCase
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import LESSON

class test_cls_teacher_permission__check_permission__when_lesson_edit(TestCase):

    def setUp(self):
        # act
        self.test = Model(teacher_id=2, teacher_name="", scheme_of_work=SchemeOfWorkModel(11),
            lesson_permission=LESSON.EDITOR)
        self.test.is_authorised = True


    def tearDown(self):
        pass


    def test_check__none_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))


    def test_check__owner_returns_false(self):
        # assert
        self.assertFalse(self.test.check_permission(LESSON.OWNER))
        

    def test_check__edit_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(LESSON.EDITOR))
        

    def test_check__view_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(LESSON.VIEWER))


    def test_should_be_false__when_is_authorised__false(self):
        # arrange

        self.test.is_authorised = False
        
        # assert
        self.assertFalse(self.test.check_permission(LESSON.VIEWER))
        self.assertFalse(self.test.check_permission(LESSON.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))
        self.assertFalse(self.test.check_permission(LESSON.NONE))