from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.resources.viewmodels import ResourceIndexViewModel as ViewModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_resource import ResourceModel as Model
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_GetAllViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    
    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        

        lesson = LessonModel(12)
        lesson.is_from_db = True

        with patch.object(LessonModel, 'get_model', return_value=lesson):
            with patch.object(Model, "get_all", return_value=data_to_return):

                db = MagicMock()
                db.cursor = MagicMock()

                mock_request = Mock()

                # act
                self.viewmodel = ViewModel(db=db, request=mock_request, lesson_id=99, scheme_of_work_id=12, auth_user=99)

                # assert functions was called
                Model.get_all.assert_called()
                self.assertEqual(0, len(self.viewmodel.model))


    
    def test_init_called_fetch__single_row(self):
        
        # arrange
        
        data_to_return = [Model(56)]
        

        lesson = LessonModel(12)
        lesson.is_from_db = True

        with patch.object(LessonModel, 'get_model', return_value=lesson):
            with patch.object(Model, "get_all", return_value=data_to_return):

                db = MagicMock()
                db.cursor = MagicMock()

                mock_request = Mock()

                # act
                self.viewmodel = ViewModel(db=db, request=mock_request, lesson_id=92, scheme_of_work_id=12, auth_user=99)

                # assert functions was called
                Model.get_all.assert_called()
                self.assertEqual(1, len(self.viewmodel.model))


    
    def test_init_called_fetch__multiple_rows(self):
        
        # arrange
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        lesson = LessonModel(12)
        lesson.is_from_db = True

        with patch.object(LessonModel, 'get_model', return_value=lesson):
            with patch.object(Model, "get_all", return_value=data_to_return):

                db = MagicMock()
                db.cursor = MagicMock()

                mock_request = Mock()

                # act
                self.viewmodel = ViewModel(db=db, request=mock_request, lesson_id=20, scheme_of_work_id=100, auth_user=99)

                # assert functions was called
                Model.get_all.assert_called()
                self.assertEqual(3, len(self.viewmodel.model))

