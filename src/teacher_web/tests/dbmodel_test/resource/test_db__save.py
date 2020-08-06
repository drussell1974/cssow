from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_resource import ResourceModel as Model

# create test context

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

        model = Model(0, title="How to test an exception", publisher="Unit test",  lesson_id=11, scheme_of_work_id=114)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, auth_user=99)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, title="How to test an exception", publisher="Unit test",  lesson_id=12, scheme_of_work_id=114)
    
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save(self.fake_db, model, auth_user=99)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(23, title="How to make unit tests", publisher="Unit test",  lesson_id=13, scheme_of_work_id=115)
        

        with patch.object(ExecHelper, 'execCRUDSql', return_value=model):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "UPDATE sow_resource SET title = 'How to make unit tests', publisher = 'Unit test', type_id = 0, page_notes = '', url = '', md_document_name = '', is_expired = 0, lesson_id = 13, published = 1 WHERE id = 23;"
             , log_info=handle_log_info)
            
            self.assertEqual(23, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)

            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "INSERT INTO sow_resource (title, publisher, type_id, page_notes, url, md_document_name, is_expired, lesson_id, created, created_by, published) VALUES ('How to make more unit tests', 'Unit test', 0, '', '', 'NULL', 0, 15, '', 0, 1);SELECT LAST_INSERT_ID();"
                , result=[]
                , log_info=handle_log_info)

            self.assertEqual(expected_result, actual_result.id)