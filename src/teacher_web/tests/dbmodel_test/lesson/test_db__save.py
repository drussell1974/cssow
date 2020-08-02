from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess, handle_log_info

save = LessonDataAccess.save

class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, 99)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, "")
    
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model)


    def test_should_call__copy_objective_ids__when_copying(self):
         # arrange
        model = Model(0, "CPU and RAM")
        
        model.is_copy = MagicMock(return_value=True)

        # Mock functions not being tested
        
        LessonDataAccess._upsert_related_topic_ids = MagicMock()
        LessonDataAccess._upsert_pathway_objective_ids = MagicMock()
        LessonDataAccess._upsert_pathway_ks123_ids = MagicMock()
        LessonDataAccess._upsert_key_words = MagicMock()
        LessonDataAccess._copy_objective_ids = Mock()

        expected_result = ([], 341)

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert
            
            LessonDataAccess._copy_objective_ids.assert_called()

            self.assertEqual(341, actual_result.id)


    def test_should_not_call__copy_objective_ids__when_not_copying(self):
         # arrange
        model = Model(0, "CPU and RAM")
        model.is_copy = Mock(return_value=False)

        # Mock functions not being tested
        
        LessonDataAccess._upsert_related_topic_ids = Mock()
        LessonDataAccess._upsert_pathway_objective_ids = Mock()
        LessonDataAccess._upsert_pathway_ks123_ids = Mock()
        LessonDataAccess._upsert_key_words = Mock()
        LessonDataAccess._copy_objective_ids = MagicMock()

        expected_result = ([], 454)

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert
            
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(expected_result[1], actual_result.id)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(1, "CPU and RAM")
        
        # Mock functions not being tested
        LessonDataAccess._upsert_related_topic_ids = Mock()
        LessonDataAccess._upsert_pathway_objective_ids = Mock()
        LessonDataAccess._upsert_pathway_ks123_ids = Mock()
        LessonDataAccess._upsert_key_words = Mock()
        LessonDataAccess._copy_objective_ids = Mock()


        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "UPDATE sow_lesson SET title = 'CPU and RAM', order_of_delivery_id = 1, year_id = 0, scheme_of_work_id = 0, topic_id = 0, summary = '', published = 1 WHERE id =  1;"
                , []
                , log_info=handle_log_info)

            # check subsequent functions where called
            
            LessonDataAccess._upsert_related_topic_ids.assert_called()
            LessonDataAccess._upsert_pathway_objective_ids.assert_called()
            LessonDataAccess._upsert_pathway_ks123_ids.assert_called()
            LessonDataAccess._upsert_key_words.assert_called()
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(expected_result, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, "")

        # mock functions not being tested    
        LessonDataAccess._upsert_related_topic_ids = MagicMock()
        LessonDataAccess._upsert_pathway_objective_ids = MagicMock()
        LessonDataAccess._upsert_pathway_ks123_ids = MagicMock()
        LessonDataAccess._upsert_key_words = MagicMock()
        LessonDataAccess._copy_objective_ids = MagicMock()
        LessonDataAccess._copy_objective_ids.assert_not_called()

        expected_result = ("100", 876)

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "INSERT INTO sow_lesson (title, order_of_delivery_id, year_id, scheme_of_work_id, topic_id, summary, created, created_by, published) VALUES ('', 1, 0, 0, 0, '', '', 0, 1);SELECT LAST_INSERT_ID();"
                , []
                , log_info=handle_log_info)

            # check subsequent functions where called
            
            LessonDataAccess._upsert_related_topic_ids.assert_called()
            LessonDataAccess._upsert_pathway_objective_ids.assert_called()
            LessonDataAccess._upsert_pathway_ks123_ids.assert_called()
            LessonDataAccess._upsert_key_words.assert_called()
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(expected_result[1], actual_result.id)


    def test_should_call_execCRUDSql__delete__when__is_new__false__and__published_is_2(self):
        # arrange

        model = Model(23, "")
        
        # mock functions not being tested    
        LessonDataAccess._upsert_related_topic_ids = MagicMock()
        LessonDataAccess._upsert_pathway_objective_ids = MagicMock()
        LessonDataAccess._upsert_pathway_ks123_ids = MagicMock()
        LessonDataAccess._upsert_key_words = MagicMock()
        LessonDataAccess._copy_objective_ids = MagicMock()

        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99, published=2)

            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "DELETE FROM sow_lesson WHERE id = 23;"
                , []
                , log_info=handle_log_info)

            # check subsequent functions where called
            
            LessonDataAccess._upsert_related_topic_ids.assert_not_called()
            LessonDataAccess._upsert_pathway_objective_ids.assert_not_called()
            LessonDataAccess._upsert_pathway_ks123_ids.assert_not_called()
            LessonDataAccess._upsert_key_words.assert_not_called()
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(expected_result, actual_result.id)
