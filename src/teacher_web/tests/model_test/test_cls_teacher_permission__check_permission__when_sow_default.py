from unittest import TestCase
from unittest.mock import MagicMock
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK

class test_cls_teacher_permission__check_permission__when_sow_default(TestCase):

    def setUp(self):
        # act
        fake_user_model = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science"))
        fake_user_model.get_username = MagicMock(return_value="Dave Russell")
        self.test = Model(teacher=fake_user_model, scheme_of_work=SchemeOfWorkModel(11))
        self.test.is_authorised = True
        

    def tearDown(self):
        pass


    def test_check__has_no_permission_by_default(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))


    def test_check__not_an_owner_by_default(self):
        # assert
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.OWNER))


    def test_check__cannot_edit_by_default(self):
        # assert
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
    

    def test_check__cannot_view_by_default(self):
        # assert
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.VIEWER))


    def test_should_be_false__when_is_authorised__false(self):
        # arrange

        self.test.is_authorised = False
        
        # assert
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.VIEWER))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.OWNER))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.NONE))