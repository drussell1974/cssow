from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_content import ContentModel as Model, handle_log_info


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
                Model.get_model(self.fake_db,  scheme_of_work_id=54, auth_user=4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = Model.get_model(self.fake_db, 99, scheme_of_work_id=54, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'content__get'
                , (99, 54, 6079)
                , []
                , handle_log_info)

            self.assertIsNone(actual_result)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(6, "Lorem", "A", 1)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            model = Model.get_model(self.fake_db, 6, scheme_of_work_id=30, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'content__get'
                , (6, 30, 6079)
                , []
                , handle_log_info)

            self.assertEqual(6, model.id)
            self.assertEqual("Lorem", model.description)
            self.assertEqual("A", model.letter_prefix)
            self.assertFalse(model.is_new())
            self.assertTrue(model.is_from_db)



