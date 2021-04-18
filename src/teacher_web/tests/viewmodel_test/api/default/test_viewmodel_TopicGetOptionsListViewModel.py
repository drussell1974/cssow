from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from api.default.viewmodels import TopicGetOptionsListViewModel as ViewModel

from shared.models.cls_topic import TopicModel as Model


from tests.test_helpers.mocks import fake_ctx_model


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_TopicGetOptionsListViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_options", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, topic_id=3, lvl=1, auth_user=6079)

            # assert functions was called
            Model.get_options.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [Model(56, name="Nullam", department_id=13)]
        
        with patch.object(Model, "get_options", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, topic_id=12, auth_user=6079, lvl=1)

            # assert functions was called
            Model.get_options.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [Model(56, name="placerat", department_id=13),Model(57, name="Aenean", department_id=13),Model(58, name="Praesent", department_id=13)]
        
        with patch.object(Model, "get_options", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, topic_id=1, lvl=1, auth_user=6079)

            # assert functions was called
            Model.get_options.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))