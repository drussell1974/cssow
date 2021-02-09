from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_ks123pathway import KS123PathwayModel, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__get_linked_pathway_ks123(TestCase):
    
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
                KS123PathwayModel.get_linked_pathway_ks123(self.fake_db, 87)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KS123PathwayModel.get_linked_pathway_ks123(self.fake_db, 67, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_linked_pathway'
                , (67, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            [34, "Morbi sit amet mauris ut ante porttitor interdum."]
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = KS123PathwayModel.get_linked_pathway_ks123(self.fake_db, 236, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_linked_pathway'
                , (236, mock_auth_user.id)
                , []
                , handle_log_info)
            
            self.assertEqual(1, len(rows))

            self.assertEqual(34, rows[0][0])
            self.assertEqual("Morbi sit amet mauris ut ante porttitor interdum.", rows[0][1])


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            [356, "Morbi sit amet mauris ut ante porttitor interdum."],
            [445, "Curabitur vestibulum ipsum vitae mi iaculis, id dapibus."],
            [777, "Sed blandit fringilla dui et vehicula. Donec sagittis."]
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = KS123PathwayModel.get_linked_pathway_ks123(self.fake_db, 403, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_linked_pathway'
                , (403, mock_auth_user.id)
                , []
                , handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(356, rows[0][0])
            self.assertEqual("Morbi sit amet mauris ut ante porttitor interdum.", rows[0][1])

            self.assertEqual(777, rows[2][0])
            self.assertEqual("Sed blandit fringilla dui et vehicula. Donec sagittis.", rows[2][1])
