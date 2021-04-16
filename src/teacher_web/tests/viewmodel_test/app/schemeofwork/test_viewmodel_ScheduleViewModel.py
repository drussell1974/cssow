from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.schemesofwork.viewmodels import SchemeOfWorkScheduleViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson_schedule import LessonScheduleModel
from tests.test_helpers.mocks import *

@patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work())
@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_ScheduleViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_render(self, mock_auth_user, SchemeOfWorkModel_get_model):
        
        # arrange

        db = MagicMock()
        db.cursor = MagicMock()
        mock_request = Mock()
        mock_request.session = { "lesson_schedule.show_next_days":7 }


        self.mock_model = Mock()

        # act
        self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=99, department_id=67, scheme_of_work_id=11, auth_user=mock_auth_user)

        # assert
        SchemeOfWorkModel_get_model.assert_called()
        self.assertEqual([], self.viewmodel.model)



    def test_init_called_fetch__no_return_rows(self, mock_auth_user, SchemeOfWorkModel_get_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(LessonScheduleModel, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()
            
            mock_request = Mock()
            mock_request.method = MagicMock(return_value="GET")
            mock_request.session = { "lesson_schedule.show_next_days":7 }

            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=99, department_id=67, scheme_of_work_id=11, auth_user=mock_auth_user)

            # assert functions was called
            LessonScheduleModel.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()
            self.assertEqual(7, self.viewmodel.show_next_days) # default


    def test_init_called_fetch__single_row(self, mock_auth_user, SchemeOfWorkModel_get_model):
        
        # arrange
        model = fake_lesson_schedule(id=22, auth_ctx=mock_auth_user)
        
        data_to_return = [model]
        
        with patch.object(LessonScheduleModel, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = MagicMock(return_value="GET")
            mock_request.session = { "lesson_schedule.show_next_days":7 }

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=56, department_id=67, scheme_of_work_id=11, auth_user=mock_auth_user)

            # assert functions was called
            LessonScheduleModel.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()

            self.assertEqual(1, len(self.viewmodel.model))
            self.assertEqual(7, self.viewmodel.show_next_days) # default


    def test_init_called_fetch__multiple_rows(self, mock_auth_user, SchemeOfWorkModel_get_model):
        
        # arrange
        
        data_to_return = [
            fake_lesson_schedule(id=22, auth_ctx=mock_auth_user),
            fake_lesson_schedule(id=23, auth_ctx=mock_auth_user),
            fake_lesson_schedule(id=24, auth_ctx=mock_auth_user)
        ]
        
        with patch.object(LessonScheduleModel, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = MagicMock(return_value="GET")
            mock_request.session = { "lesson_schedule.show_next_days":7 }

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=56, department_id=67, scheme_of_work_id=11, auth_user=mock_auth_user)

            # assert functions was called
            LessonScheduleModel.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()

            self.assertEqual(3, len(self.viewmodel.model))
            self.assertEqual(7, self.viewmodel.show_next_days) # default



    def test_init_called_fetch__multiple_rows__with_POST(self, mock_auth_user, SchemeOfWorkModel_get_model):
        
        # arrange
        
        data_to_return = [
            fake_lesson_schedule(id=22, auth_ctx=mock_auth_user),
            fake_lesson_schedule(id=23, auth_ctx=mock_auth_user),
            fake_lesson_schedule(id=24, auth_ctx=mock_auth_user)
        ]
        
        with patch.object(LessonScheduleModel, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "POST"
            mock_request.POST = { "show_next_days": 14 }
            mock_request.session = { "lesson_schedule.show_next_days":7 }

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=56,  department_id=67, scheme_of_work_id=11, auth_user=mock_auth_user)

            # assert
            LessonScheduleModel.get_all.assert_called()
            SchemeOfWorkModel_get_model.assert_called()

            self.assertEqual(3, len(self.viewmodel.model))
            self.assertEqual(14, self.viewmodel.show_next_days)
