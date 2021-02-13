from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_institute__deleteunpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        InstituteModel(0, "")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                InstituteModel.delete_unpublished(self.fake_db, mock_ctx)


    def test_should_call__delete(self, mock_ctx):
         # arrange

        with patch.object(ExecHelper, 'delete', return_value=(5)):
            # act

            actual_result = InstituteModel.delete_unpublished(self.fake_db, auth_user=mock_ctx)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db,
                'institute__delete_unpublished'
                , (0, mock_ctx.id)
                , handle_log_info)

            self.assertEqual(5, actual_result)
