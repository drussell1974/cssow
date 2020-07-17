from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel, delete_unpublished


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

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete_unpublished(self.fake_db, 1)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = SchemeOfWorkModel(1)
        
        expected_result = 5

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_result = delete_unpublished(self.fake_db, 1)
            
            # assert
            ExecHelper.execSql.assert_called()

            #ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
            # "UPDATE sow_scheme_of_work SET name = '', description = '', exam_board_id = 0, key_stage_id = 0, published = 1 WHERE id =  1;", 
            # loghandler)

            self.assertEqual(expected_result, actual_result)
