from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.lesson_schedules.viewmodels import LessonScheduleIndexViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model
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
            self.assertEqual(7, actual_result.show_next_days) # default


    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work(id=92, is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(2, "Box of Rain - Grateful Dead", is_from_db=True))
    def test_init_called_fetch__single_item(self, SchemeOfWorkModel_get_model, LessonModel_get_model, mock_auth_user):
        
        # arrange
        
        data_to_return = [fake_lesson_schedule(34, title="", class_code="", class_name="", start_date="2021-06-09T17:20", lesson_id=220, scheme_of_work_id=11, auth_ctx=mock_auth_user)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=11, lesson_id=220, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()
            LessonModel_get_model.assert_called()

            self.assertEqual(1, len(actual_result.model))
            self.assertEqual(7, actual_result.show_next_days) # default
            

    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work(id=92, name="Tumbing Dice - Rolling Stones", is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(3, "Box of Rain - Grateful Dead", is_from_db=True))
    def test_init_called_fetch__multiple_items(self, SchemeOfWorkModel_get_model, LessonModel_get_model, mock_auth_user):
        
        # arrange
        
        data_to_return = [
            fake_lesson_schedule(91, title="Vivamus", class_code="", class_name="", start_date="2021-06-09T17:20", lesson_id=220, scheme_of_work_id=11, auth_ctx=mock_auth_user), 
            fake_lesson_schedule(92, title="Orci", class_code="", class_name="", start_date="2021-06-09T17:20", lesson_id=220, scheme_of_work_id=11, auth_ctx=mock_auth_user),
            fake_lesson_schedule(93,  title="At porta", class_code="", class_name="", start_date="2021-06-09T17:20", lesson_id=220, scheme_of_work_id=11, auth_ctx=mock_auth_user)
            ]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=11, lesson_id=220, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()
            LessonModel_get_model.assert_called()
            
            self.assertEqual(3, len(actual_result.model))
            self.assertEqual(7, actual_result.show_next_days) # default
            

    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work(id=92, name="Tumbing Dice - Rolling Stones", is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(3, "Box of Rain - Grateful Dead", is_from_db=True))
    def test_init_called_fetch__multiple_items_with_POST(self, SchemeOfWorkModel_get_model, LessonModel_get_model, mock_auth_user):
        
        # arrange
        
        data_to_return = [
            fake_lesson_schedule(91, title="Vivamus", class_code="", class_name="", start_date="2021-06-09T17:20", lesson_id=220, scheme_of_work_id=11, auth_ctx=mock_auth_user), 
            fake_lesson_schedule(92, title="Orci", class_code="", class_name="", start_date="2021-06-09T17:20", lesson_id=220, scheme_of_work_id=11, auth_ctx=mock_auth_user),
            fake_lesson_schedule(93,  title="At porta", class_code="", class_name="", start_date="2021-06-09T17:20", lesson_id=220, scheme_of_work_id=11, auth_ctx=mock_auth_user)
            ]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "POST"
            mock_request.POST = { "show_next_days": 14 }

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=11, lesson_id=220, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()
            LessonModel_get_model.assert_called()
            
            self.assertEqual(3, len(actual_result.model))
            self.assertEqual(14, actual_result.show_next_days) # default
            
