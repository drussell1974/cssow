from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.department.viewmodels import DepartmentIndexViewModel as ViewModel
from shared.models.cls_department import DepartmentModel as Model
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch.object(InstituteModel, "get_model", return_value=InstituteModel(534, "Lorum Ipsum", is_from_db=True))
@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
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
        model = Model(56, "Lorum")
        
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

            self.assertEqual("Lorum", self.viewmodel.model[0].name)


    def test_init_called_fetch__multiple_rows(self, mock_auth_user, InstituteModel_get_model):
        
        # arrange
        
        data_to_return = [Model(56, "Tic"),Model(57, "Tac"),Model(58, "Toe")]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, institute_id = 5229, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            InstituteModel_get_model.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))

