from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.default.viewmodels import KeywordSaveViewModel as ViewModel, KeywordGetModelViewModel
from shared.models.cls_keyword import KeywordDataAccess as DataAccess, KeywordModel


class test_viewmodel_SaveListViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()


    def tearDown(self):
        pass


    def test_execute_not_called_save__with_exception__when_invaid_type(self):
        """ View Model does not process new instance """

        # arrange
        
        test_context = ViewModel(self.mock_db, KeywordGetModelViewModel)
        
        with self.assertRaises(AttributeError):
            # act
            test_context.execute(99)


    def test_execute_called_save__with_exception(self):
        """ View Model does not process new instance """

        # arrange
        on_find_or_create__create_new_instance = KeywordModel(0, "Database")
        
        test_context = ViewModel(self.mock_db, "Database")
        
        test_context._find_or_create_by_term = Mock(return_value=on_find_or_create__create_new_instance)

        with patch.object(DataAccess, "save", side_effect=KeyError):
    
            with self.assertRaises(KeyError):
                # act
                test_context.execute(99)


    def test_execute_called_save__add_existing_int(self):
        """ View Model will find existing instance from id"""

        # arrange
        
        data_to_return = KeywordModel(112, "Unit Testing")
        data_to_return.is_valid = True

        # act

        test_context = ViewModel(self.mock_db, "112")
        test_context._find_keyword_by_id = Mock(return_value=data_to_return)
        
        with patch.object(DataAccess, "save", return_value=data_to_return):
            
            test_context.execute(99)
            
            # assert functions was called
            DataAccess.save.assert_not_called()
            self.assertEqual(112, test_context.model.id)
            self.assertEqual("Unit Testing", test_context.model.term)


    def test_execute_called_save__add_model_to_data__when_not_exists(self):
        """ View model will create a valid new instances and save it to the database with a new id"""

        # arrange
        on_find_or_create__create_new_instance = KeywordModel(0, "Unit Test")        
        new_instance_to_save = KeywordModel(119, "Unit Test")

        # act

        test_context = ViewModel(self.mock_db, "Unit Test")
        test_context._find_or_create_by_term = Mock(return_value=on_find_or_create__create_new_instance)
        
        with patch.object(DataAccess, "save", return_value=new_instance_to_save):
            
            test_context.execute(99)
            
            # assert

            test_context._find_or_create_by_term.assert_called()
            DataAccess.save.assert_called()
            
            self.assertEqual(119, test_context.model.id)
            self.assertEqual("Unit Test", test_context.model.term)


    def test_execute_not_called_save__add_model_to_data__when_not_valid(self):
        """ View model will create new instance that is not valid """

        # arrange
        on_find_or_create__create_new_instance = KeywordModel(0, "")        

        test_context = ViewModel(self.mock_db, "")
 
        test_context._find_or_create_by_term = Mock(return_value=on_find_or_create__create_new_instance)
        
        with patch.object(DataAccess, "save"):
           # act

            
            with self.assertRaises(ValueError):
 
                test_context.execute(99)
                
                # assert
                test_context._find_or_create_by_term.assert_called()
 
                DataAccess.save.assert_not_called()

                self.assertEqual(99999, test_context.model.id)
                self.assertEqual("XXXX", test_context.model.term)


    def test_execute_called_save__add_model_to_data__when_new_term_already_exists(self):
        """ View will try to create a new keyword where the term already exists in the database """
        
        # arrange
        on_find_or_create__find_existing_instance = KeywordModel(101, "Tuple")        

        test_context = ViewModel(self.mock_db, "Tuple")
 
        test_context._find_or_create_by_term = Mock(return_value=on_find_or_create__find_existing_instance)
        
        with patch.object(DataAccess, "save"):
            # act

            test_context.execute(99)
            
            # assert
            test_context._find_or_create_by_term.assert_called()

            DataAccess.save.assert_not_called()

            self.assertEqual(101, test_context.model.id)
            self.assertEqual("Tuple", test_context.model.term)


    def test_execute_not_called_save__add_model_to_data__when_string_is_an_integer(self):
        """ String will be parsed and used to find existing object """
        
        # arrange

        
        test_context = ViewModel(self.mock_db, "999")
        test_context._find_keyword_by_id = Mock(return_value=None)
        
        with patch.object(DataAccess, "save", return_value=None):
            
            with self.assertRaises(KeyError):
                # act

                test_context.execute(99)
                
                # assert
                
                test_context._find_keyword_by_id.assert_called()
 
                DataAccess.save.assert_not_called()

                self.assertEqual(99999, test_context.model.id)
                self.assertEqual("XXXX", test_context.model.term)



