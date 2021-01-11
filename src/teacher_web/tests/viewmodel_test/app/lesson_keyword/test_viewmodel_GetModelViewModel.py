from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404

# test context

from app.lesson_keywords.viewmodels import LessonKeywordGetModelViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_KeywordGetModelViewModel(TestCase):
    
    fake_schemeofwork = SchemeOfWorkModel(22)
    fake_schemeofwork.is_from_db = True
    
    fake_lesson = LessonModel(45)
    fake_lesson.is_from_db = True
    

    def setUp(self):                       
        pass
        

    def tearDown(self):
        pass


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    @patch.object(SchemeOfWorkModel, "get_model", return_value=fake_schemeofwork)
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    def test_init_called_fetch__no_return_rows(self, check_permission, SchemeOfWorkModel__get_model, LessonModel__get_model):
        
        # arrange


        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()


            with self.assertRaises(Http404):

                # act
                self.viewmodel = ViewModel(db=db, scheme_of_work_id=22, lesson_id=45, keyword_id=33, auth_user=99)

                # assert functions was called
                Model.get_model.assert_not_called()
                self.assertIsNone(self.viewmodel.model)



    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    @patch.object(SchemeOfWorkModel, "get_model", return_value=fake_schemeofwork)
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    def test_init_called_fetch__return_item(self, check_permission, SchemeOfWorkModel__get_model, LessonModel__get_model):
        
        # arrange
        data_to_return = Model(101, "Abstraction")
        data_to_return.is_from_db = True
    
        fake_schemeofwork = SchemeOfWorkModel(22)
        fake_schemeofwork.is_from_db = True

        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=23, lesson_id=2, keyword_id=101, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(101, self.viewmodel.model.id)
            self.assertEqual("Abstraction", self.viewmodel.model.term)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    @patch.object(SchemeOfWorkModel, "get_model", return_value=fake_schemeofwork)
    @patch.object(LessonModel, "get_model", return_value=fake_lesson)
    def test_should_raise_PermissionError(self, check_permission, SchemeOfWorkModel__get_model, LessonModel__get_model):
        # arrange
        data_to_return = Model(101, "Abstraction")
        data_to_return.is_from_db = True
    
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            with self.assertRaises(PermissionError):
                # act
                self.viewmodel = ViewModel(db=db, scheme_of_work_id=23, lesson_id=2, keyword_id=101, auth_user=99)

                # assert functions was called
                Model.get_model.assert_called()
                self.assertEqual(101, self.viewmodel.model.id)
                self.assertEqual("Abstraction", self.viewmodel.model.term)
