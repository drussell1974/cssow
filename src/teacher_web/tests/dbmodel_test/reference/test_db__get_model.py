from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_reference import ReferenceDataAccess, handle_log_info

# test context

get_model = ReferenceDataAccess.get_model

@skip("Deprecated. No longer used.")
class test_db__get_model(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_model(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_results = get_model(self.fake_db, 99, scheme_of_work_id=874, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT ref.id as id, ref.reference_type_id as reference_type_id,  ref_type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_reference_type as ref_type ON ref_type.id = ref.reference_type_id WHERE ref.id = 99 AND (ref.published = 1 OR ref.created_by = 1);"
                , []
                , log_info=handle_log_info)

            self.assertTrue(actual_results.is_new())


    def test__should_call_execSql_return_single_item(self):
        # arrange

        expected_result = [(
            342, #id_=row, 
            34, #reference_type_id = row[1], 
            "Book", #reference_type_name = row[2], 
            "How Computers Represent Data", #title=row[3], 
            "Phiadon", #publisher=row[4], 
            1998, #year_published=row[5],
            "Sue Sentance", #authors=row[6], 
            "https://www.acme.net", #uri=row[7]
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 321, scheme_of_work_id=874, auth_user=1)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT ref.id as id, ref.reference_type_id as reference_type_id,  ref_type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_reference_type as ref_type ON ref_type.id = ref.reference_type_id WHERE ref.id = 321 AND (ref.published = 1 OR ref.created_by = 1);"
                , []
                , log_info=handle_log_info)
        

            self.assertEqual(342, actual_results.id)
            self.assertEqual(34, actual_results.reference_type_id),
            self.assertEqual("Book", actual_results.reference_type_name),
            self.assertEqual("How Computers Represent Data", actual_results.title),
            self.assertEqual("Phiadon", actual_results.publisher),
            self.assertEqual("Sue Sentance", actual_results.authors),
            self.assertEqual("https://www.acme.net", actual_results.uri)




