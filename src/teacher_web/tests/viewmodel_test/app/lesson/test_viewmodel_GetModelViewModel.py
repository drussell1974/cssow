from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
# test context

from app.lessons.viewmodels import LessonGetModelViewModel as ViewModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_LessonGetModelViewModel(TestCase):
    

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass

    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_fetch__with_exception(self, check_permission):
        
        # arrange        
        with patch.object(Model, "get_model", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db=db, lesson_id=99, scheme_of_work_id=22, auth_user=99)
            #TODO: #233 remove self.assertRaises
             
            # assert
            #TODO: #233 assert error_message
            #self.assertEqual("ERROR MESSAGE HERE!!!", self.viewmodel.error_message)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_fetch__no_return_rows(self, check_permission):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            with self.assertRaises(Http404):
                self.viewmodel = ViewModel(db=db, lesson_id=123, scheme_of_work_id=22, auth_user=99)

                # assert functions was called
                Model.get_model.assert_called()
                self.assertIsNone(self.viewmodel.model)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_fetch__return_item(self, check_permission):
        
        # arrange
        
        data_to_return = Model(99, "How to save the world in a day")
        data_to_return.key_words = [
                KeywordModel(34, "CPU"),
                KeywordModel(45, "Fetch Decode Execute"),
                KeywordModel(106, "RAM"),
            ]
        data_to_return.is_from_db = True

        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, lesson_id=456, scheme_of_work_id=22, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(99, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.title)
            self.assertEqual(3, len(self.viewmodel.model.key_words))



    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_should_raise_PermissionError(self, check_permission):
        # arrange

        db = MagicMock()
        db.cursor = MagicMock()
        
        with self.assertRaises(PermissionError):
            # act
            self.viewmodel = ViewModel(db=db, lesson_id=99, scheme_of_work_id=22, auth_user=99)
