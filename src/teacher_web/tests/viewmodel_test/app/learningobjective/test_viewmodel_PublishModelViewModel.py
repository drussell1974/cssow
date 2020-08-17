from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.learningobjectives.viewmodels import LearningObjectivePublishModelViewModel as ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model


class test_viewmodel_PublishModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_should_call_publish_item(self):
        
        # arrange
        
        data_to_return = Model(56)
        
        with patch.object(Model, "publish_item", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Model(56)

            # act
            self.viewmodel = ViewModel(db, self.mock_model.id, 101, auth_user=99)

            # assert functions was called
            Model.publish_item.assert_called()
