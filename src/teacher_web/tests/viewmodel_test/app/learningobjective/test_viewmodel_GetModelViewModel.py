from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.learningobjectives.viewmodels import LearningObjectiveGetModelViewModel as ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model


class test_viewmodel_GetModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, self.mock_model, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self):
        
        # arrange
        
        data_to_return = Model(56, "How to save the world in a day")
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, self.mock_model, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()

            self.assertEqual(56, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.description)