from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.default.viewmodels import KeywordSaveViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model


class test_viewmodel_SaveListViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()


    def tearDown(self):
        pass


    def test_execute_not_called_save__with_exception__when_invaid_type(self):
        """ View Model does not process new instance """

        # arrange
        
        test_context = ViewModel(db=self.mock_db, model=None, scheme_of_work_id=23, auth_user=34)
        
        with self.assertRaises(AttributeError):
            # act
            test_context.execute(99)


    def test_execute_called_save__with_exception(self):

        # arrange
        on_find_or_create__create_new_instance = Model(15, "Database","",13)
        
        test_context = ViewModel(db=self.mock_db, scheme_of_work_id=13, model=Model(15,"Database","", 13), auth_user=99)
        
        test_context._find_by_term = Mock(return_value=on_find_or_create__create_new_instance)

        with patch.object(Model, "save", side_effect=KeyError):   
            # act
            
            with self.assertRaises(KeyError):
                test_context.execute(99)

            Model.save.assert_called()
            self.assertEqual(15, test_context.model.id)
            self.assertEqual("Database", test_context.model.term)


    def test_execute_called_save__update_existing(self):

        # arrange
        
        data_to_return = Model(112, "Unit Testing", "new definition", 13)
        data_to_return.is_valid = True

        # act

        test_context = ViewModel(db=self.mock_db, scheme_of_work_id=13, model=Model(112, "Unit Testing", "new definition", 13), auth_user=99)
        test_context._find_keyword_by_id = Mock(return_value=data_to_return)
        
        with patch.object(Model, "save", return_value=data_to_return):
            
            test_context.execute(99)
            
            # assert functions was called
            Model.save.assert_called()
            self.assertEqual(112, test_context.model.id)
            self.assertEqual("Unit Testing", test_context.model.term)
            self.assertEqual("new definition", test_context.model.definition)


    def test_execute_called_save__add_model_to_data__when_not_exists(self):

        # arrange
        on_find_or_create__create_new_instance = Model(0, "Unit Test", scheme_of_work_id=13)        
        new_instance_to_save = Model(119, "Unit Test")

        # act

        test_context = ViewModel(db=self.mock_db, scheme_of_work_id=13, model=Model(0, "Unit Test", scheme_of_work_id=13), auth_user=99)
        #test_context._find_by_term = Mock(return_value=on_find_or_create__create_new_instance)
        
        with patch.object(Model, "save", return_value=new_instance_to_save):
            
            test_context.execute(99)
            
            # assert

            #test_context._find_by_term.assert_called()
            Model.save.assert_called()
            
            self.assertEqual(119, test_context.model.id)
            self.assertEqual("Unit Test", test_context.model.term)


    def test_execute_not_called_save__add_model_to_data__when_not_valid(self):

        # arrange
        on_find_or_create__create_new_instance = Model(0, "", scheme_of_work_id=13)        

        test_context = ViewModel(db=self.mock_db, scheme_of_work_id=13, model= Model(0, "", scheme_of_work_id=13), auth_user=99)
 
        #test_context._find_by_term = Mock(return_value=on_find_or_create__create_new_instance)
        
        with patch.object(Model, "save"):
            # act

            test_context.execute(99)
            
            # assert
            #test_context._find_by_term.assert_called()

            Model.save.assert_not_called()

            self.assertEqual(0, test_context.model.id)
            self.assertEqual("", test_context.model.term)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual({'term': 'required'}, test_context.model.validation_errors)


    def test_execute_called_save__add_model_to_data__when_new_term_already_exists(self):
        """ View will try create a new keyword """
        
        # arrange

        # -- return object with new id
        on_find_or_create__find_existing_instance = Model(101, "New Keyword", scheme_of_work_id=13)        

        # start with new object id=0
        test_context = ViewModel(db=self.mock_db, scheme_of_work_id=13, model=Model(0, "New Keyword", scheme_of_work_id=13), auth_user=99)
 
        #test_context._find_by_term = MagicMock(return_value=on_find_or_create__find_existing_instance)
        
        with patch.object(Model, "save"):
            # act

            test_context.execute(99)
            
            # assert
            #test_context._find_by_term.assert_called()

            Model.save.assert_called()


    def test_execute_not_called_save__add_model_to_data__when_passing_json_string(self):
        """ String will be parsed and used to find existing object """
        
        # arrange
        
        test_context = ViewModel(db=self.mock_db, scheme_of_work_id=34, model='{"id":999,"term":"non-existing object","definition":""}', auth_user=99)
        test_context._find_keyword_by_id = Mock(return_value=None)
        
        with patch.object(Model, "save", return_value=None):
            
            with self.assertRaises(AttributeError):
                # act

                test_context.execute(99)
                
                # assert
                
            test_context._find_keyword_by_id.assert_not_called()

            Model.save.assert_not_called()
  