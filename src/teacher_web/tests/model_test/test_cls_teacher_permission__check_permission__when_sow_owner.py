from unittest import TestCase
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import SCHEMEOFWORK

class test_cls_teacher_permission__check_permission__when_sow_edit(TestCase):

    def setUp(self):
        # act
        ''' The scheme of work owner '''
        self.test = Model(auth_user=2, auth_user_name="", scheme_of_work=SchemeOfWorkModel(11), 
            scheme_of_work_permission=SCHEMEOFWORK.OWNER)


    def tearDown(self):
        pass


    def test_check__none_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))


    def test_check__owner_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.OWNER))


    def test_check__edit_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.EDITOR))


    def test_check__view_returns_true(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.VIEWER))
