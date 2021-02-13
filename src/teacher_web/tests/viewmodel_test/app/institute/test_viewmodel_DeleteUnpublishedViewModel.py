
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.institute.viewmodels import InstituteDeleteUnpublishedViewModel as ViewModel
from shared.models.cls_institute import InstituteModel as Model
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    
    def test_should_call_delete_unpublished(self, mock_auth_user):
        
        # arrange
        
        data_to_return = Model(56, "Lorem Ipsum")
        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=mock_auth_user)

            # assert functions was called
            Model.delete_unpublished.assert_called()
