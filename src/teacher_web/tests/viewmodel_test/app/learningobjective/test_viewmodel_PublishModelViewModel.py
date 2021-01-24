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


    def test_should_raise404__when_item_does_not_exist(self):
        
        
        with patch.object(Model, "get_model"):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            #with self.assertRaises(PermissionError):
            #   # act
            ViewModel(db=db, learning_objective_id=56, lesson_id=2, scheme_of_work_id=101, auth_user=99)


    def test_should_call_publish_item(self):
        
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
