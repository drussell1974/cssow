from unittest import TestCase
from shared.models.cls_department import DepartmentModel as Model, handle_log_info
from shared.models.enums.publlished import STATE
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

#@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_DepartmentDataAccess__get_all(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange

        mock_ctx = fake_ctx_model()
        
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_all(self.fake_db, key_stage_id = 4)
            

    def test__should_call__select__no_items(self):
        # arrange

        mock_ctx = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_all(self.fake_db, 12776111277611, auth_user = mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'department__get_all$2'
                , (12776111277611, int(STATE.PUBLISH_INTERNAL), mock_ctx.auth_user_id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    @patch.object(Model, "get_number_of_schemes_of_work", return_value=3)
    def test__should_call__select__single_items(self, DepartmentModel_get_number_of_schemes_of_work):
        # arrange

        mock_ctx = fake_ctx_model()
        
        expected_result = [(1,"Computer Science", 3, 12776111277611, "Finibus Bonorum", "2020-07-21 17:09:34", 1, "test_user", 0)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_all(self.fake_db, 12776111277611, auth_user = mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'department__get_all$2'
                , (12776111277611, int(STATE.PUBLISH_INTERNAL), mock_ctx.auth_user_id,)
                , []
                , handle_log_info)

            DepartmentModel_get_number_of_schemes_of_work.assert_called_with(self.fake_db, 1, mock_ctx)

            self.assertEqual(1, len(rows))
            self.assertEqual("Computer Science", rows[0].name)
            self.assertEqual("Finibus Bonorum", rows[0].institute.name)
            self.assertEqual(3, rows[0].topic_id)
            

    @patch.object(Model, "get_number_of_schemes_of_work", return_value=10)
    def test__should_call__select__multiple_items(self, DepartmentModel_get_number_of_schemes_of_work):
        # arrange

        mock_ctx = fake_ctx_model()

        expected_result = [
            (1,"Computer Science", 3, 12776111277611, "Finibus Bonorum", "2020-07-21 17:09:34", 1, "test_user", 0),
            (2, "Business", 2, 12776111277611, "Finibus Bonorum", "2020-07-21 17:09:34", 1, "test_user", 0), 
            (3, "IT", 1, 12776111277611, "Lorem Ipsum", "2020-07-21 17:09:34", 1, "test_user", 0)
        ]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_all(self.fake_db, 12776111277611, auth_user = mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'department__get_all$2'
                , (12776111277611, int(STATE.PUBLISH_INTERNAL), mock_ctx.auth_user_id,)
                , []
                , handle_log_info)

            DepartmentModel_get_number_of_schemes_of_work.assert_called_with(self.fake_db, 3, mock_ctx)
            
            self.assertEqual(3, len(rows))
            self.assertEqual("Computer Science", rows[0].name)
            self.assertEqual("Finibus Bonorum", rows[0].institute.name)
            self.assertEqual(3, rows[0].topic_id)

            self.assertEqual("IT", rows[len(rows)-1].name)
            self.assertEqual("Lorem Ipsum", rows[len(rows)-1].institute.name)
            self.assertEqual(1, rows[len(rows)-1].topic_id)
