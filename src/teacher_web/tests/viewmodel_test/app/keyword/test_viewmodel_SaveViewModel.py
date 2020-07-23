from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.default.viewmodels import KeywordSaveViewModel as ViewModel
from shared.models.cls_keyword import KeywordDataAccess as DataAccess, KeywordModel as Model
from shared.models.cls_lesson import LessonModel

#Serializer = test_context.KeywordModelSerializer

class test_viewmodel_SaveViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()

        self.mock_model = Mock()
        self.test_context = ViewModel(self.mock_db)
        

    def tearDown(self):
        pass


    def test_execute_called_save__with_exception(self):
        
        # arrange
                
        with patch.object(DataAccess, "save", side_effect=KeyError):
    
            with self.assertRaises(KeyError):
                # act
                self.test_context.execute(self.mock_model, 99)


    def test_execute_called_save__add_model_to_data(self):
        
        # arrange
        
        data_to_return = LessonModel(99)
        
        with patch.object(DataAccess, "save", return_value=data_to_return):
            

            # act
            self.test_context.execute(self.mock_model, 99)
            
            # assert functions was called
            DataAccess.save.assert_called()
            self.assertEqual(99, self.test_context.model.id)


    @skip("NOT TESTED")
    def test_execute_called_save__add_model_to_data__when_exisiting_item(self):
        self.fail("not tested - pass key_words with array of int")


    @skip("NOT TESTED")
    def test_execute_called_save__add_model_to_data__when_not_exists(self):
        self.fail("not tested - pass string with array of string and int")


    @skip("NOT TESTED")
    def test_execute_called_save__add_model_to_data__when_not_valid(self):
        self.fail("not tested - pass string empty term and raise exception")