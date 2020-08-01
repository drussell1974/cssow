from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.schemesofwork.viewmodels import SchemeOfWorkPublishModelViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkDataAccess as DataAccess, SchemeOfWorkModel as Model


class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_should_call_published(self):
        
        # arrange
        
        data_to_return = Model(56)
        
        with patch.object(DataAccess, "publish", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 7839, auth_user=99)

            # assert functions was called
            DataAccess.publish.assert_called()
