from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.accounts.viewmodels import AccountDeleteViewModel as ViewModel
from shared.models.cls_teacher import TeacherModel as Model
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_AccountDeleteViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__does_not_exist(self, mock_auth_user):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_fetch(self, mock_auth_user):
        
        # arrange
        
        data_to_return = Model(56, "Lorem Ipsum", department=fake_department(67, institute=fake_institute()))
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual("Lorem Ipsum", self.viewmodel.model.name)


    def test_delete_called_on_execute(self, mock_auth_user):
        
        # arrange
        
        data_to_return = Model(59, "Lorem Ipsum", department=fake_department(67, institute=fake_institute()))

        with patch.object(Model, "get_model", return_value=data_to_return):
            with patch.object(Model, "delete", return_value=None):

                db = MagicMock()
                db.cursor = MagicMock()

                # act
                self.viewmodel = ViewModel(db, auth_user=mock_auth_user)
                self.viewmodel.execute()

                # assert functions was called
                Model.get_model.assert_called()
                Model.delete.assert_called()
