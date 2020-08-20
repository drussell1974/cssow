from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

from shared.models.cls_resource import ResourceModel as Model, handle_log_info

# create test context

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

        model = Model(1, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                delete(self.fake_db, 1, model.id)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = Model(1, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        expected_result = [(1)]

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = delete(self.fake_db, model.id, 6079)
            
            # assert

            ExecHelper.delete.assert_called_with(self.fake_db, 
                'lesson_resource__delete'
                , (1, 6079)
                , handle_log_info)

            self.assertEqual(1, actual_result[0])