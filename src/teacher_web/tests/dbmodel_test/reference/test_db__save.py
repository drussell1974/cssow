from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_reference import ReferenceModel as Model, ReferenceDataAccess, handle_log_info

save = ReferenceDataAccess.save

@skip("Deprecated. No longer used.")
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

        model = Model(0, title="How to test an exception", publisher="Unit test",  scheme_of_work_id=114, reference_type_id=7, year_published=1943)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, title="How to test an exception", publisher="Unit test", scheme_of_work_id=87, reference_type_id=89, year_published=2018)
    
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(1, title="How to make unit tests", publisher="Unit test", scheme_of_work_id=115, reference_type_id=89, year_published=2018)
        
        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "UPDATE sow_reference SET reference_type_id = 89, title = 'How to make unit tests', authors = '', publisher = 'Unit test', year_published = 2018, url = '', scheme_of_work_id = 115 WHERE id = 1;"
             , log_info=handle_log_info)
            
            self.assertEqual(expected_result, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, title="How to make more unit tests", publisher="Unit test",  scheme_of_work_id=115, reference_type_id=89, year_published=2018)
        
        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)

            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "INSERT INTO sow_reference (reference_type_id, title, authors, publisher, year_published, url, scheme_of_work_id, created, created_by) VALUES (89, 'How to make more unit tests', '', 'Unit test', 2018, '', 115, '', 0);"
                , log_info=handle_log_info)

            self.assertEqual(expected_result, actual_result.id)