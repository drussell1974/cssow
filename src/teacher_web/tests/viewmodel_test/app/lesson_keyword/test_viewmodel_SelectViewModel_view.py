from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.lesson_keywords.viewmodels import LessonKeywordSelectViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_teacher_permission import TeacherPermissionModel


class test_viewmodel_KeywordSelectViewModel_view(TestCase):
    
    fake_lesson = LessonModel(45)
    fake_lesson.is_from_db = True


    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    @patch.object(LessonModel, "get_options", return_value=[])
    def test_init_called_fetch__no_return_rows(self, LessonModel__get_model, LessonModel__get_options):
        
        # arrange
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )
    
        self.fake_schemeofwork = SchemeOfWorkModel(22)
        self.fake_schemeofwork.is_from_db = True
        self.fake_schemeofwork.key_words.clear()
                
        with patch.object(SchemeOfWorkModel, "get_model", return_value=self.fake_schemeofwork):
            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=22, lesson_id=45, auth_user=6079)
            actual_result.view(mock_request)

            # assert functions was called
            SchemeOfWorkModel.get_model.assert_called()
            LessonModel__get_model.assert_called()
            LessonModel__get_options.assert_called()

            self.assertEqual(45, actual_result.model.id)


    
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    def test_init_called_fetch_single_item(self, LessonModel__get_model):

        # arrange
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )
    
        self.fake_schemeofwork = SchemeOfWorkModel(22)
        self.fake_schemeofwork.is_from_db = True   
        self.fake_schemeofwork.key_words.clear()
        self.fake_schemeofwork.key_words.append(Model(34))

        with patch.object(SchemeOfWorkModel, "get_model", return_value=self.fake_schemeofwork):
            # act
            actual_result = ViewModel(db=db, request=mock_request, lesson_id=45, scheme_of_work_id=22, auth_user=6079)
            actual_result.view(mock_request)

            # assert functions was called
            SchemeOfWorkModel.get_model.assert_called()
            LessonModel__get_model.assert_called()

            self.assertEqual(45, actual_result.model.id)        
            self.assertEqual(1, len(actual_result.keyword_options))


    
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    @patch.object(LessonModel, "get_options", return_value=[LessonModel(34), Model(35), Model(36)])
    def test_init_called_fetch__multiple_items(self, LessonModel__get_model, LessonModel__get_options):
        
        # arrange
        
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )
        
        self.fake_schemeofwork = SchemeOfWorkModel(22)
        self.fake_schemeofwork.is_from_db = True   
        self.fake_schemeofwork.key_words.clear()
        self.fake_schemeofwork.key_words.append(Model(34))
        self.fake_schemeofwork.key_words.append(Model(35))
        self.fake_schemeofwork.key_words.append(Model(36))
                
        with patch.object(SchemeOfWorkModel, "get_model", return_value=self.fake_schemeofwork):
                
            # act
            actual_result = ViewModel(db=db, request=mock_request, lesson_id=45, scheme_of_work_id=12, auth_user=6079)
            actual_result.view(mock_request)

            # assert functions was called
            SchemeOfWorkModel.get_model.assert_called()
            LessonModel__get_model.assert_called()
            LessonModel__get_options.assert_called()     

            self.assertEqual(45, actual_result.model.id)    
            self.assertEqual(3, len(actual_result.lesson_options))        
            self.assertEqual(3, len(actual_result.keyword_options))
