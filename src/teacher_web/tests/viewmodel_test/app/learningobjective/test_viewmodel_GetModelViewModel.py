from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404

# test context

from app.learningobjectives.viewmodels import LearningObjectiveGetModelViewModel as ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_GetModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            with self.assertRaises(Http404):
                self.viewmodel = ViewModel(db=db, learning_objective_id=99, lesson_id=19, scheme_of_work_id=84, auth_user=99)

                # assert functions was called
                Model.get_model.assert_called()
                self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self):
        
        # arrange
        
        data_to_return = Model(56, "How to save the world in a day")
        data_to_return.is_from_db = True
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db=db, learning_objective_id=56, lesson_id=19, scheme_of_work_id=84, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()

            self.assertEqual(56, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.description)
            self.assertTrue(self.viewmodel.model.is_from_db)
