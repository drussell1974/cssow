from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.lessons.viewmodels import LessonSaveViewModel as ViewModel
from shared.models.cls_lesson import LessonDataAccess as DataAccess, LessonModel as Model

#Serializer = test_context.KeywordModelSerializer

class test_viewmodel_SaveViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()

        self.mock_model = Mock()
        self.test_context = ViewModel(self.mock_db, self.mock_model, auth_user=99)
        

    def tearDown(self):
        pass


    def test_execute_called_save__add_model_to_data(self):
        
        # arrange
        
        data_to_return = Model(99)
        
        with patch.object(DataAccess, "save", return_value=data_to_return):
            

            # act
            self.test_context.execute(self.mock_model)
            
            # assert functions was called
            DataAccess.save.assert_called()
            self.assertEqual(99, self.test_context.model.id)
