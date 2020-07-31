from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
import shared.models.cls_schemeofwork as test_context

# create test context

save = test_context.SchemeOfWorkDataAccess.save
handle_log_info = test_context.handle_log_info
Model = test_context.SchemeOfWorkModel


class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1)
    
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(89)
        

        with patch.object(ExecHelper, 'execCRUDSql', return_value=model):
            # act

            actual_result = save(self.fake_db, model)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            #ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
            # "UPDATE sow_scheme_of_work SET name = '', description = '', exam_board_id = 0, key_stage_id = 0, published = 1 WHERE id =  1;", 
            # log_info=handle_log_info)
            
            self.assertEqual(89, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0)


        with patch.object(ExecHelper, 'execCRUDSql', return_value=([], 101)):
            # act

            actual_result = save(self.fake_db, model)

            # assert

            ExecHelper.execCRUDSql.assert_called()
            #ExecHelper.execCRUDSql.assert_called_with(
            #    self.fake_db, 
            #    "INSERT INTO sow_scheme_of_work (name, description, exam_board_id, key_stage_id, created, created_by, published) VALUES ('', '', 0, 0, '', 0, 1);SELECT LAST_INSERT_ID();", [], 
            #    log_info=handle_log_info)

            self.assertEqual(101, actual_result.id)