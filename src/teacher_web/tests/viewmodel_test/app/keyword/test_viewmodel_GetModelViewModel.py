from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
from app.keywords.viewmodels import KeywordGetModelViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_viewmodel_KeywordGetModelViewModel(TestCase):
    
    fake_schemeofwork = SchemeOfWorkModel(22)
    fake_schemeofwork.is_from_db = True

    def setUp(self):                       
        pass
        

    def tearDown(self):
        pass


    @patch.object(SchemeOfWorkModel, "get_model", return_value=fake_schemeofwork)
    def test_init_called_fetch__no_return_rows(self, SchemeOfWorkModel__get_model, mock_auth_user):
        
        # arrange


        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()


            with self.assertRaises(Http404):

                # act
                self.viewmodel = ViewModel(db=db, scheme_of_work_id=22, keyword_id=33, auth_user=mock_auth_user)

                # assert functions was called
                Model.get_model.assert_not_called()
                self.assertIsNone(self.viewmodel.model)



    @patch.object(SchemeOfWorkModel, "get_model", return_value=fake_schemeofwork)
    def test_init_called_fetch__return_item(self, SchemeOfWorkModel__get_model, mock_auth_user):
        
        # arrange
        data_to_return = Model(101, "Abstraction")
        data_to_return.is_from_db = True
    
        fake_schemeofwork = SchemeOfWorkModel(22)
        fake_schemeofwork.is_from_db = True

        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=23, keyword_id=101, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(101, self.viewmodel.model.id)
            self.assertEqual("Abstraction", self.viewmodel.model.term)
