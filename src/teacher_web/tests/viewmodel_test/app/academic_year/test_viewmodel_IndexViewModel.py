from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.department.viewmodels import DepartmentAllViewModel as ViewModel
from shared.models.cls_department import DepartmentModel as Model
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_institute import InstituteModel
from tests.test_helpers.mocks import *

@patch.object(InstituteModel, "get_model", return_value=InstituteModel(534, "Lorum Ipsum", is_from_db=True))
@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_IndexViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_auth_user, InstituteModel_get_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, institute_id=99, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            InstituteModel_get_model.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self, mock_auth_user, InstituteModel_get_model):
        
        # arrange
        fake_institute = InstituteModel(12767111276711, "Ipsum")
        model = Model(2020, "2020-09-01", "2021-07-15", is_from_db=True)
        
        data_to_return = [model]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, institute_id=56, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            InstituteModel_get_model.assert_called()

            self.assertEqual(1, len(self.viewmodel.model))

            self.assertEqual("2020-09-01", self.viewmodel.model[0].display_name)


    def test_init_called_fetch__multiple_rows(self, mock_auth_user, InstituteModel_get_model):
        
        # arrange
        fake_institute = InstituteModel(12767111276711, "Ipsum")
        data_to_return = [
            Model(2019, "2019-09-03", "2020-07-13", is_from_db=True),
            Model(2020, "2020-09-01", "2021-07-06", is_from_db=True),
            Model(2021, "2021-09-02", "2022-07-21", is_from_db=True)
        ]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, institute_id = fake_institute.id, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            InstituteModel_get_model.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))

            self.assertEqual("2019-09-03", self.viewmodel.model[0].display_name)

            self.assertEqual("2021-09-02", self.viewmodel.model[2].display_name)
