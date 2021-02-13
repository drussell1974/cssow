from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_all(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(KeyError):
                Model.get_all(self.fake_db, 4, scheme_of_work_id=30, auth_user=mock_ctx)


    def test__should_call_select__return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = Model.get_all(self.fake_db, lesson_id=5, scheme_of_work_id=30, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson_learning_objective__get_all"
                , (5, 30, mock_ctx.user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_ctx):
        # arrange
        expected_result = [(
            934, "Sed at arcu in leo vestibulum dapibus. Suspendisse",
            1, "Prestructural", 1,  34,
            "Nullam dapibus leo vitae imperdiet mollis.",
            4, "KS4",
            12, "Vivamus rutrum viverra lorem",
            "malesuada,sapien,condimentum", "Ut consequat mi purus, ut placerat libero tempus.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user", 1
        )]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = Model.get_all(self.fake_db, lesson_id=3, scheme_of_work_id=30, auth_user=mock_ctx)
            
            # assert
            
            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson_learning_objective__get_all"
                , (3, 30, mock_ctx.user_id)
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(934, actual_results[0]["id"])
            self.assertEqual("Sed at arcu in leo vestibulum dapibus. Suspendisse", actual_results[0]["description"])
            self.assertEqual("Prestructural", actual_results[0]["solo_taxonomy_name"])
            self.assertEqual("Nullam dapibus leo vitae imperdiet mollis.", actual_results[0]["content_description"])


    def test__should_call_select__return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [(
            934, "Etiam eu efficitur ante. Nunc justo turpis, finibus.",
            1, "Unistructural", 1,  34,
            "Donec mattis sed eros ac eleifend.",
            4, "KS4",
            12, "Morbi volutpat justo quis",
            "ligula,pretium congue,vestibulum", "Sed egestas, ligula eu tempus sollicitudin, lectus velit.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user", 0
        ),
        (
            935, "Sed at arcu in leo vestibulum dapibus. Suspendisse",
            3, "Multistructural", 1,  34,
            "Nullam dapibus leo vitae imperdiet mollis.",
            4, "KS4",
            12, "Vivamus rutrum viverra lorem",
            "malesuada,sapien,condimentum", "Ut consequat mi purus, ut placerat libero tempus.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user", 0
        ),
        (
            936, "Sed consectetur nulla ut venenatis dignissim. Sed dictum.",
            4, "Relational", 1,  34,
            "Donec ut condimentum risus.",
            4, "KS4",
            12, " Maecenas tincidunt tempus arcu.",
            "Nulla,molestie,magna purus", "A dapibus enim lobortis.",
            "Consequat tempus.", 1, "2020-07-17 16:24:04", 99, "test_user", 1
        )]


        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = Model.get_all(self.fake_db, lesson_id=20, scheme_of_work_id=30, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                 "lesson_learning_objective__get_all"
                 , (20,30,mock_ctx.user_id)
                 , []
                 , handle_log_info)

            self.assertEqual(3, len(actual_results))


            self.assertEqual(934, actual_results[0]["id"])
            self.assertEqual("Etiam eu efficitur ante. Nunc justo turpis, finibus.", actual_results[0]["description"])
            self.assertEqual("Unistructural", actual_results[0]["solo_taxonomy_name"])
            self.assertEqual("Donec mattis sed eros ac eleifend.", actual_results[0]["content_description"])

            self.assertEqual(936, actual_results[2]["id"])
            self.assertEqual("Sed consectetur nulla ut venenatis dignissim. Sed dictum.", actual_results[2]["description"])
            self.assertEqual("Relational", actual_results[2]["solo_taxonomy_name"])
            self.assertEqual("Donec ut condimentum risus.", actual_results[2]["content_description"])

