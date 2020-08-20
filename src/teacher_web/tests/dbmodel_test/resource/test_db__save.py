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

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, auth_user=99)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, title="How to test an exception", publisher="Unit test",  lesson_id=12, scheme_of_work_id=114)
    
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save(self.fake_db, model, auth_user=99)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(23, title="How to make unit tests", publisher="Unit test",  lesson_id=13, scheme_of_work_id=115)
        

        with patch.object(ExecHelper, 'update', return_value=model):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert
            
            ExecHelper.update.assert_called_with(self.fake_db, 
             'lesson_resource__update'
             , (23, 'How to make unit tests', 'Unit test', 0, '', '', '', False, 13, 1, 99)
             , handle_log_info)
            
            self.assertEqual(23, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        expected_result = (102,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)

            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'lesson_resource__insert'
                , (0, 'How to make more unit tests', 'Unit test', 0, '', '', '', False, 15, '', 0, 1, 99)
                , handle_log_info)

            self.assertEqual(102, actual_result.id)