import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.department_topic.viewmodels import DepartmentTopicDeleteUnpublishedViewModel as ViewModel
from shared.models.cls_topic import TopicModel as Model
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_delete__with_exception(self, mock_auth_user):
        
        # arrange        
        with patch.object(Model, "delete_unpublished", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, auth_user=mock_auth_user)
                

    def test_init_called_delete__no_return_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=mock_auth_user)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            

    def test_init_called_delete__return_item(self, mock_auth_user):
        
        # arrange
        
        data_to_return = Model(912, "How to save the world in a day")
        data_to_return.published = STATE.DELETE

        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99)

            # assert functions was called
            Model.delete_unpublished.assert_called()
