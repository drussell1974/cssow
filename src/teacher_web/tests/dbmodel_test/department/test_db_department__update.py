from unittest import TestCase
from shared.models.cls_department import DepartmentModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_DepartmentDataAccess___update(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__save__with_exception(self, mock_ctx):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "insert", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.save(self.fake_db, 99, "Lorum ipsum", auth_user = mock_ctx)
            

    def test__should_call__save__if_valid(self, mock_ctx):
        # arrange
        expected_result = [101]

        fake_model = Model(101, "Lorum ipsum", institute = InstituteModel(12767111276711, "Lorum ipsum"))
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = True

        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = mock_ctx)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db,
                'department__update'
                , (101, 'Lorum ipsum', 12767111276711, 1, mock_ctx.auth_user_id)
                , handle_log_info)

            self.assertEqual(101, result.id)


    def test__should_not_call__save__if_not_valid(self, mock_ctx):
        # arrange
        expected_result = [99]

        fake_model = Model(99, "Lorum ipsum", institute = InstituteModel(12767111276711, "Lorum ipsum"))
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = False

        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = mock_ctx)
            
            # assert

            ExecHelper.update.not_called()

            self.assertEqual(99, result.id)
            self.assertFalse(result.is_valid)
