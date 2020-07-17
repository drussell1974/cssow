from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

import shared.models.cls_resource as test_context 

# create test context

delete = test_context.delete
handle_log_info = test_context.handle_log_info
Model = test_context.ResourceModel

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

        model = Model(1, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                delete(self.fake_db, 1, model.id)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = Model(1, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        expected_result = [(1)]

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = delete(self.fake_db, 1, model.id)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            #ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
            # "UPDATE sow_scheme_of_work SET name = '', description = '', exam_board_id = 0, key_stage_id = 0, published = 1 WHERE id =  1;", 
            # loghandler)
            self.assertEqual(expected_result, actual_result)