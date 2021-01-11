from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.lesson_keywords.viewmodels import LessonKeywordSelectViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_teacher_permission import TeacherPermissionModel


class test_viewmodel_SelectViewModel_execute(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()


    def tearDown(self):
        pass


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_not_called_save__with_exception__when_invaid_type(self, check_permission):
        """ ViewModel does not process new instance """

        # arrange
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "POST"
        )
        
        test_context = ViewModel(db=db, request=mock_request, scheme_of_work_id=22, lesson_id=45, auth_user=6079)
        
        with self.assertRaises(AttributeError):
            # act
            test_context.execute(99)

    @skip("not implemented")
    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_called_save__with_exception(self, check_permission):

        # arrange
        
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "POST"    
        )
        mock_request.POST = Mock({
                    "scheme_of_work_id": 5,
                    "lesson_id": 230
                })

        mock_request.POST.getlist = MagicMock(returns_value=[1,2,3])
        
        test_context = ViewModel(db=db, request=mock_request, scheme_of_work_id=22, lesson_id=45, auth_user=6079)
        
        with patch.object(LessonModel, "save_keywords", side_effect=KeyError):   
            # act
            
            with self.assertRaises(KeyError):
                test_context.execute(mock_request)

            # assert
            LessonModel.save_keywords.assert_called()
            self.assertEqual(15, test_context.model.id)
            self.assertEqual("Database", test_context.model.term)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_called_save__update_existing(self, check_permission):

        # arrange
        
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "POST"    
        )
        mock_request.POST = Mock({
                    "scheme_of_work_id": 5,
                    "lesson_id": 230
                })

        mock_request.POST.getlist = MagicMock(returns_value=[1,2,3])

        # act

        test_context = ViewModel(db=db, request=mock_request, scheme_of_work_id=22, lesson_id=45, auth_user=6079)

        
        with patch.object(LessonModel, "save_keywords"):
            
            test_context.execute(mock_request)
            
            # assert functions was called
            LessonModel.save_keywords.assert_called()


    @skip("not implemented")
    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_should_raise_PermissionError(self, check_permission):
        # arrange
        
        with self.assertRaises(PermissionError):
            # act

            ViewModel(db=self.mock_db, scheme_of_work_id=99, model=KeywordModel(0, "New Keyword", scheme_of_work_id=13), auth_user=99)
