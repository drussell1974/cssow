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

        # arrange
        on_find_or_create__create_new_instance = KeywordModel(15, "Database","")
        
        test_context = ViewModel(self.mock_db, KeywordModel(15,"Database",""))
        
        test_context._find_by_term = Mock(return_value=on_find_or_create__create_new_instance)

        with patch.object(DataAccess, "save", side_effect=KeyError):   
            # act
            with self.assertRaises(KeyError):
                test_context.execute(99)

            # assert
            DataAccess.save.assert_called()
            self.assertEqual(15, test_context.model.id)
            self.assertEqual("Database", test_context.model.term)


    def test_execute_called_save__update_existing(self):

        # arrange
        
        data_to_return = KeywordModel(112, "Unit Testing", "new definition")
        data_to_return.is_valid = True

        # act

        test_context = ViewModel(self.mock_db, KeywordModel(112, "Unit Testing", "new definition"))
        test_context._find_keyword_by_id = Mock(return_value=data_to_return)
        
        with patch.object(DataAccess, "save", return_value=data_to_return):
            
            test_context.execute(99)
            
            # assert functions was called
            DataAccess.save.assert_called()
            self.assertEqual(112, test_context.model.id)
            self.assertEqual("Unit Testing", test_context.model.term)
            self.assertEqual("new definition", test_context.model.definition)


    def test_execute_called_save__add_model_to_data__when_not_exists(self):

        # arrange
        on_find_or_create__create_new_instance = KeywordModel(0, "Unit Test")        
        new_instance_to_save = KeywordModel(119, "Unit Test")

        # act

        test_context = ViewModel(self.mock_db, KeywordModel(0, "Unit Test"))
        test_context._find_by_term = Mock(return_value=on_find_or_create__create_new_instance)
        
        with patch.object(DataAccess, "save", return_value=new_instance_to_save):
            
            test_context.execute(99)
            
            # assert

            test_context._find_by_term.assert_called()
            DataAccess.save.assert_called()
            
            self.assertEqual(119, test_context.model.id)
            self.assertEqual("Unit Test", test_context.model.term)


    def test_execute_not_called_save__add_model_to_data__when_not_valid(self):

        # arrange
        on_find_or_create__create_new_instance = KeywordModel(0, "")        

        test_context = ViewModel(self.mock_db, KeywordModel(0, ""))
 
        test_context._find_by_term = Mock(return_value=on_find_or_create__create_new_instance)
        
        with patch.object(DataAccess, "save"):
            # act

            test_context.execute(99)
            
            # assert
            test_context._find_by_term.assert_called()

            DataAccess.save.assert_not_called()

            self.assertEqual(0, test_context.model.id)
            self.assertEqual("", test_context.model.term)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual({'term': 'required'}, test_context.model.validation_errors)


    def test_execute_called_save__add_model_to_data__when_new_term_already_exists(self):
        """ View will try create a new keyword """
        
        # arrange

        # -- return object with new id
        on_find_or_create__find_existing_instance = KeywordModel(101, "New Keyword")        

        # start with new object id=0
        test_context = ViewModel(self.mock_db, KeywordModel(0, "New Keyword"))
 
        test_context._find_by_term = MagicMock(return_value=on_find_or_create__find_existing_instance)
        
        with patch.object(DataAccess, "save"):
            # act

            test_context.execute(99)
            
            # assert
            test_context._find_by_term.assert_called()

            DataAccess.save.assert_called()


    def test_execute_not_called_save__add_model_to_data__when_passing_json_string(self):
        """ String will be parsed and used to find existing object """
        
        # arrange
        
        test_context = ViewModel(self.mock_db, '{"id":999,"term":"non-existing object","definition":""}')
        test_context._find_keyword_by_id = Mock(return_value=None)
        
        with patch.object(DataAccess, "save", return_value=None):
            
            with self.assertRaises(AttributeError):
                # act

                test_context.execute(99)
                
                # assert
                
            test_context._find_keyword_by_id.assert_not_called()

            DataAccess.save.assert_not_called()

