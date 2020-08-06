from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.schemesofwork.viewmodels import SchemeOfWorkEditViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model

#Serializer = test_context.KeywordModelSerializer

class test_viewmodel_SaveViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_execute_called_save__add_model_to_data(self):
        
        # arrange

        mock_model = Model(0, name="Proin id massa metus. Aliqua tincidunt.")
        mock_model.description = "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur"
        mock_model.exam_board_id = 56
        mock_model.key_stage_id = 5
        mock_model.lesson_id = 230

        on_save__data_to_return = Model(99, "Proin id massa metus. Aliqua tincidunt.")
        
        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=1)
                            
            # assert functions was called
            
            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.name)


    def test_execute_called_save__add_model_to_data__return_invalid(self):
         
        # arrange

        mock_model = Model(99, name="Suspendisse nisi dui, lobortis ut")
        mock_model.key_stage_id = 3
        mock_model.lesson_id = 0 # invalid value
        mock_model.description = "unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo."

        with patch.object(Model, "save", return_value=None):
                
            # act
            
            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(1)
                            
            # assert save functions was not called
            Model.save.assert_not_called()

            # return the invalid object
            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Suspendisse nisi dui, lobortis ut", test_context.model.name)
            self.assertEqual(0, test_context.model.lesson_id)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual(1, len(test_context.model.validation_errors)) 
            self.assertEqual({'exam_board_id': '0 is not a valid range'}, test_context.model.validation_errors) 
