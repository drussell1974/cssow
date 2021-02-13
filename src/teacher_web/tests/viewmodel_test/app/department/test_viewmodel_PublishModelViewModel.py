from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.department.viewmodels import DepartmentPublishModelViewModel as ViewModel
from shared.models.cls_department import DepartmentModel as Model
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_should_call_published(self, mock_auth_user):
        
        # arrange
        
        data_to_return = Model(56, "Lorum Ipsum", institute=InstituteModel(12767111276711, "Lorem Ipsum"))
        
        with patch.object(Model, "publish_by_id", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=mock_auth_user)

            # assert functions was called
            Model.publish_by_id.assert_called()
