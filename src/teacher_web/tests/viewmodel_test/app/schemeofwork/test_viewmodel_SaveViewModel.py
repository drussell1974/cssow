from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.schemesofwork.viewmodels import SchemeOfWorkSaveModelViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkDataAccess as DataAccess, SchemeOfWorkModel as Model

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
        
        with patch.object(DataAccess, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=1)
                            
            # assert functions was called
            
            DataAccess.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.name)


    def test_execute_called_insert(self):
        
        # arrange

        mock_model = Model(0, "Aliquam pellentesque urna ac hendrerit")
        mock_model.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore"
        mock_model.key_stage_id = 2
        mock_model.lesson_id = 11
        mock_model.exam_board_id = 56

        on_save__data_to_return = Model(99, "Aliquam pellentesque urna ac hendrerit")
        
        with patch.object(DataAccess, "_insert", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=1)
                            
            # assert functions was called
            
            DataAccess._insert.assert_called()
            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Aliquam pellentesque urna ac hendrerit", test_context.model.name)
            self.assertEqual(1, test_context.model.published)
            self.assertEqual("published", test_context.model.published_state)


    def test_execute_called_update(self):
        
        # arrange

        mock_model = Model(101, name="Fusce mattis sagittis orci, quis")
        mock_model.description = "Lorem ipsum dolor sit amet."
        mock_model.key_stage_id = 3
        mock_model.lesson_id = 46
        mock_model.exam_board_id = 56

        on_save__data_to_return = Model(101, "Fusce mattis sagittis orci, quis")
        
        with patch.object(DataAccess, "_update", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=1)
                            
            # assert functions was called
            
            DataAccess._update.assert_called()

            self.assertEqual(101, test_context.model.id)
            self.assertEqual("Fusce mattis sagittis orci, quis", test_context.model.name)
            self.assertEqual(1, test_context.model.published)
            self.assertEqual("published", test_context.model.published_state)


    def test_execute_called_delete(self):
        
        # arrange

        mock_model = Model(99, "Vestibulum lobortis, lectus et porttitor")
        mock_model.description = "Lorem ipsum dolor sit amet."
        mock_model.published = 1
        mock_model.key_stage_id = 5
        mock_model.lesson_id = 338
        mock_model.exam_board_id = 71

        on_save__data_to_return = Model(99, "Vestibulum lobortis, lectus et porttitor")
        on_save__data_to_return.published = 2
        
        with patch.object(DataAccess, "_delete", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(published=2) # delete

            # assert functions was called
            
            DataAccess._delete.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Vestibulum lobortis, lectus et porttitor", test_context.model.name)
            self.assertEqual(2, test_context.model.published)


    def test_execute_called_save__add_model_to_data__return_invalid(self):
         
        # arrange

        mock_model = Model(99, name="Suspendisse nisi dui, lobortis ut")
        mock_model.key_stage_id = 3
        mock_model.lesson_id = 0 # invalid value
        mock_model.description = "unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo."

        with patch.object(DataAccess, "save", return_value=None):
                
            # act
            
            test_context = ViewModel(self.mock_db, mock_model, auth_user=99)
            test_context.execute(1)
                            
            # assert save functions was not called
            DataAccess.save.assert_not_called()

            # return the invalid object
            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Suspendisse nisi dui, lobortis ut", test_context.model.name)
            self.assertEqual(0, test_context.model.lesson_id)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual(1, len(test_context.model.validation_errors)) 
            self.assertEqual({'exam_board_id': '0 is not a valid range'}, test_context.model.validation_errors) 
