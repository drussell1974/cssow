from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.accounts.viewmodels import AccountIndexViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_AccountIndexViewModel__latest_schemes_of_work(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_latest_schemes_of_work", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_latest_schemes_of_work.assert_called()
            self.assertEqual(0, len(self.viewmodel.latest_schemes_of_work))


    def test_init_called_fetch__single_row(self, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(56, name="Test", study_duration=3, start_study_in_year=7)]
        
        with patch.object(Model, "get_latest_schemes_of_work", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_latest_schemes_of_work.assert_called()
            self.assertEqual(1, len(self.viewmodel.latest_schemes_of_work))


    def test_init_called_fetch__multiple_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(56, name="Test1", study_duration=3, start_study_in_year=7),Model(57, name="Test2", study_duration=3, start_study_in_year=7),Model(58, name="Test3", study_duration=3, start_study_in_year=7),Model(59, name="Test4", study_duration=3, start_study_in_year=7)]
        
        with patch.object(Model, "get_latest_schemes_of_work", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_latest_schemes_of_work.assert_called()
            self.assertEqual(4, len(self.viewmodel.latest_schemes_of_work))
