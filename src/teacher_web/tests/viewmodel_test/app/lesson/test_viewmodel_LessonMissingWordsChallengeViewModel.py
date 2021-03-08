from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
# test context

from app.lessons.viewmodels import LessonMissingWordsChallengeViewModel as ViewModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_learningobjective import LearningObjectiveModel

class test_viewmodel_LessonMissingWordsChallengeViewModel(TestCase):
    

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass

    
    def test_init_called_fetch__with_exception(self):
        
        # arrange        
        with patch.object(Model, "get_model", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db=db, lesson_id=99, scheme_of_work_id=22, auth_user=99)

    
    def test_init_called_fetch__no_return_rows(self):
        
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

    
    def test_init_called_fetch__return_item(self):
        
        # arrange
        
        data_to_return = Model(99, "Lorem ipsum dolor sit amet, consectetur adipiscing elit")
        data_to_return.learning_objectives = [
                LearningObjectiveModel(1064, "Lorem ipsum dolor sit amet, consectetur adipiscing elit", notes="dapibus in ligula. Duis turpis lectus", missing_words_challenge="dapibus, ligula, lectus"),
                LearningObjectiveModel(1234, "Curabitur luctus venenatis mauris."),
                LearningObjectiveModel(1876, "Donec a ligula mi. Aenean pretium mauris ut nam."),
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
            self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit", self.viewmodel.model.title)
            self.assertEqual(3, len(self.viewmodel.model.learning_objectives))

            self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit", self.viewmodel.model.learning_objectives[0].description)
            self.assertEqual("dapibus in ligula. Duis turpis lectus", self.viewmodel.model.learning_objectives[0].notes)
            self.assertEqual("dapibus, ligula, lectus", self.viewmodel.model.learning_objectives[0].missing_words_challenge)


            self.assertEqual("Donec a ligula mi. Aenean pretium mauris ut nam.", self.viewmodel.model.learning_objectives[2].description)
            self.assertEqual("", self.viewmodel.model.learning_objectives[2].notes)
            self.assertEqual("", self.viewmodel.model.learning_objectives[2].missing_words_challenge)
