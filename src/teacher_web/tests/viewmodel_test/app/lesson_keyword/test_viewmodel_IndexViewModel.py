from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.lesson_keywords.viewmodels import LessonKeywordIndexViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_IndexViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work(id=34, name="Tumbing Dice - Rolling Stones", is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(1, "Box of Rain - Grateful Dead", is_from_db=True))
    def test_init_called_fetch__no_return_rows(self, SchemeOfWorkModel_get_model, LessonModel_get_model, mock_auth_user):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=34, lesson_id=1, auth_user=mock_auth_user)
            # assert functions was called
            Model.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()
            LessonModel_get_model.assert_called()

            self.assertEqual(0, len(actual_result.model))


    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work(id=92, is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(2, "Box of Rain - Grateful Dead", is_from_db=True))
    def test_init_called_fetch__single_item(self, SchemeOfWorkModel_get_model, LessonModel_get_model, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(34, "")]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=38, lesson_id=2, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()
            LessonModel_get_model.assert_called()

            self.assertEqual(1, len(actual_result.model))
            

    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work(id=92, name="Tumbing Dice - Rolling Stones", is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(3, "Box of Rain - Grateful Dead", is_from_db=True))
    def test_init_called_fetch__multiple_items(self, SchemeOfWorkModel_get_model, LessonModel_get_model, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(91, "Tic"), Model(92, "Tac"), Model(93, "Toe")]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=92, lesson_id=3, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()
            LessonModel_get_model.assert_called()
            
            self.assertEqual(3, len(actual_result.model))
            