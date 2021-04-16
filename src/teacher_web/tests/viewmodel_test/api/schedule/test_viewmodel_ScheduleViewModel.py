from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from api.schedules.viewmodels import LessonScheduleViewModel as ViewModel
from shared.models.core.context import Ctx
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model
from tests.test_helpers.mocks import fake_ctx_model, fake_lesson_schedule, fake_resolve_schedule_urls


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_ScheduleViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, scheme_of_work_id=11, lesson_id=220, show_next_days=7, auth_ctx=mock_ctx_model, fn_resolve_url=fake_resolve_schedule_urls)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))
            
            

    def test_init_called_fetch__single_row(self, mock_ctx_model):
        
        # arrange
        mock_ctx_model.institute_id = 12767111276711
        mock_ctx_model.department_id = 67

        mock_resolve_schedule_urls = MagicMock()

        data_to_return = [fake_lesson_schedule(id=56, auth_ctx=mock_ctx_model, fn_resolve_url=mock_resolve_schedule_urls)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, scheme_of_work_id=11, lesson_id=220, show_next_days=0, auth_ctx=mock_ctx_model, fn_resolve_url=mock_resolve_schedule_urls)

            # assert functions was called
            Model.get_all.assert_called()
            mock_resolve_schedule_urls.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self, mock_ctx_model):
        
        # arrange
        mock_ctx_model.institute_id = 12767111276711
        mock_ctx_model.department_id = 67

        mock_resolve_schedule_urls = MagicMock()
        
        data_to_return = [
            fake_lesson_schedule(id=56, class_name="Tic", auth_ctx=mock_ctx_model, fn_resolve_url=mock_resolve_schedule_urls),
            fake_lesson_schedule(id=57, class_name="Tac", auth_ctx=mock_ctx_model, fn_resolve_url=mock_resolve_schedule_urls),
            fake_lesson_schedule(id=59, class_name="Toe", auth_ctx=mock_ctx_model, fn_resolve_url=mock_resolve_schedule_urls),
        ]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, scheme_of_work_id=11, lesson_id=220, show_next_days=0, auth_ctx=mock_ctx_model, fn_resolve_url=mock_resolve_schedule_urls)

            # assert functions was called
            Model.get_all.assert_called()
            mock_resolve_schedule_urls.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))