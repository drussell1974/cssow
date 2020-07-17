from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_learningobjective as test_context 

get_all = test_context.get_all
handle_log_info = test_context.handle_log_info


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

            with self.assertRaises(KeyError):
                get_all(self.fake_db, 4, auth_user=99)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_all(self.fake_db, lesson_id=5, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  lob.id as id,  lob.description as description,  solo.id as solo_id,  solo.name as solo_taxonomy_name,  solo.lvl as solo_taxonomy_level,  cnt.id as content_id,  cnt.description as content_description,  sow.key_stage_id as key_stage_id,  ks.name as key_stage_name,  le.id as lesson_id,  le.order_of_delivery_id as lesson_name,  lob.key_words as key_words, lob.notes as notes, lob.group_name as group_name, le_lo.is_key_objective as is_key_objective, lob.created as created,  lob.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name  FROM sow_scheme_of_work as sow  INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id  INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id  INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id  LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id  LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id  LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id  LEFT JOIN auth_user as user ON user.id = lob.created_by  WHERE le.id = 5 AND (le.published = 1 or le.created_by = 1);"
                , [])
                
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(
            934, "Sed at arcu in leo vestibulum dapibus. Suspendisse",
            1, "Prestructural", 1,  34,
            "Nullam dapibus leo vitae imperdiet mollis.",
            4, "KS4",
            12, "Vivamus rutrum viverra lorem",
            "malesuada,sapien,condimentum", "Ut consequat mi purus, ut placerat libero tempus.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user"
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, lesson_id=3, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  lob.id as id,  lob.description as description,  solo.id as solo_id,  solo.name as solo_taxonomy_name,  solo.lvl as solo_taxonomy_level,  cnt.id as content_id,  cnt.description as content_description,  sow.key_stage_id as key_stage_id,  ks.name as key_stage_name,  le.id as lesson_id,  le.order_of_delivery_id as lesson_name,  lob.key_words as key_words, lob.notes as notes, lob.group_name as group_name, le_lo.is_key_objective as is_key_objective, lob.created as created,  lob.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name  FROM sow_scheme_of_work as sow  INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id  INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id  INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id  LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id  LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id  LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id  LEFT JOIN auth_user as user ON user.id = lob.created_by  WHERE le.id = 3 AND (le.published = 1 or le.created_by = 1);"
                , [])
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(934, actual_results[0]["id"])
            self.assertEqual("Sed at arcu in leo vestibulum dapibus. Suspendisse", actual_results[0]["description"])
            self.assertEqual("Prestructural", actual_results[0]["solo_taxonomy_name"])
            self.assertEqual("Nullam dapibus leo vitae imperdiet mollis.", actual_results[0]["content_description"])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(
            934, "Etiam eu efficitur ante. Nunc justo turpis, finibus.",
            1, "Unistructural", 1,  34,
            "Donec mattis sed eros ac eleifend.",
            4, "KS4",
            12, "Morbi volutpat justo quis",
            "ligula,pretium congue,vestibulum", "Sed egestas, ligula eu tempus sollicitudin, lectus velit.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user"
        ),
        (
            935, "Sed at arcu in leo vestibulum dapibus. Suspendisse",
            3, "Multistructural", 1,  34,
            "Nullam dapibus leo vitae imperdiet mollis.",
            4, "KS4",
            12, "Vivamus rutrum viverra lorem",
            "malesuada,sapien,condimentum", "Ut consequat mi purus, ut placerat libero tempus.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user"
        ),
        (
            936, "Sed consectetur nulla ut venenatis dignissim. Sed dictum.",
            4, "Relational", 1,  34,
            "Donec ut condimentum risus.",
            4, "KS4",
            12, " Maecenas tincidunt tempus arcu.",
            "Nulla,molestie,magna purus", "A dapibus enim lobortis.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user"
        )]


        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, lesson_id=20, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                 "SELECT  lob.id as id,  lob.description as description,  solo.id as solo_id,  solo.name as solo_taxonomy_name,  solo.lvl as solo_taxonomy_level,  cnt.id as content_id,  cnt.description as content_description,  sow.key_stage_id as key_stage_id,  ks.name as key_stage_name,  le.id as lesson_id,  le.order_of_delivery_id as lesson_name,  lob.key_words as key_words, lob.notes as notes, lob.group_name as group_name, le_lo.is_key_objective as is_key_objective, lob.created as created,  lob.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name  FROM sow_scheme_of_work as sow  INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id  INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id  INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id  LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id  LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id  LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id  LEFT JOIN auth_user as user ON user.id = lob.created_by  WHERE le.id = 20 AND (le.published = 1 or le.created_by = 1);"
                 , [])

            self.assertEqual(3, len(actual_results))


            self.assertEqual(934, actual_results[0]["id"])
            self.assertEqual("Etiam eu efficitur ante. Nunc justo turpis, finibus.", actual_results[0]["description"])
            self.assertEqual("Unistructural", actual_results[0]["solo_taxonomy_name"])
            self.assertEqual("Donec mattis sed eros ac eleifend.", actual_results[0]["content_description"])

            self.assertEqual(936, actual_results[2]["id"])
            self.assertEqual("Sed consectetur nulla ut venenatis dignissim. Sed dictum.", actual_results[2]["description"])
            self.assertEqual("Relational", actual_results[2]["solo_taxonomy_name"])
            self.assertEqual("Donec ut condimentum risus.", actual_results[2]["content_description"])

