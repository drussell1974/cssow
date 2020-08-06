from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_reference import ReferenceDataAccess, handle_log_info

get_options = ReferenceDataAccess.get_options

@skip("Deprecated. No longer used")
class test_db__get_options(TestCase):
    
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
                get_options(self.fake_db, 21, auth_user=1)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db, 21, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT ref.id as id, ref.reference_type_id as reference_type_id, type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_reference_type as type ON type.id = ref.reference_type_id WHERE ref.scheme_of_work_id = 21 AND (ref.published = 1 OR ref.created_by = 1);"
            , [])

            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (4345, 40, "Markdown", "Writing Mock Unit Tests", "Dave Russell", 2020, "", "http://daverussell.co.uk", 12)
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db, 21, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT ref.id as id, ref.reference_type_id as reference_type_id, type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_reference_type as type ON type.id = ref.reference_type_id WHERE ref.scheme_of_work_id = 21 AND (ref.published = 1 OR ref.created_by = 1);"
            , [])
            
            self.assertEqual(1, len(rows))

            self.assertEqual(4345, rows[0].id)
            self.assertEqual("Writing Mock Unit Tests", rows[0].title)
            self.assertEqual("Markdown", rows[0].reference_type_name)
            self.assertEqual("Dave Russell", rows[0].publisher)
            self.assertEqual("http://daverussell.co.uk", rows[0].uri)



    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (934, 40, "Accumsan", "Vivamus sodales enim cursus ex.", "Liquet pretium", 1988, "", "http://acme.co.uk", 12),
            (666, 40, "Vivamus", "Praesent tempus facilisis pharetra.", "Mi, Posuere", 2005, "", "http://horsefair.org", 12),
            (37, 40, "Praesent", "Praesent vulputate, tortor et accumsan", "Nulla Torotor", 2020, "", "http://handles.net", 12)
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db, 21, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT ref.id as id, ref.reference_type_id as reference_type_id, type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_reference_type as type ON type.id = ref.reference_type_id WHERE ref.scheme_of_work_id = 21 AND (ref.published = 1 OR ref.created_by = 1);"
            , [])
            
            self.assertEqual(3, len(rows))

            self.assertEqual(934, rows[0].id)
            self.assertEqual("Vivamus sodales enim cursus ex.", rows[0].title)
            self.assertEqual("Accumsan", rows[0].reference_type_name)
            self.assertEqual("Liquet pretium", rows[0].publisher)
            self.assertEqual("http://acme.co.uk", rows[0].uri)


            self.assertEqual(37, rows[2].id)
            self.assertEqual("Praesent vulputate, tortor et accumsan", rows[2].title)
            self.assertEqual("Praesent", rows[2].reference_type_name)
            self.assertEqual("Nulla Torotor", rows[2].publisher)
            self.assertEqual("http://handles.net", rows[2].uri)