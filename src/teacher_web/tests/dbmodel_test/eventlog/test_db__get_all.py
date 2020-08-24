from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.core.log_type import LOG_TYPE
from shared.models.cls_eventlog import EventLogModel, EventLogFilter

get_all = EventLogModel.get_all

class test_db__get_all(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_all(self.fake_db)


    def test__should_call_select_return_no_items(self):
        # arrange
        expected_result = []

        search_criteria = EventLogFilter(date_from="", date_to="")

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_all(self.fake_db, search_criteria, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_all'
                , ("", "", 1, 6079)
                , [])
                
            self.assertEqual(0, len(rows))


    def test__should_call_select_return_single_item(self):
        # arrange
        expected_result = [
            (1029, "2020-08-23 03:49:56", LOG_TYPE.Error, "An error occured doing some stuff", "nec arcu nec dolor vehicula ornare non.", "A", "B"),
            ]

        search_criteria = EventLogFilter(date_from="", date_to="", event_type=2)

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, search_criteria,  auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_all'
                , ("", "", 2, 6079)
                , [])                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(1029, actual_results[0].id)
            self.assertEqual(LOG_TYPE.Error, actual_results[0].event_type),
            self.assertEqual("2020-08-23 03:49:56", actual_results[0].created),
            self.assertEqual("An error occured doing some stuff", actual_results[0].message)
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].details)
            self.assertEqual("A", actual_results[0].category)
            self.assertEqual("B", actual_results[0].subcategory)



    def test__should_call_select_return_multiple_item(self):
        # arrange
        expected_result = [
            (1021, "2020-07-27 15:48:40", LOG_TYPE.Error, "An error occured doing stuff", "nec arcu nec dolor vehicula ornare non.", "X", "Y"),
            (1022, "2020-07-27 15:51:08", LOG_TYPE.Error, "An error occured doing same thing", "purus lacus, ut volutpat nibh euismod.", "Y", "Z"),
            (1023, "2020-08-23 03:48:01", LOG_TYPE.Warning, "Validation errors", "rutrum lorem a arcu ultrices, id mollis", "Z", "A")
        ]

        search_criteria = EventLogFilter(date_from="", date_to="", event_type=1)

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, search_criteria, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'logging__get_all'
                , ("", "", 1, 6079)
                , [])

            self.assertEqual(3, len(actual_results))


            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual(LOG_TYPE.Error, actual_results[0].event_type),
            self.assertEqual("2020-07-27 15:48:40", actual_results[0].created),
            self.assertEqual("An error occured doing stuff", actual_results[0].message)
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].details)
            self.assertEqual("X", actual_results[0].category)
            self.assertEqual("Y", actual_results[0].subcategory)
            

            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual(LOG_TYPE.Warning, actual_results[2].event_type),
            self.assertEqual("2020-08-23 03:48:01", actual_results[2].created),
            self.assertEqual("Validation errors", actual_results[2].message)
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[2].details)
            self.assertEqual("Z", actual_results[2].category)
            self.assertEqual("A", actual_results[2].subcategory)
