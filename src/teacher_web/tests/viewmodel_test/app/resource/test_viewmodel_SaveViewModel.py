from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.resources.viewmodels import ResourceSaveViewModel as ViewModel
from shared.models.cls_resource import ResourceDataAccess as DataAccess, ResourceModel as Model

#Serializer = test_context.KeywordModelSerializer

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
        
        with patch.object(DataAccess, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=1)
                   
            # assert functions was called
            
            DataAccess.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.title)


    def test_execute_called_insert(self):
        
        # arrange

        mock_model = Model(0, title="Class aptent taciti sociosqu ad")
        mock_model.type_id = 3
        mock_model.publisher = "Penguin"
        mock_model.page_note = " litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales"

        on_save__data_to_return = Model(99, title="Class aptent taciti sociosqu ad")
        
        with patch.object(DataAccess, "_insert", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=1)
                            
            # assert functions was called
            
            DataAccess._insert.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Class aptent taciti sociosqu ad", test_context.model.title)
            self.assertEqual(1, test_context.model.published)
            self.assertEqual("published", test_context.model.published_state)

    
    def test_execute_called_update(self):
        
        # arrange

        mock_model = Model(101, title="Cras leo arcu, interdum.")
        mock_model.type_id = 3
        mock_model.publisher = "Penguin"
        mock_model.page_note = " litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales"

        on_save__data_to_return = Model(99, title="Cras leo arcu, interdum.")
        
        with patch.object(DataAccess, "_update", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=1)
                            
            # assert functions was called
            
            DataAccess._update.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Cras leo arcu, interdum.", test_context.model.title)
            self.assertEqual(1, test_context.model.published)
            self.assertEqual("published", test_context.model.published_state)

    
    def test_execute_called_delete(self):
        
        # arrange

        mock_model = Model(99, title="egestas nisi sodales, cursus mi") # should be able to delete invalid
        mock_model.type_id = 3
        mock_model.publisher = "Penguin"
        mock_model.page_note = ""
        
        on_save__data_to_return = Model(99, "Pegestas nisi sodales, cursus mi")
        on_save__data_to_return.published = 2
        
        with patch.object(DataAccess, "_delete", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=2) # delete

            # assert functions was called
            
            DataAccess._delete.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("egestas nisi sodales, cursus mi", test_context.model.title)
            self.assertEqual(2, test_context.model.published)


    def test_execute_called_save__add_model_to_data__return_invalid(self):
         
        # arrange


        mock_model = Model(99, title="Proin id massa metus. Aliqua tincidunt.")
        mock_model.type_id = 1
        mock_model.publisher = "Penguin"
        mock_model.page_note = "" # invalid value


        with patch.object(DataAccess, "save", return_value=None):
                
            # act
            
            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(1)
                            
            # assert save functions was not called
            DataAccess.save.assert_not_called()

            # return the invalid object
            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.title)
            self.assertEqual(0, test_context.model.lesson_id)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual(1, len(test_context.model.validation_errors)) 
            self.assertEqual({'page_note': 'required'}, test_context.model.validation_errors) 
