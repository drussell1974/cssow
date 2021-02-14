from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from tests.test_helpers.mocks import fake_ctx_model

class test_db_institute__deleteunpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        InstituteModel(0, "")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                InstituteModel.delete_unpublished(self.fake_db, fake_ctx_model())


    def test_should_call__delete(self):
         # arrange

        with patch.object(ExecHelper, 'delete', return_value=(5)):
            # act

            actual_result = InstituteModel.delete_unpublished(self.fake_db, auth_user=fake_ctx_model())
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db,
                'institute__delete_unpublished'
                , (0, 6079)
                , handle_log_info)

            self.assertEqual(5, actual_result)
