from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__get_options(TestCase):
    
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
                LessonModel.get_options(self.fake_db, 21, auth_user=1)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = LessonModel.get_options(self.fake_db, 21, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_options'
                , (21, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(87, "Praesent tempus facilisis pharetra. Pellentesque.", 1, 92, "Garden Peas", 10,"Yr10")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = LessonModel.get_options(self.fake_db, 12, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_options'
                , (12, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows))

            self.assertEqual(87, rows[0].id)
            self.assertEqual("Praesent tempus facilisis pharetra. Pellentesque.", rows[0].title)
            self.assertEqual(1, rows[0].order_of_delivery_id)
            self.assertEqual("Garden Peas", rows[0].topic_name)
            self.assertEqual("Yr10", rows[0].year_name)



    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (834, "Vivamus sodales enim cursus ex.", 1, 95, "Runner Beans", 10,"Yr7"),
            (835, "Praesent tempus facilisis pharetra. Pellentesque.", 2, 96, "Mushrooms", 10,"Yr8"),
            (836, "Praesent vulputate, tortor et accumsan.", 3, 97, "Radish", 10,"Yr9"),
        ]


        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = LessonModel.get_options(self.fake_db, 214, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_options'
                , (214, mock_auth_user.id)
                , []
                , handle_log_info)
            
            self.assertEqual(834, rows[0].id)
            self.assertEqual("Vivamus sodales enim cursus ex.", rows[0].title)
            self.assertEqual(1, rows[0].order_of_delivery_id)
            self.assertEqual("Runner Beans", rows[0].topic_name)
            self.assertEqual("Yr7", rows[0].year_name)

            self.assertEqual(836, rows[2].id)
            self.assertEqual("Praesent vulputate, tortor et accumsan.", rows[2].title)
            self.assertEqual(3, rows[2].order_of_delivery_id)
            self.assertEqual("Radish", rows[2].topic_name)
            self.assertEqual("Yr9", rows[2].year_name)
