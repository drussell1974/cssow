import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.lessons.viewmodels import LessonPublishViewModel as ViewModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_LessonPublishViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_publish__with_exception(self, check_permission):
        
        # arrange        
        with patch.object(Model, "publish", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, auth_user=99, lesson_id=999)
            #TODO: #233 remove self.assertRaises
             
            # assert
            #TODO: #233 assert error_message
            #self.assertEqual("ERROR MESSAGE HERE!!!", self.viewmodel.error_message)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_publish__no_return_rows(self, check_permission):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "publish", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=13, auth_user=99, lesson_id=101)

            # assert functions was called
            Model.publish.assert_called()
            self.assertIsNone(self.viewmodel.model)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_publish__return_item(self, check_permission):
        
        # arrange
        
        data_to_return = Model(912, "How to save the world in a day")
        data_to_return.published = 1

        
        with patch.object(Model, "publish", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=13, auth_user=99, lesson_id=912)

            # assert functions was called
            Model.publish.assert_called()
            self.assertEqual(912, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.title)
            self.assertEqual(1, self.viewmodel.model.published)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_should_raise_PermissionError(self, check_permission):
        # arrange 
        # assert

        with self.assertRaises(PermissionError):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            ViewModel(db=db, scheme_of_work_id=13, auth_user=99, lesson_id=912)