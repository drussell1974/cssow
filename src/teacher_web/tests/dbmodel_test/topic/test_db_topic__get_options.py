from unittest import TestCase, skip
from shared.models.cls_topic import TopicModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import fake_teacher_permission_model

@patch("shared.models.cls_teacher_permission.TeacherPermissionModel", return_value=fake_teacher_permission_model())
class test_db_topic__get_options__level_1(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = Mock()
        self.fake_db.connect()
        handle_log_info = MagicMock()


    def tearDown(self):
        self.fake_db.close()

    
    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                TopicModel.get_options(self.fake_db, lvl = 1)


    def test__should_call__select__return_no_items(self, mock_auth_user):
        # arrange

        expected_result = []
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = Model.get_options(self.fake_db, lvl = 2, auth_user=mock_auth_user, topic_id = 1)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'topic__get_options'
                , (1, 2, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call__select__return_single_items(self, mock_auth_user):
        # arrange

        expected_result = [(1,"Operators","X","X")]

        with patch.object(ExecHelper, 'select',  return_value=expected_result):
            
            # act
            rows = Model.get_options(self.fake_db, lvl = 2, auth_user=mock_auth_user, topic_id = 2)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'topic__get_options'
                , (2, 2, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(1, len(rows))
            self.assertEqual("Operators", rows[0]["name"], "First item not as expected")
        


    def test__should_call__select__return_multiple_items(self, mock_auth_user):
        # arrange
        
        expected_result = [(1,"Binary","X","X"),(2,"Operators","X","X"),(3,"Data compression","X","X")]

        with patch.object(ExecHelper, 'select',  return_value=expected_result):
            
            # act
            
            rows = Model.get_options(self.fake_db, lvl = 2, topic_id = 3, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'topic__get_options'
                , (3, 2, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(3, len(rows))
            self.assertEqual("Binary", rows[0]["name"], "First item not as expected")
            self.assertEqual("Data compression", rows[len(rows)-1]["name"], "Last item not as expected")
