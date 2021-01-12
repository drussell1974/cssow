from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_eventlog import EventLogModel as Model, EventLogDataAccess, handle_log_info

delete = Model.delete

class test_db__delete(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete(self.fake_db, 0, 99)


    def test_should_call__delete(self):
        # arrange
        
        expected_result = 2001

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = delete(db=self.fake_db, scheme_of_work_id=69, older_than_n_days=31, auth_user=6079)

            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                "logging__delete"
                , (69, 31, 6079)
                , handle_log_info)

            # check subsequent functions where called

            self.assertEqual(2001, actual_result)
           