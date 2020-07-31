from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lesson import LessonDataAccess as test_context, KeywordModel, handle_log_info
from shared.models.cls_learningobjective import LearningObjectiveDataAccess
from shared.models.cls_resource import ResourceDataAccess
# test context

get_model = test_context.get_model
#handle_log_info = shared.models.cls_lesson.handle_log_info


class test_db__get_model(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

        test_context.get_all_keywords = Mock(return_value=[
            KeywordModel(32, 'Central Processing Unit (CPU)', ''),
            KeywordModel(17, 'Control Unit (CU)', ''),
            KeywordModel(7, 'Registers', '')
        ])

        LearningObjectiveDataAccess.get_all = Mock(return_value=[1,2,3])
        ResourceDataAccess.get_all = Mock(return_value=[])
        test_context.get_pathway_objective_ids = Mock(return_value=[])
        test_context.get_ks123_pathway_objective_ids = Mock(return_value=[])


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_model(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
         
            actual_results = get_model(self.fake_db, 99, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  le.id as id, le.title as title, le.order_of_delivery_id as order_of_delivery_id, le.scheme_of_work_id as scheme_of_work_id, sow.name as scheme_of_work_name, top.id as topic_id, top.name as topic_name, pnt_top.id as parent_topic_id, pnt_top.name as parent_topic_name, sow.key_stage_id as key_stage_id, yr.id as year_id, le.summary as summary, le.created as created, le.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_lesson as le INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id INNER JOIN sow_year as yr ON yr.id = le.year_id INNER JOIN sow_topic as top ON top.id = le.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN auth_user as user ON user.id = sow.created_by WHERE le.id = 99 AND (le.published = 1 OR le.created_by = 1);"
                , [])


            self.assertEqual(99, actual_results.id)
            self.assertEqual("", actual_results.title),
            self.assertEqual(0, actual_results.topic_id),
            self.assertEqual("", actual_results.topic_name),
            self.assertEqual(0, actual_results.parent_topic_id),
            self.assertEqual("", actual_results.parent_topic_name),
            self.assertEqual("", actual_results.summary)
            self.assertEqual([], actual_results.key_words)



    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(
            321,"Understanding numbering systems",1,5,"Computer Science",
            2,"Denary",3,"Data representation",38,11,"Understand common numbering systems","2020-07-16 01:04:59",
            1,"test_user",0,{32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'},4,"learning_objectives",23,343
        )]
        

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 321, auth_user=99)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  le.id as id, le.title as title, le.order_of_delivery_id as order_of_delivery_id, le.scheme_of_work_id as scheme_of_work_id, sow.name as scheme_of_work_name, top.id as topic_id, top.name as topic_name, pnt_top.id as parent_topic_id, pnt_top.name as parent_topic_name, sow.key_stage_id as key_stage_id, yr.id as year_id, le.summary as summary, le.created as created, le.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_lesson as le INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id INNER JOIN sow_year as yr ON yr.id = le.year_id INNER JOIN sow_topic as top ON top.id = le.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN auth_user as user ON user.id = sow.created_by WHERE le.id = 321 AND (le.published = 1 OR le.created_by = 99);"
                , [])
            
            test_context.get_all_keywords.assert_called_with(self.fake_db, lesson_id=321)
            self.assertEqual(3, len(actual_results.key_words))

            self.assertEqual(321, actual_results.id)
            self.assertEqual("Understanding numbering systems", actual_results.title),
            self.assertEqual(2, actual_results.topic_id),
            self.assertEqual("Denary", actual_results.topic_name),
            self.assertEqual(3, actual_results.parent_topic_id),
            self.assertEqual("Data representation", actual_results.parent_topic_name),
            self.assertEqual("Understand common numbering systems", actual_results.summary)

            self.assertNotIsInstance(actual_results, dict, "remove __dict__ from actual_results")

            #self.assertEqual("", actual_results) #test_context.get_all_objectives = Mock(return_value=[1,2,3])
            #test_context.get_all_objectives.assert_called()
            #self.assertEqual("", actual_results) #test_context.get_all_resources = Mock(return_value=[])
            #test_context.get_all_resources.assert_called()
            #self.assertEqual("", actual_results) #test_context.get_pathway_objective_ids = Mock(return_value=[])
            #test_context.get_pathway_objective_ids.assert_called()
            #self.assertEqual("", actual_results) #test_context.get_ks123_pathway_objective_ids = Mock(return_value=[])




