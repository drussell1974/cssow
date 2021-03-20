from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
# test context

from app.lessons.viewmodels import LessonGetModelViewModel as ViewModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.cls_keyword import KeywordModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_LessonGetModelViewModel(TestCase):
    

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__with_exception(self, mock_auth_user):
        
        # arrange        
        with patch.object(Model, "get_model", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db=db, lesson_id=99, scheme_of_work_id=22, auth_user=mock_auth_user)


    def test_init_called_fetch__no_return_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):
            with patch.object(LessonScheduleModel, "get_model", return_value=LessonScheduleModel(15, "ABCDEF", lesson_id=99, scheme_of_work_id=12)):

                db = MagicMock()
                db.cursor = MagicMock()

                self.mock_model = Mock()

                # act
                with self.assertRaises(Http404):
                    self.viewmodel = ViewModel(db=db, lesson_id=123, scheme_of_work_id=22, auth_user=mock_auth_user)

                    # assert functions was called
                    Model.get_model.assert_called()
                    LessonScheduleModel.get_model.assert_called()

                    self.assertIsNone(self.viewmodel.model)
                    self.assertEqual("ABCDEF", self.viewmodel.lesson_schedule.class_code)


    def test_init_called_fetch__return_item(self, mock_auth_user):
        
        # arrange
        
        data_to_return = Model(99, "How to save the world in a day")
        data_to_return.key_words = [
                KeywordModel(34, "CPU"),
                KeywordModel(45, "Fetch Decode Execute"),
                KeywordModel(106, "RAM"),
            ]
        data_to_return.is_from_db = True

        with patch.object(Model, "get_model", return_value=data_to_return):
            with patch.object(LessonScheduleModel, "get_model", return_value=LessonScheduleModel(15, "ABCDEF", lesson_id=99, scheme_of_work_id=12)):
                
                db = MagicMock()
                db.cursor = MagicMock()

                self.mock_model = Mock()
                
                # act
                self.viewmodel = ViewModel(db=db, lesson_id=456, scheme_of_work_id=22, auth_user=mock_auth_user)

                # assert functions was called
                Model.get_model.assert_called()
                LessonScheduleModel.get_model.assert_called()

                self.assertEqual(99, self.viewmodel.model.id)
                self.assertEqual("How to save the world in a day", self.viewmodel.model.title)
                self.assertEqual(3, len(self.viewmodel.model.key_words))
                self.assertEqual("ABCDEF", self.viewmodel.lesson_schedule.class_code)
