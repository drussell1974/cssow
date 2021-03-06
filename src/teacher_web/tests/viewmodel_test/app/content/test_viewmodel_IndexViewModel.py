from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
from tests.viewmodel_test.viewmodel_testcase import ViewModelTestCase
from app.content.viewmodels import ContentIndexViewModel as ViewModel
from shared.models.cls_content import ContentModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.utils.breadcrumb_generator import BreadcrumbGenerator
from tests.test_helpers.mocks import *

@patch.object(BreadcrumbGenerator, "get_items", return_value=fake_breadcrumbs())
class test_viewmodel_IndexViewModel(ViewModelTestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass

    def test_init_called_404_if_scheme_of_work_not_found(self, mock_bc):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, "Test 2", name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=None):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    with self.assertRaises(Http404):
                        self.viewmodel = ViewModel(db, scheme_of_work_id = 999, auth_user=99)

                        # assert functions was called
                        Model.get_all.assert_called()
                        SchemeOfWorkModel.get_options.assert_called()
                        SchemeOfWorkModel.get_model.assert_called()

                        self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_404_if_scheme_of_work_not_found(self, mock_bc):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=None):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    with self.assertRaises(Http404):
                        self.viewmodel = ViewModel(db=db, scheme_of_work_id = 999, auth_user=99)

                        # assert functions was called
                        Model.get_all.assert_called()
                        SchemeOfWorkModel.get_options.assert_called()
                        SchemeOfWorkModel.get_model.assert_called()

                        self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__no_return_rows(self, mock_bc):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(11, name="Test", study_duration=3, start_study_in_year=7, is_from_db=True)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    mock_request = MagicMock()

                    # act
                    self.viewmodel = ViewModel(db=db, scheme_of_work_id=999, auth_user=99)

                    # assert functions was called
                    Model.get_all.assert_called()
                    SchemeOfWorkModel.get_options.assert_called()
                    SchemeOfWorkModel.get_model.assert_called()

                    self.assertEqual(0, len(self.viewmodel.model))
                    self.assertViewModelContent(mock_request, self.viewmodel, "", "Test", "Scheme of work", {})                


    def test_init_called_fetch__single_row(self, mock_bc):
        
        # arrange
        
        data_to_return = [Model(56,"", "")]

        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(11, name="Test", study_duration=3, start_study_in_year=7, is_from_db=True)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()
                    
                    mock_request = MagicMock()
                    
                    # act
                    self.viewmodel = ViewModel(db=db, scheme_of_work_id=101, auth_user=99)

                    # assert functions was called
                    Model.get_all.assert_called()
                    SchemeOfWorkModel.get_options.assert_called()
                    SchemeOfWorkModel.get_model.assert_called()
                    
                    self.assertEqual(1, len(self.viewmodel.model))                    
                    self.assertViewModelContent(mock_request, self.viewmodel, "", "Test", "Scheme of work", {})                


    def test_init_called_fetch__multiple_rows(self, mock_bc):
        
        # arrange
        
        data_to_return = [Model(56,"", ""),Model(57,"", ""),Model(58,"", "")]
 
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(11, name="Test", study_duration=3, start_study_in_year=7, is_from_db=True)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    mock_request = MagicMock()
                    
                    # act
                    self.viewmodel = ViewModel(db=db, scheme_of_work_id=103, auth_user=99)

                    # assert functions was called
                    Model.get_all.assert_called()
                    SchemeOfWorkModel.get_options.assert_called()
                    SchemeOfWorkModel.get_model.assert_called()

                    self.assertEqual(3, len(self.viewmodel.model))
                    self.assertViewModelContent(mock_request, self.viewmodel, "", "Test", "Scheme of work", {})
