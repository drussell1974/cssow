from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_type import LOG_TYPE
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_eventlog import EventLogFilter
from shared.models.cls_notification import NotifyModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_notifications(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select_with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")
        
        search_criteria = EventLogFilter([5,10,25,50,100], 2, 100)
        
        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(KeyError):
                NotifyModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)


    def test__should_call_select_return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        search_criteria = EventLogFilter([5,10,25,50,100], 2, 100, date_to = "2121-12-31T00:00:00")
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = NotifyModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_notifications'
                , ("2121-12-31T00:00:00", 1, 100, mock_auth_user.auth_user_id)
                , [])
                
            self.assertEqual(0, len(actual_results))


    def test__should_call_select_return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (1029, "2020-08-23 03:49:56", "2020-08-20 14:34:10", LOG_TYPE.Error, "An error occured doing some stuff", "http://localhost/dosomething/1", "do something about it"),
            ]
        
        search_criteria = EventLogFilter([5,10,25,50,100], 2, 100, date_to = "2021-01-15T00:00:00")

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = NotifyModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_notifications'
                , ("2021-01-15T00:00:00", 1, 100, mock_auth_user.auth_user_id)
                , [])                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(1029, actual_results[0].id)
            self.assertEqual(LOG_TYPE.parse(LOG_TYPE.Error), actual_results[0].event_type)
            self.assertEqual("2020-08-23 03:49:56", actual_results[0].reminder)
            self.assertEqual("2020-08-20 14:34:10", actual_results[0].created)
            self.assertEqual("An error occured doing some stuff", actual_results[0].message)
            self.assertEqual("do something about it", actual_results[0].notify_message)
            self.assertEqual("http://localhost/dosomething/1", actual_results[0].action)


    def test__should_call_select_return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (1021, "2020-07-27 15:48:40", "2020-05-30 00:12:00", LOG_TYPE.Error, "An error occured doing stuff", "http://localhost/dosomething/1", "it needs attention"),
            (1022, "2020-07-27 15:51:08", "2020-07-26 15:12:34", LOG_TYPE.Error, "An error occured doing same thing", "http://localhost/dosomething/2", "action it"),
            (1023, "2020-08-23 03:48:01", "2020-08-23 03:48:00", LOG_TYPE.Warning, "Validation errors", "http://localhost/dosomething/3", "go there")
        ]
        
        search_criteria = EventLogFilter([5,10,25,50,100], 2, 100, date_to = "2021-04-05T00:00:00")
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = NotifyModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_notifications'
                , ("2021-04-05T00:00:00", 1, 100, mock_auth_user.auth_user_id)
                , [])

            self.assertEqual(3, len(actual_results))


            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual(LOG_TYPE.parse(LOG_TYPE.Error), actual_results[0].event_type)
            self.assertEqual("2020-07-27 15:48:40", actual_results[0].reminder)
            self.assertEqual("2020-05-30 00:12:00", actual_results[0].created)
            self.assertEqual("An error occured doing stuff", actual_results[0].message)
            self.assertEqual("it needs attention", actual_results[0].notify_message)
            self.assertEqual("http://localhost/dosomething/1", actual_results[0].action)
            

            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual(LOG_TYPE.parse(LOG_TYPE.Warning), actual_results[2].event_type),
            self.assertEqual("2020-08-23 03:48:01", actual_results[2].reminder),
            self.assertEqual("2020-08-23 03:48:00", actual_results[2].created),
            self.assertEqual("Validation errors", actual_results[2].message)
            self.assertEqual("go there", actual_results[2].notify_message)
            self.assertEqual("http://localhost/dosomething/3", actual_results[2].action)
