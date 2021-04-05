from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_type import LOG_TYPE
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_eventlog import EventLogModel, EventLogFilter
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
                EventLogModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)


    def test__should_call_select_return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        search_criteria = EventLogFilter([5,10,25,50,100], 2, 100)
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = EventLogModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_notifications'
                , (1, 100, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(actual_results))


    def test__should_call_select_return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (1029, "2020-08-23 03:49:56", LOG_TYPE.Error, "An error occured doing some stuff", "nec arcu nec dolor vehicula ornare non.", "http://localhost/dosomething/1"),
            ]
        
        search_criteria = EventLogFilter([5,10,25,50,100], 2, 100)
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = EventLogModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_notifications'
                , (1, 100, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(1029, actual_results[0].id)
            self.assertEqual(LOG_TYPE.parse(LOG_TYPE.Error), actual_results[0].event_type),
            self.assertEqual("2020-08-23 03:49:56", actual_results[0].created),
            self.assertEqual("An error occured doing some stuff", actual_results[0].message)
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].details)
            self.assertEqual("http://localhost/dosomething/1", actual_results[0].action)


    def test__should_call_select_return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (1021, "2020-07-27 15:48:40", LOG_TYPE.Error, "An error occured doing stuff", "nec arcu nec dolor vehicula ornare non.", "http://localhost/dosomething/1"),
            (1022, "2020-07-27 15:51:08", LOG_TYPE.Error, "An error occured doing same thing", "purus lacus, ut volutpat nibh euismod.", "http://localhost/dosomething/2"),
            (1023, "2020-08-23 03:48:01", LOG_TYPE.Warning, "Validation errors", "rutrum lorem a arcu ultrices, id mollis", "http://localhost/dosomething/3")
        ]
        
        search_criteria = EventLogFilter([5,10,25,50,100], 2, 100)
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = EventLogModel.get_notifications(self.fake_db, search_criteria=search_criteria, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_notifications'
                , (1, 100, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))


            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual(LOG_TYPE.parse(LOG_TYPE.Error), actual_results[0].event_type),
            self.assertEqual("2020-07-27 15:48:40", actual_results[0].created),
            self.assertEqual("An error occured doing stuff", actual_results[0].message)
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].details)
            self.assertEqual("http://localhost/dosomething/1", actual_results[0].action)
            

            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual(LOG_TYPE.parse(LOG_TYPE.Warning), actual_results[2].event_type),
            self.assertEqual("2020-08-23 03:48:01", actual_results[2].created),
            self.assertEqual("Validation errors", actual_results[2].message)
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[2].details)
            self.assertEqual("http://localhost/dosomething/3", actual_results[2].action)
