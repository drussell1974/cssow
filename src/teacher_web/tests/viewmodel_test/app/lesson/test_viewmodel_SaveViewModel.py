from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.lessons.viewmodels import LessonSaveViewModel as ViewModel
from app.default.viewmodels import KeywordSaveViewModel
from shared.models.cls_lesson import LessonDataAccess as DataAccess, LessonModel as Model
from shared.models.cls_keyword import KeywordModel

#Serializer = test_context.KeywordModelSerializer

class test_viewmodel_SaveViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass

    @skip("Ensure correct mock keyword array is being returned")
    def test_execute_called_save__add_model_to_data(self):
        
        # arrange
        
        on_save__data_to_return = Model(99, "Quisque eu venenatis sem")
        

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(DataAccess, "save", return_value=on_save__data_to_return):

                return_keyword_model = KeywordModel(4, term="Four")
                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                # act
                mock_model = Model(0, "Proin id massa metus. Aliqua tincidunt.")
                mock_model.key_words = "12,13,14"
                mock_model.scheme_of_work_id = 12
                mock_model.topic_id = 12
                mock_model.key_stage_id = 2
                mock_model.year_id = 10

                test_context = ViewModel(self.mock_db, mock_model, key_words_json="", auth_user=99)
                test_context.execute()
                                
                # assert functions was called
                #DataAccess.save.assert_called()

                self.assertEqual("", test_context.model.validation_errors)            
                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Integer convallis erat maximus bibendum", test_context.model.title)
                self.assertEqual([], test_context.model.key_words)
                self.assertTrue(test_context.model.is_valid)            
                self.assertEqual("", test_context.model.validation_errors)            


    def test_execute_called_save__add_model_to_data__return_invalid(self):
        
        # arrange
        
        
        # TODO: Mock KeywordSaveViewModel to return keyword array
        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(DataAccess, "save", return_value=None):
                
                save_keyword.model = Mock(return_value=KeywordModel(12))

                # act
                mock_model = Model(99, "")                
                mock_model.scheme_of_work_id = 12
                mock_model.topic_id = 12
                mock_model.key_stage_id = 2
                mock_model.year_id = 10
                
                test_context = ViewModel(self.mock_db, mock_model, key_words_json='[{"id":99,"term":"","definition":""}]', auth_user=99)
                test_context.execute(0)
                                
                # assert save functions was not called
                DataAccess.save.assert_not_called()

                self.assertEqual(99, test_context.model.id)
                self.assertEqual("", test_context.model.title)
                self.assertEqual(1, len(test_context.model.key_words))
                self.assertFalse(test_context.model.is_valid)            
                self.assertEqual(1, len(test_context.model.validation_errors)) 
                self.assertEqual({'title': 'required'}, test_context.model.validation_errors) 
              

    def test_execute_called_save__add_model_to_data__return_invalid__with_keywords_invalid(self):
        
        # arrange
        mock_model = Model(99, "Quisque eu venenatis sem")
        mock_model.scheme_of_work_id = 11
        mock_model.topic_id = 101
        mock_model.year_id = 10
        mock_model.key_stage_id = 4

        key_words_json = '[{"id":493,"term":"","definition":""},{"id":32,"term":"DRAM","definition":"The brain of the computer, responsible for executing programs and carrying out arithmetic and logical operations."},{"id":19,"term":"Fetch Decode Execute (FDE)","definition":""}]'
        

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(DataAccess, "save", return_value=None):
                
                save_keyword.execute = Mock(return_value=KeywordModel(493,"DRAM"))

                # act

                test_context = ViewModel(self.mock_db, mock_model, key_words_json=key_words_json, auth_user=99)
                test_context.execute(0)
                
                # assert save function was NOT called
                DataAccess.save.assert_not_called()
                
                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Quisque eu venenatis sem", test_context.model.title)
                self.assertEqual(3, len(test_context.model.key_words))
                self.assertFalse(test_context.model.is_valid)            
                self.assertEqual({'key_words': "|key_words(id:493):{'term': 'required'}|"}, test_context.model.validation_errors) 
