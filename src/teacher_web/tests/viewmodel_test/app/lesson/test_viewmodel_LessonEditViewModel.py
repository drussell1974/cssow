import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.lessons.viewmodels import LessonEditViewModel as ViewModel
from app.default.viewmodels import KeywordSaveViewModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.cls_keyword import KeywordModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model, fake_lesson_schedule

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_execute_called_save__new(self, mock_auth_user):
        
        # arrange
        
        on_save__data_to_return = Model(92, "Quisque eu venenatis sem")
        on_save__data_to_return.is_valid = True

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(LessonScheduleModel, "save", return_value=fake_lesson_schedule(id=15, auth_ctx=mock_auth_user)):            
                with patch.object(Model, "save", return_value=on_save__data_to_return):

                    return_keyword_model = KeywordModel(4, term="Four")
                    return_keyword_model.is_valid = True

                    save_keyword.execute = Mock(return_value=return_keyword_model)
                    save_keyword.model = return_keyword_model

                    # act
                    mock_model = Model(1, "Proin id massa metus. Aliqua tincidunt.")
                    mock_model.scheme_of_work_id = 12
                    mock_model.content_id = 10
                    mock_model.topic_id = 12
                    mock_model.key_stage_id = 2
                    mock_model.year_id = 10

                    ''' ensure is_new is true to generate class code '''
                    mock_model.is_new = MagicMock(return_value=True)

                    test_context = ViewModel(db=self.mock_db, scheme_of_work_id=12, model=mock_model, auth_user=mock_auth_user)
                    test_context.execute(published=STATE.PUBLISH)
                                    
                    # assert functions was called
                    Model.save.assert_called()
                    LessonScheduleModel.save.assert_called()

                    self.assertEqual({}, test_context.model.validation_errors)            
                    self.assertEqual(92, test_context.model.id)
                    self.assertEqual("Quisque eu venenatis sem", test_context.model.title)
                    self.assertEqual([], test_context.model.key_words)
                    self.assertEqual({}, test_context.model.validation_errors) 
                    self.assertTrue(test_context.model.is_valid)
                    self.assertEqual("ABCDEF", test_context.lesson_schedule.class_code)           
                    

    def test_execute_called_save__add_model_to_data(self, mock_auth_user):
        
        # arrange
        
        on_save__data_to_return = Model(92, "Quisque eu venenatis sem")
        on_save__data_to_return.is_valid = True

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(LessonScheduleModel, "save", return_value=fake_lesson_schedule(id=15, auth_ctx=mock_auth_user)):            
                with patch.object(Model, "save", return_value=on_save__data_to_return):

                    return_keyword_model = KeywordModel(4, term="Four")
                    return_keyword_model.is_valid = True

                    save_keyword.execute = Mock(return_value=return_keyword_model)
                    save_keyword.model = return_keyword_model

                    # act
                    mock_model = Model(34343, "Proin id massa metus. Aliqua tincidunt.")
                    mock_model.scheme_of_work_id = 12
                    mock_model.content_id = 10
                    mock_model.topic_id = 12
                    mock_model.key_stage_id = 2
                    mock_model.year_id = 10

                    test_context = ViewModel(db=self.mock_db, scheme_of_work_id=12, model=mock_model, auth_user=mock_auth_user)
                    test_context.execute(published=STATE.PUBLISH)
                                    
                    # assert functions was called
                    Model.save.assert_called()
                    LessonScheduleModel.save.assert_not_called()

                    self.assertEqual({}, test_context.model.validation_errors)            
                    self.assertEqual(92, test_context.model.id)
                    self.assertEqual("Quisque eu venenatis sem", test_context.model.title)
                    self.assertEqual([], test_context.model.key_words)
                    self.assertEqual({}, test_context.model.validation_errors) 
                    self.assertTrue(test_context.model.is_valid)
                    self.assertIsNone(test_context.lesson_schedule)           
                    

    def test_execute_called_lesson_schedule(self, mock_auth_user):
        
        # arrange
        
        on_save__data_to_return = Model(92, "Quisque eu venenatis sem")
        on_save__data_to_return.is_valid = True

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(LessonScheduleModel, "save", return_value=fake_lesson_schedule(id=15, auth_ctx=mock_auth_user)):            
                with patch.object(Model, "save", return_value=on_save__data_to_return):

                    return_keyword_model = KeywordModel(4, term="Four")
                    return_keyword_model.is_valid = True

                    save_keyword.execute = Mock(return_value=return_keyword_model)
                    save_keyword.model = return_keyword_model

                    # act
                    mock_model = Model(0, "Proin id massa metus. Aliqua tincidunt.")
                    mock_model.scheme_of_work_id = 12
                    mock_model.content_id = 10
                    mock_model.topic_id = 12
                    mock_model.key_stage_id = 2
                    mock_model.year_id = 10

                    ''' ensure is_new is false so generate class code is NOT called '''
                    mock_model.is_new = MagicMock(return_value=False)

                    test_context = ViewModel(db=self.mock_db, scheme_of_work_id=12, model=mock_model, auth_user=mock_auth_user, create_schedule=True)
                    test_context.execute(published=STATE.PUBLISH)
                    
                    # assert functions was called
                    Model.save.assert_called()
                    LessonScheduleModel.save.assert_called()

                    self.assertEqual("ABCDEF", test_context.lesson_schedule.class_code)           
                    

    def test_execute_called_save__add_model_to_data__return_invalid(self, mock_auth_user):
        
        # arrange
        
        
        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(LessonScheduleModel, "save", return_value=fake_lesson_schedule(id=15, auth_ctx=mock_auth_user)):
                with patch.object(Model, "save", return_value=None):
                    
                    save_keyword.model = Mock(return_value=KeywordModel(12, scheme_of_work_id=13))

                    # act
                    mock_model = Model(99, "")                
                    mock_model.scheme_of_work_id = 12
                    mock_model.content_id = 10
                    mock_model.topic_id = 12
                    mock_model.key_stage_id = 2
                    mock_model.year_id = 10
                    
                    test_context = ViewModel(db=self.mock_db, scheme_of_work_id=12, model=mock_model, auth_user=mock_auth_user)
                    test_context.execute(0)
                                    
                    # assert save functions was not called
                    Model.save.assert_not_called()
                    LessonScheduleModel.save.assert_not_called()

                    self.assertEqual(99, test_context.model.id)
                    self.assertEqual("", test_context.model.title)
                    self.assertFalse(test_context.model.is_valid)            
                    self.assertEqual(1, len(test_context.model.validation_errors)) 
                    self.assertEqual({'title': 'required'}, test_context.model.validation_errors) 
                    self.assertIsNone(test_context.lesson_schedule)
                    