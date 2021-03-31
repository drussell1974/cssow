from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel
from shared.models.cls_ks123pathway import KS123PathwayModel, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_all(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(KeyError):
                KS123PathwayModel.get_all(self.fake_db, mock_auth_user.department_id, auth_ctx=mock_auth_user)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = KS123PathwayModel.get_all(self.fake_db, department_id=mock_auth_user.department_id, auth_ctx=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_all'
                , (mock_auth_user.department_id, 1, mock_auth_user.auth_user_id) 
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(actual_results))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (702, "Fringilla purus lacus, ut volutpat nibh euismod.", 10, "Year 10", 2, "Algorithms")
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KS123PathwayModel.get_all(self.fake_db, department_id=mock_auth_user.department_id, auth_ctx=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_all'
                , (mock_auth_user.department_id, 1, mock_auth_user.auth_user_id) 
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla purus lacus, ut volutpat nibh euismod.", actual_results[0].objective)
            self.assertEqual(10, actual_results[0].year_id)
            self.assertEqual(2, actual_results[0].topic_id)


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (1021, "Vestibulum nec arcu nec dolor vehicula ornare non.", 10, "Year 10", 1, "Hardware"),
            (1022, "Fringilla purus lacus, ut volutpat nibh euismod.", 10, "Year 10", 2, "Algorithms"),
            (1023, "Phasellus rutrum lorem a arcu ultrices, id mollis", 11, "Year 11", 2, "Algorithms")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KS123PathwayModel.get_all(self.fake_db, department_id=mock_auth_user.department_id, auth_ctx=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_all'
                , (mock_auth_user.department_id, 1, mock_auth_user.auth_user_id) 
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual("Vestibulum nec arcu nec dolor vehicula ornare non.", actual_results[0].objective)
            self.assertEqual("Year 10", actual_results[0].year.name)
            self.assertEqual("Hardware", actual_results[0].topic.name)
            self.assertEqual(STATE.PUBLISH, actual_results[0].published)


            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual("Phasellus rutrum lorem a arcu ultrices, id mollis", actual_results[2].objective)
            self.assertEqual("Year 11", actual_results[2].year.name)
            self.assertEqual("Algorithms", actual_results[2].topic.name)
            self.assertEqual(STATE.PUBLISH, actual_results[2].published)
