from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.default.viewmodels import DefaultIndexViewModel as ViewModel
from shared.models.cls_department import DepartmentModel as Model
from shared.models.cls_institute import InstituteModel
from tests.test_helpers.mocks import *


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(InstituteModel, "get_my", return_value=[fake_institute()])
class test_viewmodel_DefaultIndexViewModel__my_departments(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, InstituteModel_get_my, mock_auth_user):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            InstituteModel_get_my.assert_called()
            Model.get_my.assert_called()

            self.assertEqual(1, len(self.viewmodel.institutes))
            self.assertEqual(0, len(self.viewmodel.institutes[0].departments))


    def test_init_called_fetch__single_row(self, InstituteModel_get_my, mock_auth_user):
        
        # arrange
        
        mock_institute = mock_auth_user.institute

        data_to_return = [fake_department(56, institute=mock_institute)]
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            InstituteModel_get_my.assert_called()
            Model.get_my.assert_called()

            self.assertEqual(1, len(self.viewmodel.institutes))
            self.assertEqual(1, len(self.viewmodel.institutes[0].departments))
            self.assertEqual(3, self.viewmodel.institutes[0].departments[0].number_of_schemes_of_work)
            self.assertEqual(2, self.viewmodel.institutes[0].departments[0].number_of_topics)
            self.assertEqual(10, self.viewmodel.institutes[0].departments[0].number_of_pathways)


    def test_init_called_fetch__multiple_rows(self, InstituteModel_get_my, mock_auth_user):
        
        # arrange
        
        mock_institute = mock_auth_user.institute

        data_to_return = [
            fake_department(57, institute=mock_institute),
            fake_department(58, institute=mock_institute),
            fake_department(59, institute=mock_institute)
            ]
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            InstituteModel_get_my.assert_called()
            Model.get_my.assert_called()
            
            self.assertEqual(1, len(self.viewmodel.institutes))
            self.assertEqual(3, len(self.viewmodel.institutes[0].departments))

            self.assertEqual(3, self.viewmodel.institutes[0].departments[0].number_of_schemes_of_work)
            self.assertEqual(2, self.viewmodel.institutes[0].departments[0].number_of_topics)
            self.assertEqual(10, self.viewmodel.institutes[0].departments[0].number_of_pathways)

            self.assertEqual(3, self.viewmodel.institutes[0].departments[2].number_of_schemes_of_work)
            self.assertEqual(2, self.viewmodel.institutes[0].departments[2].number_of_topics)
            self.assertEqual(10, self.viewmodel.institutes[0].departments[2].number_of_pathways)
