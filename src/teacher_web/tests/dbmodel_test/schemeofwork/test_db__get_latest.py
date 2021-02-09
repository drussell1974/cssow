from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel, handle_log_info

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(9999, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__get_latest_schemes_of_work(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, auth_user_model):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkModel.get_latest_schemes_of_work(self.fake_db, 4, auth_user=auth_user_model)


    def test__should_call__select__return_no_items(self, auth_user_model):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = SchemeOfWorkModel.get_latest_schemes_of_work(self.fake_db, 4, auth_user=auth_user_model)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_latest"
                , (4, auth_user_model.id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call__select__return_single_item(self, auth_user_model):
        # arrange
        expected_result = [(6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = SchemeOfWorkModel.get_latest_schemes_of_work(self.fake_db, 3, auth_user=auth_user_model)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_latest"
                , (3, auth_user_model.id)
                , []
                , handle_log_info)
                
            self.assertEqual(1, len(rows))
            self.assertEqual(6, rows[0].id)
            self.assertEqual("Lorem", rows[0].name)
            self.assertEqual("ipsum dolor sit amet.", rows[0].description)



    def test__should_call__select__return_multiple_item(self, auth_user_model):
        # arrange

        expected_result = [
            (6, "Lorem", "ipsum dolor sit amet.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1),
            (7, "Phasellus", "ultricies orci sed tempus.", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1),
            (8, "Nulla", "Tristique pharetra nisi. Sed", 4, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 1)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = SchemeOfWorkModel.get_latest_schemes_of_work(self.fake_db, 3, auth_user=auth_user_model)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_latest"
                , (3, auth_user_model.id)
                , []
                , handle_log_info)
                
            self.assertEqual(3, len(rows))

            self.assertEqual(6, rows[0].id)
            self.assertEqual("Lorem", rows[0].name)
            self.assertEqual("ipsum dolor sit amet.", rows[0].description)

            self.assertEqual(8, rows[2].id)
            self.assertEqual("Nulla", rows[2].name)
            self.assertEqual("Tristique pharetra nisi. Sed", rows[2].description)
