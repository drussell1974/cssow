from datetime import datetime
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.lesson_schedules.viewmodels import LessonScheduleEditViewModel as ViewModel
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model
from shared.models.cls_lesson import LessonModel
from tests.test_helpers.mocks import fake_ctx_model, fake_lesson_schedule

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_404_if_lesson_not_found(self, mock_auth_user):

        # arrange

        mock_request = Mock()
        mock_request.method = "GET"
        
        mock_db = MagicMock()
        mock_db.cursor = MagicMock()
        
        # mock lesson (not from database)
        get_fake_lesson = LessonModel(0, "", is_from_db=False)

        with patch.object(LessonModel, "get_model", return_value=get_fake_lesson):
            with patch.object(Model, "get_model", return_value=None):
            
                # act

                test_context = ViewModel(db=mock_db, request=mock_request, schedule_id=0, lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
                
                test_context.view()
                
                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertFalse(test_context.saved)
                
                LessonModel.get_model.assert_called()
                
                # returns new model
                self.assertEqual(0, test_context.model.id)
                self.assertEqual(6, len(test_context.model.class_code))


    def test_view_when_new(self, mock_auth_user):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "GET"
        
        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        # mock lesson
        get_fake_lesson = LessonModel(220, "Consectetur adipiscing elit", is_from_db=True)

        with patch.object(LessonModel, "get_model", return_value=get_fake_lesson):
            with patch.object(Model, "get_model", return_value=None):
            
                # act

                test_context = ViewModel(db=mock_db, request=mock_request, schedule_id=0, lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
                
                test_context.view()
                
                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertFalse(test_context.saved)
                
                Model.get_model.assert_not_called()
                LessonModel.get_model.assert_called()

                # returns new model
                self.assertEqual(0, test_context.model.id)
                self.assertEqual(6, len(test_context.model.class_code))
                

    def test_view_when_existing(self, mock_auth_user):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "GET"
        
        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        # mock lesson
        get_fake_lesson = LessonModel(220, "Consectetur adipiscing elit", is_from_db=True)

        return_schedule_model = fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="7x", class_code="ABCDEF", start_date="2021-04-01T13:46", lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
        return_schedule_model.is_valid = True

        with patch.object(LessonModel, "get_model", return_value=get_fake_lesson):
            with patch.object(Model, "get_model", return_value=return_schedule_model):
            
                # act

                test_context = ViewModel(db=mock_db, request=mock_request, schedule_id=101, lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
                
                test_context.view()
                
                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertFalse(test_context.saved)
                
                Model.get_model.assert_called()
                LessonModel.get_model.assert_called()

                # returns new model
                self.assertEqual(101, test_context.model.id)
                self.assertEqual("ABCDEF", test_context.model.class_code)
                self.assertEqual(datetime(2021, 4, 1, 13, 46), test_context.model.start_date)
                self.assertEqual("2021-04-01", test_context.model.start_date_ui_date)
                self.assertEqual("13:46", test_context.model.start_date_ui_time)



    def test_execute_called_save_when_valid(self, mock_auth_user):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "class_code": "XBCDEF",
                    "class_name": "10yab",
                    "start_date": "2021-04-03",
                    "period": "04:42",
                    "published": "PUBLISH"
                }

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        # mock lesson
        get_fake_lesson = LessonModel(220, "Consectetur adipiscing elit", is_from_db=True)
        
        # mock existing object in database
        get_schedule_model = fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="7x", class_code="ABCDEF", start_date="2021-04-01T13:46", lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
        get_schedule_model.is_valid = True

        # mock saved object
        on_save__data_to_return = fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="", class_code="", start_date="2021-04-01T13:46", lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
        on_save__data_to_return.is_valid = True

        with patch.object(LessonModel, "get_model", return_value=get_fake_lesson):
            with patch.object(Model, "get_model", return_value=get_schedule_model):    
                with patch.object(Model, "save", return_value=on_save__data_to_return):

                    # act

                    test_context = ViewModel(db=mock_db, request=mock_request, schedule_id=101, lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
                                
                    test_context.execute()
                    
                    # assert 

                    self.assertEqual("", test_context.error_message)
                    self.assertTrue(test_context.saved)
                    
                    Model.save.assert_called()
                    LessonModel.get_model.assert_called()

                    self.assertEqual(101, test_context.model.id)
                    self.assertEqual("10yab", test_context.model.class_name)
                    self.assertEqual("XBCDEF", test_context.model.class_code)                
                    self.assertEqual(datetime(2021, 4, 3, 4, 42), test_context.model.start_date)
                    self.assertEqual("2021-04-03T04:42", test_context.model.start)
                    self.assertEqual("2021-04-03", test_context.model.start_date_ui_date)
                    self.assertEqual("04:42", test_context.model.start_date_ui_time)


    def test_execute_called_save__return_when_invalid(self, mock_auth_user):
         
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "class_code": "XBCDEX",
                    "class_name": "",
                    "start_date": "2021-04-03",
                    "period": "04:44",
                    "published": "PUBLISH"
                }

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        # mock lesson
        get_fake_lesson = LessonModel(220, "Consectetur adipiscing elit", is_from_db=True)

        # mock existing object in database
        get_schedule_model = fake_lesson_schedule(101, title="Vivamus at porta orci",  class_name="7x", class_code="ABCDEF", start_date="2021-04-01T13:46", lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
        get_schedule_model.is_valid = True

        # mock saved object
        on_save__data_to_return = fake_lesson_schedule(101, title="Vivamus at porta orci", class_name="", class_code="", start_date="2021-04-01T13:46", lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
        on_save__data_to_return.is_valid = True

        with patch.object(LessonModel, "get_model", return_value=get_fake_lesson):
            with patch.object(Model, "get_model", return_value=get_schedule_model):    
                with patch.object(Model, "save", return_value=on_save__data_to_return):

                    # act

                    test_context = ViewModel(db=mock_db, request=mock_request, schedule_id=101, lesson_id=0, scheme_of_work_id=0, auth_ctx=mock_auth_user)
                                
                    test_context.execute()
                    
                    # assert 

                    self.assertEqual({'class_name': 'required'}, test_context.error_message)
                    self.assertFalse(test_context.saved)
                    
                    Model.save.assert_not_called()
                    LessonModel.get_model.assert_called()

                    self.assertEqual(101, test_context.model.id)
                    self.assertEqual("", test_context.model.class_name)
                    self.assertEqual("XBCDEX", test_context.model.class_code)
                    self.assertEqual(datetime(2021, 4, 3, 4, 44), test_context.model.start_date)
                    self.assertEqual("2021-04-03T04:44", test_context.model.start)
                    self.assertEqual("2021-04-03", test_context.model.start_date_ui_date)
                    self.assertEqual("04:44", test_context.model.start_date_ui_time)
