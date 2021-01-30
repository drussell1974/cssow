from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.keywords.viewmodels import KeywordMergeViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel


class test_viewmodel_MergeViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()

    def tearDown(self):
        pass


    def test_execute_called_save__with_exception(self):

        # arrange
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = { 
            "published":"2",
            "next":"/"
        }
        
        with patch.object(Model, "merge_duplicates", side_effect=KeyError):   
            # act
            
            with self.assertRaises(KeyError):
                test_context = ViewModel(db=self.mock_db, keyword_id=15, scheme_of_work_id=13, auth_user=99)
        
                test_context.execute(mock_request)

    
    def test_execute_called_merge_duplicates(self):

        # arrange
        
        data_to_return = Model(334, "Me Enamore", "new definition", 13)
        data_to_return.is_valid = True
        
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = { 
            "published":"2",
            "next":"/"
        }

        # act

        with patch.object(Model, "merge_duplicates", return_value=data_to_return):
            

            test_context = ViewModel(db=self.mock_db, keyword_id=112, scheme_of_work_id=13, auth_user=99)
        
            test_context.execute(mock_request)
            
            # assert

            Model.merge_duplicates.assert_called()
            
            self.assertEqual(334, test_context.model.id)
            self.assertEqual("Me Enamore", test_context.model.term)
            self.assertEqual("new definition", test_context.model.definition)

    
    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(92, "Lo Hecho Esta Hecho", is_from_db=True))
    @patch.object(Model, "get_model", return_value=Model(365, "Me Enamore", is_from_db=True))
    def test_execute_not_called_save__add_model_to_data__when_not_valid(self, SchemeOfWorkModel_get_model, KeywordModel_get_model):
    
        mock_request = Mock()

        with patch.object(Model, "merge_duplicates"):
            # act

            test_context = ViewModel(db=self.mock_db, keyword_id=29, scheme_of_work_id=13, auth_user=99)
            
            test_context.execute(mock_request)
            
            # assert
            
            Model.merge_duplicates.assert_not_called()
            SchemeOfWorkModel_get_model.assert_called()
            KeywordModel_get_model.assert_called()
            