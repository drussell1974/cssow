from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, handle_log_info 

# TODO: #329 - remove global references
get_ks123_pathway_objective_ids = LessonModel.get_ks123_pathway_objective_ids


from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__get_ks123_pathway_ids(TestCase):
    
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

            with self.assertRaises(Exception):
                get_ks123_pathway_objective_ids(self.fake_db, 21)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_ks123_pathway_objective_ids(self.fake_db, 67, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_ks123_pathway_objective_ids'
                , (67, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [("87",)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_ks123_pathway_objective_ids(self.fake_db, 87, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_ks123_pathway_objective_ids'
                , (87, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(87, actual_results[0])


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [("1034",),("1045",),("12",)]


        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_ks123_pathway_objective_ids(self.fake_db, 21, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_ks123_pathway_objective_ids'
                , (21, mock_auth_user.id)
                , []
                , handle_log_info)
            
            self.assertEqual(1034, actual_results[0])
            self.assertEqual(12, actual_results[2])
