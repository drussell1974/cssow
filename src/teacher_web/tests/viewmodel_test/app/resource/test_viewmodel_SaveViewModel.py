from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.resources.viewmodels import ResourceSaveViewModel as ViewModel
from shared.models.cls_resource import ResourceModel as Model
from shared.models.enums.publlished import STATE

class test_viewmodel_SaveViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    
    def test_execute_called_save__add_model_to_data(self):
        
        # arrange

        mock_model = Model(0, title="Proin id massa metus. Aliqua tincidunt.")
        mock_model.type_id = 1
        mock_model.publisher = "Penguin"
        mock_model.page_note = "Curabitur id augue vel dui."

        on_save__data_to_return = Model(99, title="Proin id massa metus. Aliqua tincidunt.")
        
        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(db=self.mock_db, scheme_of_work_id=99, lesson_id=13, model=mock_model, auth_user=99)
            test_context.execute(published=STATE.PUBLISH)
                   
            # assert functions was called
            
            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.title)


    
    def test_execute_called_save__add_model_to_data__return_invalid(self):
         
        # arrange


        mock_model = Model(99, title="Proin id massa metus. Aliqua tincidunt.")
        mock_model.type_id = 1
        mock_model.publisher = "Penguin"
        mock_model.page_note = "" # invalid value


        with patch.object(Model, "save", return_value=None):
                
            # act
            
            test_context = ViewModel(db=self.mock_db, scheme_of_work_id=99, lesson_id=12, model=mock_model, auth_user=99)
            test_context.execute(1)
                            
            # assert save functions was not called
            Model.save.assert_not_called()

            # return the invalid object
            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.title)
            self.assertEqual(0, test_context.model.lesson_id)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual(1, len(test_context.model.validation_errors)) 
            self.assertEqual({'page_note': 'required'}, test_context.model.validation_errors) 

