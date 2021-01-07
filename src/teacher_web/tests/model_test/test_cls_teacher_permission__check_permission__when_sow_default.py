from unittest import TestCase
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON

class test_cls_teacher_permission__check_permission__when_sow_default(TestCase):

    def setUp(self):
        # act
        self.test = Model(auth_user=2,scheme_of_work_id=11)
        

    def tearDown(self):
        pass


    def test_check__has_no_permission_by_default(self):
        # assert
        self.assertTrue(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.NONE))


    def test_check__cannot_edit_by_default(self):
        # assert
        self.assertFalse(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.EDIT))
        

    def test_check__cannot_add_by_default(self):
        # assert
        self.assertFalse(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.ADD))


    def test_check__cannot_view_by_default(self):
        # assert
        self.assertFalse(self.test.check_scheme_of_work_permission(SCHEMEOFWORK.VIEW))