from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.schemesofwork.viewmodels import SchemeOfWorkIndexViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.decorators.permissions import TeacherPermissionModel


class test_viewmodel_IndexViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @patch.object(TeacherPermissionModel, 'check_permission', return_value=True)
    def test_init_called_fetch__no_return_rows(self, check_permission):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    @patch.object(TeacherPermissionModel, 'check_permission', return_value=True)
    def test_init_called_fetch__single_row(self, check_permission):
        
        # arrange
        model = Model(56, "Lorum")
        model.key_words = [KeywordModel(), KeywordModel()]

        data_to_return = [model]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))

            self.assertEqual("Lorum", self.viewmodel.model[0].name)
            self.assertEqual(2, len(self.viewmodel.model[0].key_words))


    @patch.object(TeacherPermissionModel, 'check_permission', return_value=True)
    def test_init_called_fetch__multiple_rows(self, check_permission):
        
        # arrange
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))

