from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_content import ContentModel as Model, ContentDataAccess, handle_log_info

save = Model.save

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

        model = Model(0, "")

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, 99)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, "")
    
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(1, "CPU and RAM")

        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99, published=1)
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "UPDATE sow_content SET description = 'CPU and RAM', letter = '', published = 1 WHERE id = 1;"
                , handle_log_info)

            self.assertEqual(expected_result, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, description="", key_stage_id=20)

        expected_result = ("100", 876)

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99, published = 1)
            
            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "INSERT INTO sow_content (description, letter, key_stage_id, created_by, published) VALUES ('', '', 20, 99, 1);"
                , []
                , handle_log_info)
            
            self.assertEqual(expected_result[1], actual_result.id)


    def test_should_call_execCRUDSql__delete__when__is_new__false__and__published_is_2(self):
        # arrange

        model = Model(23, "")
        
        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99, published=2)

            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "DELETE FROM sow_content WHERE id = 23 AND published IN (0,2);"
                , handle_log_info)

            # check subsequent functions where called

            self.assertEqual(expected_result, actual_result.id)
