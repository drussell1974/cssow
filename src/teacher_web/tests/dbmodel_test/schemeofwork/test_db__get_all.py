from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel, SchemeOfWorkDataAccess, handle_log_info
from shared.models.cls_keyword import KeywordModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model


class test_db__get_all(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.close = Mock()
        self.fake_db.cursor = Mock()
        self.fake_db.cursor.close = Mock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkModel.get_all(self.fake_db, 99, key_stage_id=4)


    def test__should_call__select__return_no_items(self):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = SchemeOfWorkModel.get_all(self.fake_db, fake_ctx, key_stage_id=5)
            
            # assert
            ExecHelper.select.assert_called_with(
                self.fake_db,
                'scheme_of_work__get_all$2'
                , (5, 67, 127671276711, int(STATE.PUBLISH_INTERNAL), fake_ctx.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call__select__return_single_item(self):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = [(6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", 56, 2, "2020-07-21 17:09:34", 1, "test_user", 1, 2, 10)]

        SchemeOfWorkModel.get_number_of_lessons = Mock(return_value=[(66,)])
        SchemeOfWorkModel.get_number_of_learning_objectives = Mock(return_value=[(253,)])
        SchemeOfWorkModel.get_number_of_resources = Mock(return_value=[(20,)])
        SchemeOfWorkModel.get_all_keywords = Mock(return_value=[KeywordModel(), KeywordModel()])

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            rows = SchemeOfWorkModel.get_all(self.fake_db, fake_ctx, key_stage_id=3)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all$2'
                , (3, 67, 127671276711, int(STATE.PUBLISH_INTERNAL), fake_ctx.auth_user_id)
                , []
                , handle_log_info)

            SchemeOfWorkModel.get_number_of_lessons.assert_called()
            SchemeOfWorkModel.get_number_of_learning_objectives.assert_called()
            SchemeOfWorkModel.get_number_of_resources.assert_called()
            SchemeOfWorkModel.get_all_keywords.assert_called()

            self.assertEqual(1, len(rows))
            self.assertEqual(6, rows[0]["id"])
            self.assertEqual("Lorem", rows[0]["name"])
            self.assertEqual("ipsum dolor sit amet.", rows[0]["description"])
            self.assertEqual(4, rows[0]["exam_board_id"])
            self.assertEqual("AQA", rows[0]["exam_board_name"])
            self.assertEqual(4, rows[0]["key_stage_id"])
            self.assertEqual("KS4", rows[0]["key_stage_name"])
            self.assertEqual(56, rows[0]["department_id"])
            self.assertEqual(2, rows[0]["institute_id"])
            self.assertEqual("2020-07-21 17:09:34", rows[0]["created"])
            self.assertEqual(1, rows[0]["created_by_id"])
            self.assertEqual(1, rows[0]["published"])
            self.assertEqual(2, rows[0]["study_duration"])
            self.assertEqual(10, rows[0]["start_study_in_year"])



    def test__should_call__select__return_multiple_item(self):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = [
            (6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", 54, 2, "2020-07-21 17:09:34", 1, "test_user", 1, 2, 10),
            (7, "Phasellus", "ultricies orci sed tempus.", 4, "AQA", 4, "KS4", 56, 2, "2020-07-21 17:09:34", 1, "test_user", 1, 2, 10),
            (8, "Nulla", "Tristique pharetra nisi. Sed", 4, "AQA",  4, "KS4", 56, 2, "2020-07-21 17:09:34", 1, "test_user", 1, 3, 9)]

        SchemeOfWorkModel.get_number_of_lessons = Mock(return_value=[(66,)])
        SchemeOfWorkModel.get_number_of_learning_objectives = Mock(return_value=[(253,)])
        SchemeOfWorkModel.get_number_of_resources = Mock(return_value=[(20,)])
        SchemeOfWorkModel.get_all_keywords = Mock(return_value=[KeywordModel(), KeywordModel()])

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = SchemeOfWorkModel.get_all(self.fake_db, fake_ctx, key_stage_id=3)
            
            # assert

            ExecHelper.select.assert_called_with(
                self.fake_db,
                'scheme_of_work__get_all$2'
                , (3, 67, 127671276711, int(STATE.PUBLISH_INTERNAL), fake_ctx.auth_user_id)
                , []
                , handle_log_info)

            SchemeOfWorkModel.get_number_of_lessons.assert_called()
            SchemeOfWorkModel.get_number_of_learning_objectives.assert_called()
            SchemeOfWorkModel.get_number_of_resources.assert_called()
            SchemeOfWorkModel.get_all_keywords.assert_called()

            self.assertEqual(3, len(rows))

            self.assertEqual(6, rows[0]["id"])
            self.assertEqual("Lorem", rows[0]["name"])
            self.assertEqual("ipsum dolor sit amet.", rows[0]["description"])

            self.assertEqual(8, rows[2]["id"])
            self.assertEqual("Nulla", rows[2]["name"])
            self.assertEqual("Tristique pharetra nisi. Sed", rows[2]["description"])
            self.assertEqual(9, rows[2]["start_study_in_year"])
            self.assertEqual(3, rows[2]["study_duration"])
