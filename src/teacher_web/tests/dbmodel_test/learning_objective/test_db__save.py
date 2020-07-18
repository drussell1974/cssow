from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
import shared.models.cls_learningobjective as test_context

# create test context

Model = test_context.LearningObjectiveModel
save = test_context.save
handle_log_info = test_context.handle_log_info


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

        model = Model(1, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(1, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        model.is_new = MagicMock(return_value=False)
        model.is_valid = MagicMock(return_value=True)

        test_context._update_lesson_lessonobjectives = Mock()

        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "UPDATE sow_learning_objective SET description = 'Mauris ac velit ultricies, vestibulum.', group_name = '', notes = '', key_words = '', solo_taxonomy_id = 1, content_id = NULL, parent_id = NULL, published = 1 WHERE id = 1;"
                , log_info=handle_log_info)

            test_context._update_lesson_lessonobjectives.assert_called()

            self.assertEqual(expected_result, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        model.is_new = MagicMock(return_value=True)
        model.is_valid = MagicMock(return_value=True)

        test_context._insert_lesson_lessonobjectives = Mock()
        
        expected_result = ("100",23)

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)

            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "INSERT INTO sow_learning_objective (description, group_name, notes, key_words, solo_taxonomy_id, content_id, parent_id, created, created_by, published) VALUES ('Mauris ac velit ultricies, vestibulum.', '', '', '', 1, NULL, NULL, '', 0, 1);SELECT LAST_INSERT_ID();"
                , result=[]
                , log_info=handle_log_info)
                
            self.assertEqual(23, actual_result.id)
