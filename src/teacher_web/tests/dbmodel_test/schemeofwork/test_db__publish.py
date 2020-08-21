from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel

publish_by_id = SchemeOfWorkModel.publish_by_id


class test_db__publish_by_id(TestCase):


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

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                publish_by_id(self.fake_db, 1, 123)


    def test_should_call_update(self):
        # arrange
        
        expected_result = [(1,)]

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = publish_by_id(self.fake_db, 1, 123)
            
            # assert
            ExecHelper.update.assert_called_with(self.fake_db,
                "scheme_of_work__publish"
                , (1, 1, 123)
                , handle_log_info)
            
            self.assertEqual(1, len(actual_result))

