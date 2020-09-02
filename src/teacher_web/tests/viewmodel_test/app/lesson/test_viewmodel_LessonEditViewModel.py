import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.lessons.viewmodels import LessonEditViewModel as ViewModel
from app.default.viewmodels import KeywordSaveViewModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_keyword import KeywordModel
from shared.serializers.srl_keyword import KeywordModelSerializer


class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_execute_called_save__add_model_to_data(self):
        
        # arrange
        
        on_save__data_to_return = Model(92, "Quisque eu venenatis sem")
        on_save__data_to_return.is_valid = True

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=on_save__data_to_return):

                return_keyword_model = KeywordModel(4, term="Four")
                return_keyword_model.is_valid = True

                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                # act
                mock_model = Model(0, "Proin id massa metus. Aliqua tincidunt.")
                mock_model.scheme_of_work_id = 12
                mock_model.content_id = 10
                mock_model.topic_id = 12
                mock_model.key_stage_id = 2
                mock_model.year_id = 10

                test_context = ViewModel(self.mock_db, mock_model, '[{"id": 4, "term": "Four", "definition": ""}]', auth_user=99)
                test_context.execute(published=1)
                                
                # assert functions was called
                Model.save.assert_called()

                self.assertEqual({}, test_context.model.validation_errors)            
                self.assertEqual(92, test_context.model.id)
                self.assertEqual("Quisque eu venenatis sem", test_context.model.title)
                self.assertEqual([], test_context.model.key_words)
                self.assertEqual({}, test_context.model.validation_errors)            
                self.assertTrue(test_context.model.is_valid)
                

    def test_execute_called_save__add_model_to_data__return_invalid(self):
        
        # arrange
        
        
        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=None):
                
                save_keyword.model = Mock(return_value=KeywordModel(12, scheme_of_work_id=13))

                # act
                mock_model = Model(99, "")                
                mock_model.scheme_of_work_id = 12
                mock_model.content_id = 10
                mock_model.topic_id = 12
                mock_model.key_stage_id = 2
                mock_model.year_id = 10
                
                test_context = ViewModel(self.mock_db, mock_model, key_words_json='[{"id":99,"term":"","definition":""}]', auth_user=99)
                test_context.execute(0)
                                
                # assert save functions was not called
                Model.save.assert_not_called()

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
        mock_model.content_id = 10
        mock_model.topic_id = 101
        mock_model.year_id = 10
        mock_model.key_stage_id = 4

        key_words_json = '[{"id":493,"term":"","definition":""},{"id":32,"term":"DRAM","definition":"The brain of the computer, responsible for executing programs and carrying out arithmetic and logical operations."},{"id":19,"term":"Fetch Decode Execute (FDE)","definition":""}]'
        

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=None):
                
                save_keyword.execute = Mock(return_value=KeywordModel(493,"DRAM",scheme_of_work_id=11))

                # act

                test_context = ViewModel(self.mock_db, mock_model, key_words_json=key_words_json, auth_user=99)
                test_context.execute(0)
                
                # assert save function was NOT called
                Model.save.assert_not_called()
                
                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Quisque eu venenatis sem", test_context.model.title)
                self.assertEqual(3, len(test_context.model.key_words))
                self.assertFalse(test_context.model.is_valid)            
                self.assertEqual({'key_words': "|key_words(id:493):{'term': 'required'}|"}, test_context.model.validation_errors) 


    def test_execute_called_save__add_model_to_data__return_exception_keywords_invalid_format(self):
        
        # arrange
        mock_model = Model(99, "Quisque eu venenatis sem")
        mock_model.scheme_of_work_id = 11
        mock_model.topic_id = 101
        mock_model.year_id = 10
        mock_model.key_stage_id = 4

        key_words_json = '[{id:493,"term":"","definition":""},{"id":32,"term":"DRAM","definition":"The brain of the computer, responsible for executing programs and carrying out arithmetic and logical operations."},{"id":19,"term":"Fetch Decode Execute (FDE)","definition":""}]'
        

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=None):
                
                save_keyword.execute = Mock(return_value=KeywordModel(493,"DRAM"))

                # act
                with self.assertRaises(json.decoder.JSONDecodeError):
                    test_context = ViewModel(self.mock_db, mock_model, key_words_json=key_words_json, auth_user=99)
                    test_context.execute(0)
                    
                    # assert save function was NOT called
                    Model.save.assert_not_called()
                    
                    self.assertEqual(99, test_context.model.id)
                    self.assertEqual("Quisque eu venenatis sem", test_context.model.title)
                    self.assertEqual(3, len(test_context.model.key_words))
                    self.assertFalse(test_context.model.is_valid)            
                    self.assertEqual({'key_words': "|key_words(id:493):{'term': 'required'}|"}, test_context.model.validation_errors) 
