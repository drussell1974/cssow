from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_learningobjective as test_context 

get_all_pathway_objectives = test_context.LearningObjectiveModel.get_all_pathway_objectives
handle_log_info = test_context.handle_log_info


class test_db__get_all_pathway_objectives(TestCase):


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
                get_all_pathway_objectives(self.fake_db, key_stage_id=4, key_words="")


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_all_pathway_objectives(self.fake_db, key_stage_id=5, key_words="")
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob LEFT JOIN sow_topic as top ON top.id = lob.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE ks.id < 5 ORDER BY ks.name DESC, solo.lvl;"
                , [])
                
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        
        expected_result = [(
            934, # 0 
            "Sed at arcu in leo vestibulum dapibus. Suspendisse", # 1
            1, # 2
            "Prestructural", # 3
            34, # 4
            23, # 5
            "Nullam dapibus leo vitae imperdiet mollis.", # 6
            4, # 7
            "KS4", # 8 
            "CPU,RAM,DDR,DIMM", # 9
            "Vivamus rutrum viverra lorem", # 10
            "2020-07-17 16:24:04", # 11
            99, # 12
            "test_user" # 13
        )]
    
        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all_pathway_objectives(self.fake_db, key_stage_id=3, key_words="CPU")
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob LEFT JOIN sow_topic as top ON top.id = lob.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE ks.id < 3 ORDER BY ks.name DESC, solo.lvl;"
                , [])
                
            self.assertEqual(1, len(actual_results))

            self.assertEqual(934, actual_results[0]["id"])
            self.assertEqual("Sed at arcu in leo vestibulum dapibus. Suspendisse", actual_results[0]["description"])
            self.assertEqual("Prestructural", actual_results[0]["solo_taxonomy_name"])
            self.assertEqual("Nullam dapibus leo vitae imperdiet mollis.", actual_results[0]["content_description"])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange

        expected_result = [(
            934, # 0
            "Etiam eu efficitur ante. Nunc justo turpis, finibus.", # 1
            1, # 2
            "Unistructural", # 3 
            1, # 4
            34, # 5
            "Donec mattis sed eros ac eleifend.", # 6
            4, # 7
            "KS4", # 8
            "ligula,pretium congue,vestibulum", # 9
            "", # 10
            "2020-07-17 16:24:04", # 11
            99, # 12
            "test_user" # 13
        ),
        (
            935, "Sed at arcu in leo vestibulum dapibus. Suspendisse",
            3, "Multistructural", 1,  34,
            "Nullam dapibus leo vitae imperdiet mollis.",
            4, "KS4",
            "malesuada,sapien,condimentum",
            "",
            "2020-07-17 16:24:04", 99, "test_user"
        ),
        (
            936, "Sed consectetur nulla ut venenatis dignissim. Sed dictum.",
            4, "Relational", 1,  34,
            "Donec ut condimentum risus.",
            4, "KS4",
            "Nulla,molestie,magna purus, congue, dapibus enim lobortis",
            "",
            "2020-07-17 16:24:04", 99, "test_user"
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all_pathway_objectives(self.fake_db, key_stage_id=20, key_words="congue")
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                 "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob LEFT JOIN sow_topic as top ON top.id = lob.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE ks.id < 20 ORDER BY ks.name DESC, solo.lvl;"
                 , [])


            # found 2 or 3
            
            self.assertEqual(2, len(actual_results)) 


            self.assertEqual(934, actual_results[0]["id"])
            self.assertEqual("Etiam eu efficitur ante. Nunc justo turpis, finibus.", actual_results[0]["description"])
            self.assertEqual("Unistructural", actual_results[0]["solo_taxonomy_name"])
            self.assertEqual("Donec mattis sed eros ac eleifend.", actual_results[0]["content_description"])

            self.assertEqual(936, actual_results[1]["id"])
            self.assertEqual("Sed consectetur nulla ut venenatis dignissim. Sed dictum.", actual_results[1]["description"])
            self.assertEqual("Relational", actual_results[1]["solo_taxonomy_name"])
            self.assertEqual("Donec ut condimentum risus.", actual_results[1]["content_description"])

