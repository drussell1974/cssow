from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.institute.viewmodels import InstituteScheduleViewModel as ViewModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_lesson_schedule import LessonScheduleModel
from tests.test_helpers.mocks import *

@patch.object(InstituteModel, "get_model", return_value=InstituteModel(534, "Lorum Ipsum", is_from_db=True))
@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_ScheduleViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_render(self, mock_auth_user, InstituteModel_get_model):
        
        # arrange

        db = MagicMock()
        db.cursor = MagicMock()
        mock_request = Mock()

        self.mock_model = Mock()

        # act
        self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=99, auth_user=mock_auth_user)

        # assert
        InstituteModel_get_model.assert_called()
        self.assertEqual([], self.viewmodel.model)



    def test_init_called_fetch__no_return_rows(self, mock_auth_user, InstituteModel_get_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(LessonScheduleModel, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()
            
            mock_request = Mock()
            mock_request.method = MagicMock(return_value="GET")
            
            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=99, auth_user=mock_auth_user)

            # assert functions was called
            LessonScheduleModel.get_all.assert_called()
            InstituteModel_get_model.assert_called()
            self.assertEqual(7, self.viewmodel.show_next_days) # default


    def test_init_called_fetch__single_row(self, mock_auth_user, InstituteModel_get_model):
        
        # arrange
        model = fake_lesson_schedule(id=22, auth_ctx=mock_auth_user)
        
        data_to_return = [model]
        
        with patch.object(LessonScheduleModel, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = MagicMock(return_value="GET")
            
            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=56, auth_user=mock_auth_user)

            # assert functions was called
            LessonScheduleModel.get_all.assert_called()
            InstituteModel_get_model.assert_called()

            self.assertEqual(1, len(self.viewmodel.model))
            self.assertEqual(7, self.viewmodel.show_next_days) # default


    def test_init_called_fetch__multiple_rows(self, mock_auth_user, InstituteModel_get_model):
        
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
            
            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=56, auth_user=mock_auth_user)

            # assert functions was called
            LessonScheduleModel.get_all.assert_called()
            InstituteModel_get_model.assert_called()

            self.assertEqual(3, len(self.viewmodel.model))
            self.assertEqual(7, self.viewmodel.show_next_days) # default



    def test_init_called_fetch__multiple_rows__with_POST(self, mock_auth_user, InstituteModel_get_model):
        
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

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, request=mock_request, institute_id=56, auth_user=mock_auth_user)

            # assert
            LessonScheduleModel.get_all.assert_called()
            InstituteModel_get_model.assert_called()

            self.assertEqual(3, len(self.viewmodel.model))
            self.assertEqual(14, self.viewmodel.show_next_days)
