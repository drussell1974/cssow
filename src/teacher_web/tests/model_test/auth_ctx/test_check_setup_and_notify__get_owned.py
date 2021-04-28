from unittest import TestCase, skip
from unittest.mock import Mock, patch
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_notification import NotifyModel
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_check_setup_and_notify__get_owned(TestCase):
    
    def setUp(self):
        self.mock_request = MagicMock()
        self.mock_request.user = MagicMock(id=6079)

        self.mock_db = Mock()
        self.mock_db.cursor = MagicMock()
    
    def tearDown(self):
        pass


    def test__call_institutemodel_get_my__returns_no_institutes(self, mock_auth_ctx):
        """ should call InstituteModel.get_my but not DepartmentModel.get_my """
        # arrange
        with patch.object(InstituteModel, "get_my", return_value=[]):
            with patch.object(DepartmentModel, "get_my", return_value=[]):
                # act
                AuthCtx.check_setup_and_notify(self.mock_db, self.mock_request, mock_auth_ctx)
                # assert
                InstituteModel.get_my.assert_called()
                DepartmentModel.get_my.assert_not_called()


    def test__call_departmentmodel_get_my__returns_no_departments(self, mock_auth_ctx):
        """ should call InstituteModel.get_my and DepartmentModel.get_my """
        # arrange
        with patch.object(InstituteModel, "get_my", return_value=[fake_institute()]):
            with patch.object(DepartmentModel, "get_my", return_value=[]):
                # act
                AuthCtx.check_setup_and_notify(self.mock_db, self.mock_request, mock_auth_ctx)
                # assert
                InstituteModel.get_my.assert_called()
                DepartmentModel.get_my.assert_called()


    def test__call_schemeofworkmodel_get_my__returns_has_departments(self, mock_auth_ctx):
        """ should call InstituteModel.get_my and DepartmentModel.get_my """
        # arrange
        fake_inst = fake_institute()

        with patch.object(InstituteModel, "get_my", return_value=[fake_inst]):
            with patch.object(DepartmentModel, "get_my", return_value=[fake_department(76, fake_inst)]):
                with patch.object(SchemeOfWorkModel, "get_my", return_value=[mock_scheme_of_work().__dict__]):
                    # act
                    AuthCtx.check_setup_and_notify(self.mock_db, self.mock_request, mock_auth_ctx)
                    # assert
                    InstituteModel.get_my.assert_called()
                    DepartmentModel.get_my.assert_called()
                    SchemeOfWorkModel.get_my.assert_called()