import json
from unittest import TestCase, skip
from django.http import Http404
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.lesson_schedules.viewmodels import LessonScheduleDeleteViewModel as ViewModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_teacher_permission_model, mock_scheme_of_work, fake_ctx_model, fake_lesson_schedule

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_DeleteViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @patch.object(LessonModel, "get_model", return_value=LessonModel(34, title="", is_from_db=True))
    @patch.object(Model, "get_model", return_value=fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="", class_code="", start_date="2021-06-09T17:20", lesson_id=23, scheme_of_work_id=34, is_from_db=True))
    def test_init_called_delete__with_exception(self, mock_auth_user, LessonScheduleModel_get_model, LessonModel_get_model):
        
        # arrange        
        with patch.object(Model, "delete", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, schedule_id=987, lesson_id=220, scheme_of_work_id=999, auth_ctx=mock_auth_user)
                self.viewmodel.execute()

                # assert functions were called
                LessonScheduleModel_get_model.assert_called()
                LessonModel_get_model.assert_called()
                

    @patch.object(Model, "get_model", return_value=fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="", class_code="", start_date="2021-06-09T17:20", is_from_db=False, lesson_id=23, scheme_of_work_id=34))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(34, title="", is_from_db=True))
    def test_init_raise_Http404__when_model_not_found(self, mock_auth_user, LessonScheduleModel_get_model, LessonModel_get_model):
    
        db = MagicMock()
        db.cursor = MagicMock()

        self.mock_model = Mock()
        
        with self.assertRaises(Http404):
            with patch.object(Model, "delete", return_value=None):

                # act
                self.viewmodel = ViewModel(db, schedule_id=101, lesson_id=220, scheme_of_work_id=999, auth_ctx=mock_auth_user)
                self.viewmodel.execute()

                # assert functions were called.........
                LessonScheduleModel_get_model.assert_called()
                LessonModel_get_model.assert_called()
                Model.delete.assert_not_called()


    @patch.object(Model, "get_model", return_value=fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="", class_code="", start_date="2021-06-09T17:20", lesson_id=23, scheme_of_work_id=34, is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(34, title="", is_from_db=True))
    def test_init_called_delete__no_return_rows(self, mock_auth_user, LessonScheduleModel_get_model, LessonModel_get_model):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, schedule_id=987, lesson_id=220, scheme_of_work_id=999, auth_ctx=mock_auth_user)
            self.viewmodel.execute()
            
            # assert functions was called
            LessonScheduleModel_get_model.assert_called()
            Model.delete.assert_called()


    @patch.object(Model, "get_model", return_value=fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="", class_code="", start_date="2021-06-09T17:20", lesson_id=23, scheme_of_work_id=34, is_from_db=True))
    @patch.object(LessonModel, "get_model", return_value=LessonModel(34, title="", is_from_db=True))
    def test_init_called_delete__return_item(self, mock_auth_user, LessonScheduleModel_get_model, LessonModel_get_model):
        
        # arrange
        
        data_to_return = LessonScheduleModel_get_model
        data_to_return.published = STATE.DELETE
        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, schedule_id=987, lesson_id=220, scheme_of_work_id=999, auth_ctx=mock_auth_user)
            self.viewmodel.execute()
            
            # assert functions was called
            LessonScheduleModel_get_model.assert_called()
            #LessonModel_get_model.assert_called()
            Model.delete.assert_called()
