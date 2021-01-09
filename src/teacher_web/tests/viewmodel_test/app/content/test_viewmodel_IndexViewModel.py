from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
from tests.viewmodel_test.viewmodel_testcase import ViewModelTestCase

# test context

from app.content.viewmodels import ContentIndexViewModel as ViewModel

#247 used in ViewModel
from shared.models.cls_content import ContentModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.viewmodels.decorators.permissions import TeacherPermissionModel

class test_viewmodel_IndexViewModel(ViewModelTestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass

    def test_init_called_404_if_scheme_of_work_not_found(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=None):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    with self.assertRaises(Http404):
                        self.viewmodel = ViewModel(db, scheme_of_work_id = 999, auth_user=99)

                        # assert functions was called
                        Model.get_all.assert_called()
                        SchemeOfWorkModel.get_options.assert_called()
                        SchemeOfWorkModel.get_model.assert_called()

                        self.assertEqual(0, len(self.viewmodel.model))


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_404_if_scheme_of_work_not_found(self, check_permission):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=None):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    with self.assertRaises(Http404):
                        self.viewmodel = ViewModel(db=db, scheme_of_work_id = 999, auth_user=99)

                        # assert functions was called
                        Model.get_all.assert_called()
                        SchemeOfWorkModel.get_options.assert_called()
                        SchemeOfWorkModel.get_model.assert_called()

                        self.assertEqual(0, len(self.viewmodel.model))


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_fetch__no_return_rows(self, check_permission):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(11, "Test", is_from_db=True)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    self.viewmodel = ViewModel(db=db, scheme_of_work_id=999, auth_user=99)

                    # assert functions was called
                    Model.get_all.assert_called()
                    SchemeOfWorkModel.get_options.assert_called()
                    SchemeOfWorkModel.get_model.assert_called()

                    self.assertEqual(0, len(self.viewmodel.model))
                    self.assertViewModelContent(self.viewmodel, "", "Test", "Curriculum", {})                


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_fetch__single_row(self, check_permission):
        
        # arrange
        
        data_to_return = [Model(56,"", "")]

        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(11, "Test", is_from_db=True)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    self.viewmodel = ViewModel(db=db, scheme_of_work_id=101, auth_user=99)

                    # assert functions was called
                    Model.get_all.assert_called()
                    SchemeOfWorkModel.get_options.assert_called()
                    SchemeOfWorkModel.get_model.assert_called()
                    
                    self.assertEqual(1, len(self.viewmodel.model))                    
                    self.assertViewModelContent(self.viewmodel, "", "Test", "Curriculum", {})                


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_init_called_fetch__multiple_rows(self, check_permission):
        
        # arrange
        
        data_to_return = [Model(56,"", ""),Model(57,"", ""),Model(58,"", "")]
 
        with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")]):
            with patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(11, "Test", is_from_db=True)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    self.viewmodel = ViewModel(db=db, scheme_of_work_id=103, auth_user=99)

                    # assert functions was called
                    Model.get_all.assert_called()
                    SchemeOfWorkModel.get_options.assert_called()
                    SchemeOfWorkModel.get_model.assert_called()

                    self.assertEqual(3, len(self.viewmodel.model))
                    self.assertViewModelContent(self.viewmodel, "", "Test", "Curriculum", {})                



    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_init_raises_PermissionError(self, check_permission):
        
        # arrange
        
        data_to_return = [Model(56,"", ""),Model(57,"", ""),Model(58,"", "")]
 
        db = MagicMock()
        db.cursor = MagicMock()

        with self.assertRaises(PermissionError):
            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id = 103, auth_user=99)
