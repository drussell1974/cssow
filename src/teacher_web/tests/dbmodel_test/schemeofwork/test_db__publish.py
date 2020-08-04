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

        model = SchemeOfWorkModel(0)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                publish_by_id(self.fake_db, 1, 123)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = SchemeOfWorkModel(123)
        
        expected_result = []

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = publish_by_id(self.fake_db, 1, 123)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            #ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
            # "UPDATE sow_scheme_of_work SET name = '', description = '', exam_board_id = 0, key_stage_id = 0, publish_by_ided = 1 WHERE id =  1;", 
            # loghandler)
            
            self.assertEqual(len(expected_result), len(actual_result))

