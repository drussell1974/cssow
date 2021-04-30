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
    
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock()
        mock_request.user = None

        self.mock_model = Mock()

        # act
        self.viewmodel = ViewModel(db, mock_request)

        # assert functions was called
        self.assertIsNone(self.viewmodel.model)


    def test_init_called_fetch(self, mock_auth_user):
        
        # arrange
        
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock()
        mock_request.user = MagicMock(id=6079, username="Jane Doe")

        self.mock_model = Mock()

        # act
        self.viewmodel = ViewModel(db, mock_request)

        # assert
        self.assertEqual("Jane Doe", self.viewmodel.model.username)


    def test_delete_called_on_execute(self, mock_auth_user):
        
        # arrange
        
        with patch.object(Model, "save", return_value=None):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.user = MagicMock(id=6079, is_superuser = False)

            # act
            self.viewmodel = ViewModel(db, mock_request)
            self.viewmodel.execute()

            # assert
            Model.save.assert_called()


    def test_delete_exception_raised_if_super_user(self, mock_auth_user):
        
        # arrange
    
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock()
        mock_request.user = MagicMock(id=6079, is_superuser = True)

        with self.assertRaises(Exception):
            # act/assert
            self.viewmodel = ViewModel(db, mock_request)
            self.viewmodel.execute()
