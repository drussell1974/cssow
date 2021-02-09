from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel
from shared.models.cls_keyword import KeywordModel, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
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

            with self.assertRaises(Exception):
                KeywordModel.get_all(self.fake_db)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeywordModel.get_all(self.fake_db, 13, 0, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.id) 
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13, 2)
            ]

        with patch.object(LessonModel, 'get_by_keyword', return_value=[]):
            with patch.object(ExecHelper, 'select', return_value=expected_result):
                # act

                actual_results = KeywordModel.get_all(self.fake_db, 13, 0, mock_auth_user)
                
                # assert

                ExecHelper.select.assert_called_with(self.fake_db,
                    'scheme_of_work__get_all_keywords'
                    , (13, mock_auth_user.id) 
                    , []
                    , handle_log_info)
                    

                self.assertEqual(1, len(actual_results))

                self.assertEqual(702, actual_results[0].id)
                self.assertEqual("Fringilla", actual_results[0].term),
                self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)
                self.assertEqual(2, actual_results[0].published)
            
                LessonModel.get_by_keyword.assert_not_called()
                self.assertEqual([], actual_results[0].belongs_to_lessons)


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (1021, "Vestibulum", "nec arcu nec dolor vehicula ornare non.", 13, 2),
            (1022, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13, 0),
            (1023, "Phasellus", "rutrum lorem a arcu ultrices, id mollis", 13, 1)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KeywordModel.get_all(self.fake_db, 13, 0, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual("Vestibulum", actual_results[0].term),
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].definition)
            self.assertEqual(2, actual_results[0].published)


            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual("Phasellus", actual_results[2].term),
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[2].definition)
            self.assertEqual(1, actual_results[2].published)



    def test__should_call_get_by_keyword__when__get_lesson_is_true(self, mock_auth_user):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13, 2)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KeywordModel.get_all(self.fake_db, 13, 0, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.id) 
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla", actual_results[0].term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)
            self.assertEqual(2, actual_results[0].published)


    def test__should_call_select__with_empty_search_term(self, mock_auth_user):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13, 1)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KeywordModel.get_all(self.fake_db, 13, 0, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla", actual_results[0].term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)
            self.assertEqual(1, actual_results[0].published)


    def test__should_call_select__with_default_search_term(self, mock_auth_user):
        # arrange
        expected_result = [
            (21, "Phasellus", "rutrum lorem a arcu ultrices, id mollis", 13, 1),
            (22, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13, 1),
            (23, "Vestibulum", "nec arcu nec dolor vehicula ornare non.", 13, 1)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KeywordModel.get_all(self.fake_db, 13, 0, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(21, actual_results[0].id)
            self.assertEqual("Phasellus", actual_results[0].term),
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[0].definition)
            self.assertEqual(13, actual_results[0].scheme_of_work_id)
            self.assertEqual(1, actual_results[0].published)

            self.assertEqual(23, actual_results[2].id)
            self.assertEqual("Vestibulum", actual_results[2].term),
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[2].definition)
            self.assertEqual(13, actual_results[2].scheme_of_work_id)
            self.assertEqual(1, actual_results[2].published)



    def test__should_call_select__with_entered_search_term(self, mock_auth_user):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13, 0)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KeywordModel.get_all(self.fake_db, 13, 0, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla", actual_results[0].term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)
            self.assertEqual(13, actual_results[0].scheme_of_work_id)
            self.assertEqual(0, actual_results[0].published)
