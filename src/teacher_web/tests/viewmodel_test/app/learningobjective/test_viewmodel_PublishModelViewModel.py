from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
from app.learningobjectives.viewmodels import LearningObjectivePublishModelViewModel as ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_PublishModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @skip("Http404 not implemented")
    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_should_raise404__when_item_does_not_exist(self, check_permission):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            with self.assertRaises(Http404):
                # act
                ViewModel(db=db, learning_objective_id=56, scheme_of_work_id=101, auth_user=99)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_should_call_publish_item(self, check_permission):
        
        # arrange
        
        data_to_return = Model(56)
        
        with patch.object(Model, "publish_item", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Model(56)

            # act
            self.viewmodel = ViewModel(db=db, learning_objective_id=56, lesson_id=99, scheme_of_work_id=101, auth_user=99)

            # assert functions was called
            Model.publish_item.assert_called()


    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_should_raise_PermissionError(self, check_permission):
        # arrange 
        # assert
        with self.assertRaises(PermissionError):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db=db, learning_objective_id=56, scheme_of_work_id=101, auth_user=99)
