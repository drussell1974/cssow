from datetime import datetime
from django.conf import settings
from unittest import TestCase, skip
from shared.models.cls_topic import TopicModel, handle_log_info
from shared.models.enums.publlished import STATE
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import fake_teacher_permission_model

@patch("shared.models.cls_teacher_permission.TeacherPermissionModel", return_value=fake_teacher_permission_model())
class test_db_topic__get_all__level_1(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = Mock()
        self.fake_db.connect()
        

    def tearDown(self):
        self.fake_db.close()

    
    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange
        expected_result = KeyError('Bang')

        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(KeyError):
                TopicModel.get_all(self.fake_db, auth_ctx=mock_auth_user)


    def test__should_call__select__return_no_items(self, mock_auth_user):
        # arrange

        expected_result = []
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = TopicModel.get_all(self.fake_db, auth_ctx=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'topic__get_all'
                , (mock_auth_user.department_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call__select__return_single_items(self, mock_auth_user):
        # arrange

        expected_result = [        
            (1, 'Algorithms', 1, datetime(2021, 2, 27, 15, 26), 0, 1, 0, 'Computing', 0, datetime(2021, 2, 27, 15, 26), 2)
        ]

        with patch.object(ExecHelper, 'select',  return_value=expected_result):
            
            # act
            rows = TopicModel.get_all(self.fake_db, auth_ctx=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'topic__get_all'
                , (mock_auth_user.department_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(1, len(rows))
            self.assertEqual("Algorithms", rows[0].name)
            self.assertEqual(1, rows[0].lvl)
            self.assertEqual(1, rows[0].published)
            self.assertEqual("Computing", rows[0].parent.name)
            self.assertEqual(0, rows[0].parent.lvl)
            self.assertEqual(1, rows[0].parent.published)
        

    def test__should_call__select__return_multiple_items(self, mock_auth_user):
        # arrange
        
        expected_result = [
            (38, 'Data Types', 2, datetime(2021, 2, 27, 15, 26), 2, 1, 1, 'Algorithms', 1, datetime(2021, 2, 27, 15, 26), 2),
            (40, 'Logic gates', 2, datetime(2021, 2, 27, 15, 26), 2, 1, 1, 'Algorithms', 1, datetime(2021, 2, 27, 15, 26), 1),
            (35, 'Problem solving', 2, datetime(2021, 2, 27, 15, 26), 2, 1, '1', 'Algorithms', 1, datetime(2021, 2, 27, 15, 26), 1),
        ]

        with patch.object(ExecHelper, 'select',  return_value=expected_result):
            
            # act
            
            rows = TopicModel.get_all(self.fake_db, auth_ctx=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'topic__get_all'
                , (mock_auth_user.department_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(3, len(rows))
            
            self.assertEqual(38, rows[0].id)
            self.assertEqual("Data Types", rows[0].name)
            self.assertEqual(2, rows[0].lvl)
            self.assertEqual(1, rows[0].published)
            self.assertEqual("Algorithms", rows[0].parent.name)
            self.assertEqual(1, rows[0].parent.lvl)
            self.assertEqual(1, rows[0].parent.published)
        
            i = len(rows)-1
            self.assertEqual(35, rows[i].id)
            self.assertEqual("Problem solving", rows[i].name)
            self.assertEqual(2, rows[i].lvl)
            self.assertEqual(1, rows[i].published)
            self.assertEqual("Algorithms", rows[i].parent.name)
            self.assertEqual(1, rows[i].parent.lvl)
            self.assertEqual(1, rows[i].parent.published)
        