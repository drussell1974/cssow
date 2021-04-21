from datetime import datetime
from unittest import TestCase, skip
from shared.models.cls_topic import TopicModel, handle_log_info
from shared.models.enums.publlished import STATE
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
        expected_result = KeyError('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(KeyError):
                TopicModel.get_options(self.fake_db, lvl = 1, auth_ctx=mock_auth_user)


    def test__should_call__select__return_no_items(self, mock_auth_user):
        # arrange

        expected_result = []
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = TopicModel.get_options(self.fake_db, lvl = 2, auth_ctx=mock_auth_user, topic_id = 1)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'topic__get_options$2'
                , (1, mock_auth_user.department_id, 2, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call__select__return_single_items(self, mock_auth_user):
        # arrange

        expected_result = [(2,"Operators", 2, datetime(2021, 4, 20), 2, 2, 1,"Algorithms", 1, datetime(2021, 4, 20), 2, 2)]

        with patch.object(ExecHelper, 'select',  return_value=expected_result):
            
            # act
            rows = TopicModel.get_options(self.fake_db, lvl = 2, topic_id = 2, auth_ctx=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'topic__get_options$2'
                , (2, mock_auth_user.department_id, 2, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(1, len(rows))
            self.assertEqual("Operators", rows[0]["name"])
            #self.assertEqual(13, rows[0]["department_id"])
        


    def test__should_call__select__return_multiple_items(self, mock_auth_user):
        # arrange
        
        expected_result = [
            (3, "Binary", 2, datetime(2021, 4, 20), 2, 1, 1, "Algorithms", 1, datetime(2021, 4, 20), 2, 2),
            (4, "Operators", 2, datetime(2021, 4, 20), 2,  1, 1, "Algorithms", 1, datetime(2021, 4, 20), 2, 2),
            (5, "Data compression", 2, datetime(2021, 4, 20), 2, 1, 1, "Algorithms", 1, datetime(2021, 4, 20), 2, 2)]

        with patch.object(ExecHelper, 'select',  return_value=expected_result):
            
            # act
            
            rows = TopicModel.get_options(self.fake_db, lvl = 2, topic_id = 3, auth_ctx=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'topic__get_options$2'
                , (3, mock_auth_user.department_id, 2, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(3, len(rows))
        
            self.assertEqual("Binary", rows[0]["name"])
        
            self.assertEqual("Data compression", rows[len(rows)-1]["name"])
        