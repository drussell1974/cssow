from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel, SchemeOfWorkModel

delete_unpublished = SchemeOfWorkModel.delete_unpublished


class test_db__deleteunpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = SchemeOfWorkModel(0)

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete_unpublished(self.fake_db, 1)


    def test_should_call__delete(self):
         # arrange

        with patch.object(ExecHelper, 'delete', return_value=(5)):
            # act

            actual_result = delete_unpublished(self.fake_db, auth_user=6079)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db,
                'scheme_of_work__delete_unpublished'
                , (0, 6079)
                , handle_log_info)

            self.assertEqual(5, actual_result)
