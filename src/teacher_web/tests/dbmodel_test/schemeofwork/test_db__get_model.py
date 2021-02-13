from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_model(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkModel.get_model(self.fake_db, 4)


    def test__should_call__select__return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            model = SchemeOfWorkModel.get_model(self.fake_db, 99, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get"
                , (99, mock_ctx.user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, model.id)
            self.assertEqual("", model.description)
            self.assertTrue(model.is_new())
            self.assertFalse(model.is_from_db)


    def test__should_call__select__return_single_item(self, mock_ctx):
        # arrange
        expected_result = [(6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", 56, "", "2020-07-21 17:09:34", 1, "test_user", 1)]

        SchemeOfWorkModel.get_number_of_learning_objectives = Mock(return_value=[(253,)])
        SchemeOfWorkModel.get_number_of_resources = Mock(return_value=[(20,)])
        SchemeOfWorkModel.get_number_of_lessons = Mock(return_value=[(40,)])
        SchemeOfWorkModel.get_all_keywords = Mock(return_value=[(112,)])
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            model = SchemeOfWorkModel.get_model(self.fake_db, 6, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get"
                , (6, mock_ctx.user_id)
                , []
                , handle_log_info)
                 
            self.assertEqual(6, model.id)
            self.assertEqual("Lorem", model.name)
            self.assertEqual("ipsum dolor sit amet.", model.description)
            self.assertEqual(56, model.department_id)
            self.assertEqual("", model.department_name)
            self.assertFalse(model.is_new())
            self.assertTrue(model.is_from_db)



