from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_schemeofwork import SchemeOfWorkModel

class test_db__get_all(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=5)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,"SELECT   sow.id as id,   sow.name as name,   sow.description as description,   sow.exam_board_id as exam_board_id,   exam.name as exam_board_name,   sow.key_stage_id as key_stage_id,   kys.name as key_stage_name,   sow.created as created,   sow.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,   sow.published as published FROM sow_scheme_of_work as sow   LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id   INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id   LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE (sow.key_stage_id = 5 or 5 = 0) AND (sow.published = 1 OR sow.created_by = 99) ORDER BY sow.key_stage_id;", [])
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1)]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=3)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,"SELECT   sow.id as id,   sow.name as name,   sow.description as description,   sow.exam_board_id as exam_board_id,   exam.name as exam_board_name,   sow.key_stage_id as key_stage_id,   kys.name as key_stage_name,   sow.created as created,   sow.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,   sow.published as published FROM sow_scheme_of_work as sow   LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id   INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id   LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE (sow.key_stage_id = 3 or 3 = 0) AND (sow.published = 1 OR sow.created_by = 99) ORDER BY sow.key_stage_id;", [])
            self.assertEqual(1, len(rows))
            self.assertEqual(6, rows[0]["id"])
            self.assertEqual("Lorem", rows[0]["name"])
            self.assertEqual("ipsum dolor sit amet.", rows[0]["description"])



    def test__should_call_execSql_return_multiple_item(self):
        # arrange

        expected_result = [
            (6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1),
            (7, "Phasellus", "ultricies orci sed tempus.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1),
            (8, "Nulla", "Tristique pharetra nisi. Sed", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1)]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=3)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,"SELECT   sow.id as id,   sow.name as name,   sow.description as description,   sow.exam_board_id as exam_board_id,   exam.name as exam_board_name,   sow.key_stage_id as key_stage_id,   kys.name as key_stage_name,   sow.created as created,   sow.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,   sow.published as published FROM sow_scheme_of_work as sow   LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id   INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id   LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE (sow.key_stage_id = 3 or 3 = 0) AND (sow.published = 1 OR sow.created_by = 99) ORDER BY sow.key_stage_id;", [])
            self.assertEqual(3, len(rows))

            self.assertEqual(6, rows[0]["id"])
            self.assertEqual("Lorem", rows[0]["name"])
            self.assertEqual("ipsum dolor sit amet.", rows[0]["description"])

            self.assertEqual(8, rows[2]["id"])
            self.assertEqual("Nulla", rows[2]["name"])
            self.assertEqual("Tristique pharetra nisi. Sed", rows[2]["description"])
