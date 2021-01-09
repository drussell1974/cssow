from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.schemesofwork.viewmodels import SchemeOfWorkPublishModelViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from shared.viewmodels.decorators.permissions import TeacherPermissionModel


class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @patch.object(TeacherPermissionModel, 'check_permission', return_value=True)
    def test_should_call_published(self, check_permission):
        
        # arrange
        
        data_to_return = Model(56)
        
        with patch.object(Model, "publish_by_id", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 7839, auth_user=99)

            # assert functions was called
            Model.publish_by_id.assert_called()

    @patch.object(TeacherPermissionModel, 'check_permission', return_value=False)
    def test_should_raise_PermissionError(self, check_permission):
        
        # arrange
        
        db = MagicMock()
        db.cursor = MagicMock()

        # assert
        with self.assertRaises(PermissionError):
            
            # act
            self.viewmodel = ViewModel(db, 7839, auth_user=99)

