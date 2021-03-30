from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.lesson_ks123pathways.viewmodels import LessonKS123PathwaySelectViewModel as ViewModel
from shared.models.cls_ks123pathway import KS123PathwayModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_LessonKS123PathwaySelectViewModel_view(TestCase):
    
    fake_lesson = LessonModel(45)
    fake_lesson.is_from_db = True


    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    @patch.object(Model, "get_options", return_value=[])
    def test_init_called_fetch__no_return_rows(self, LessonModel__get_model, LessonModel__get_options, mock_auth_user):
        
        # arrange
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )
    
        self.fake_schemeofwork = SchemeOfWorkModel(22, name="Lorem", study_duration=2, start_study_in_year=10)
        self.fake_schemeofwork.is_from_db = True
                
        with patch.object(SchemeOfWorkModel, "get_model", return_value=self.fake_schemeofwork):
            with patch.object(Model, "get_options", return_value=[]):
                # act
                actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=22, lesson_id=45, auth_user=mock_auth_user)
                actual_result.view(mock_request)

                # assert functions was called
                SchemeOfWorkModel.get_model.assert_called()
                LessonModel__get_options.assert_called()
                Model.get_options.assert_called()

                self.assertEqual(45, actual_result.model.id)

    
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    def test_init_called_fetch_single_item(self, LessonModel__get_model, mock_auth_user):

        # arrange
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )
    
        self.fake_schemeofwork = SchemeOfWorkModel(22, name="Lorem", study_duration=3, start_study_in_year=7)
        self.fake_schemeofwork.is_from_db = True   
    
        with patch.object(SchemeOfWorkModel, "get_model", return_value=self.fake_schemeofwork):
            with patch.object(Model, "get_options", return_value=[Model(34, objective="Vestibulum tincidunt leo ac erat gravida faucibus non eu nulla.")]):
                # act
                actual_result = ViewModel(db=db, request=mock_request, lesson_id=45, scheme_of_work_id=22, auth_user=mock_auth_user)
                actual_result.view(mock_request)

                # assert functions was called
                SchemeOfWorkModel.get_model.assert_called()
                LessonModel__get_model.assert_called()
                Model.get_options.assert_called()

                self.assertEqual(45, actual_result.model.id)
                self.assertEqual(1, len(actual_result.ks123pathway))


    
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    @patch.object(Model, "get_options", return_value=[
        Model(34, objective="Sed id magna maximus, elementum ex pellentesque, vehicula magna."), 
        Model(35, objective="Donec vestibulum ipsum a nisi laoreet, eget tempus leo facilisis."), 
        Model(36, objective="Integer ac lacus mattis, faucibus ligula sit amet, blandit tortor.")
        ])
    def test_init_called_fetch__multiple_items(self, LessonModel__get_model, KS123Pathway__get_options, mock_auth_user):
        
        # arrange
        
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )
        
        self.fake_schemeofwork = SchemeOfWorkModel(22, name="Lorem", study_duration=2, start_study_in_year=10)
        self.fake_schemeofwork.is_from_db = True   
                
        with patch.object(SchemeOfWorkModel, "get_model", return_value=self.fake_schemeofwork):
            fake_ks123pathway = []
            fake_ks123pathway.append(Model(34, objective="Donec vestibulum ipsum a nisi laoreet, eget tempus leo facilisis."))
            fake_ks123pathway.append(Model(35, objective="Suspendisse pellentesque velit id tellus elementum eleifend."))
            fake_ks123pathway.append(Model(36, objective="Sed hendrerit massa sit amet ullamcorper maximus."))
            
            with patch.object(Model, "get_options", return_value=fake_ks123pathway):
                # act
                actual_result = ViewModel(db=db, request=mock_request, lesson_id=45, scheme_of_work_id=12, auth_user=6079)
                actual_result.view(mock_request)

                # assert functions was called
                SchemeOfWorkModel.get_model.assert_called()
                KS123Pathway__get_options.assert_called()     
                Model.get_options.assert_called()

                self.assertEqual(45, actual_result.model.id)
                self.assertEqual(3, len(actual_result.ks123pathway))
