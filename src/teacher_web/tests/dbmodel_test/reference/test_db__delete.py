from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

from shared.models.cls_reference import ReferenceModel as Model, ReferenceDataAccess, handle_log_info

# create test context

delete = ReferenceDataAccess.delete

@skip("Deprecated. No longer used.")
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

        model = Model(1, title="How to make more unit tests", publisher="Unit test", scheme_of_work_id=115, reference_type_id=89, year_published=2018)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                delete(self.fake_db, model.id)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = Model(46, title="How to make more unit tests", publisher="Unit test", scheme_of_work_id=115, reference_type_id=89, year_published=2018)

        expected_result = [(1)]

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = delete(self.fake_db, model.id)
            
            # assert
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "DELETE FROM sow_reference WHERE id = 46;"
                , log_info=handle_log_info)
