from unittest import TestCase, skip
from unittest.mock import Mock, patch
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_notification import NotifyModel
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import *

@patch.object(InstituteModel, "get_my", return_value=[fake_institute()])
@patch.object(DepartmentModel, "get_my", return_value=[fake_department(76, fake_institute())])
@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_check_setup_and_notify__notify_schemeofwork(TestCase):
    
    def setUp(self):
        self.mock_request = MagicMock()
        self.mock_request.user = MagicMock(id=6079)

        self.mock_db = Mock()
        self.mock_db.cursor = MagicMock()
    
    def tearDown(self):
        pass


    def test__notify(self, mock_inst_getmy, mock_dep_getmy, mock_auth_ctx):
        # arrange
        with patch.object(DepartmentModel, "get_number_of_schemes_of_work", return_value=0):
            with patch.object(NotifyModel, "create", return_value=None):
                # act
                AuthCtx.check_setup_and_notify(self.mock_db, self.mock_request, mock_auth_ctx)
                # assert
                DepartmentModel.get_number_of_schemes_of_work.assert_called()
                NotifyModel.create.assert_called()
                

    def test__does_not_notify(self, mock_inst_getmy, mock_dep_getmy, mock_auth_ctx):
        # arrange
        with patch.object(DepartmentModel, "get_number_of_schemes_of_work", return_value=1):
            with patch.object(NotifyModel, "create", return_value=None):
                # act
                AuthCtx.check_setup_and_notify(self.mock_db, self.mock_request, mock_auth_ctx)
                # assert
                DepartmentModel.get_number_of_schemes_of_work.assert_called()
                NotifyModel.create.assert_not_called()
    