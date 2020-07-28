from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
import shared.models.cls_keyword as test_context

# create test context

Model = test_context.KeywordModel
save = test_context.KeywordDataAccess.save
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

        model = Model(0, term="", definition="Mauris ac velit ultricies, vestibulum.")
        model.is_new = Mock(return_value=True)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, term="", definition="Mauris ac velit ultricies, vestibulum.")
        model.is_new = Mock(return_value=False)
        
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange

        model = Model(1, term="Lorem Ipsum", definition="Mauris ac velit ultricies, vestibulum.")
        model.is_new = MagicMock(return_value=False)
        model.is_valid = MagicMock(return_value=True)

        test_context._update_lesson_lessonobjectives = Mock()

        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "UPDATE sow_key_word SET name = 'Lorem Ipsum', definition = 'Mauris ac velit ultricies, vestibulum.' WHERE id = 1;"
                , log_info=handle_log_info)

            self.assertEqual(expected_result, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, term="Mauris", definition="Mauris ac velit ultricies, vestibulum.")
        
        model.is_new = MagicMock(return_value=True)
        model.is_valid = MagicMock(return_value=True)

        test_context._insert_lesson_lessonobjectives = Mock()
        
        expected_result = ("100")

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)

            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "INSERT INTO sow_key_word (name, definition) VALUES ('Mauris', 'Mauris ac velit ultricies, vestibulum.');"
                , result=[]
                , log_info=handle_log_info)
                
            #self.assertEqual(expected_result, actual_result.id)

