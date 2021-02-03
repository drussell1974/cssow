from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.lesson_keywords.viewmodels import LessonKeywordSelectViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.core.log_handlers import handle_log_exception

class test_viewmodel_SelectViewModel_execute(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()


    def tearDown(self):
        pass


    
    def test_execute_not_called_save__with_exception__when_invaid_type(self):
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
    

    
    def test_execute_called_save__update_existing(self):

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
