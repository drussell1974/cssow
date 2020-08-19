from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_schemeofwork import SchemeOfWorkModel, SchemeOfWorkDataAccess

class test_db__get_all(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.close = Mock()
        self.fake_db.cursor = Mock()
        self.fake_db.cursor.close = Mock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=5)
            
            # assert
            ExecHelper.select.assert_called_with(
                self.fake_db,
                'scheme_of_work__get_all'
                , (5, 99)
                , [])
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1, 48)]

        SchemeOfWorkModel.get_number_of_lessons = Mock(return_value=[(66,)])
        SchemeOfWorkModel.get_number_of_learning_objectives = Mock(return_value=[(253,)])
        SchemeOfWorkModel.get_number_of_resources = Mock(return_value=[(20,)])

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            rows = SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=3)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all'
                , (3, 99)
                , [])

            SchemeOfWorkModel.get_number_of_lessons.assert_called()
            SchemeOfWorkModel.get_number_of_learning_objectives.assert_called()
            SchemeOfWorkModel.get_number_of_resources.assert_called()

            self.assertEqual(1, len(rows))
            self.assertEqual(6, rows[0]["id"])
            self.assertEqual("Lorem", rows[0]["name"])
            self.assertEqual("ipsum dolor sit amet.", rows[0]["description"])



    def test__should_call_execSql_return_multiple_item(self):
        # arrange

        expected_result = [
            (6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1, 30),
            (7, "Phasellus", "ultricies orci sed tempus.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1, 20),
            (8, "Nulla", "Tristique pharetra nisi. Sed", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1, 34)]

        SchemeOfWorkModel.get_number_of_lessons = Mock(return_value=[(66,)])
        SchemeOfWorkModel.get_number_of_learning_objectives = Mock(return_value=[(253,)])
        SchemeOfWorkModel.get_number_of_resources = Mock(return_value=[(20,)])

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=3)
            
            # assert

            ExecHelper.select.assert_called_with(
                self.fake_db,
                'scheme_of_work__get_all'
                , (3, 99)
                , [])

            SchemeOfWorkModel.get_number_of_lessons.assert_called()
            SchemeOfWorkModel.get_number_of_learning_objectives.assert_called()
            SchemeOfWorkModel.get_number_of_resources.assert_called()

            self.assertEqual(3, len(rows))

            self.assertEqual(6, rows[0]["id"])
            self.assertEqual("Lorem", rows[0]["name"])
            self.assertEqual("ipsum dolor sit amet.", rows[0]["description"])

            self.assertEqual(8, rows[2]["id"])
            self.assertEqual("Nulla", rows[2]["name"])
            self.assertEqual("Tristique pharetra nisi. Sed", rows[2]["description"])
