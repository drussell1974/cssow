from unittest import TestCase
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON

class test_cls_teacher_permission__check_permission__when_sow_edit(TestCase):

    def setUp(self):
        # act
        self.test = Model(auth_user=2,scheme_of_work_id=11, 
            scheme_of_work_permission=SCHEMEOFWORK.EDIT)


    def tearDown(self):
        pass


    def test_check__none_returns_false(self):
        # assert
        self.assertFalse(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.NONE))


    def test_check__edit_returns_true(self):
        # assert
        self.assertTrue(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.EDIT))
        

    def test_check__add_returns_false(self):
        # assert
        self.assertFalse(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.ADD))


    def test_check__view_returns_true(self):
        # assert
        self.assertTrue(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.VIEW))
