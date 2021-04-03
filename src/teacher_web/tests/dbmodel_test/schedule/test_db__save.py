from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model, LessonScheduleDataAccess, handle_log_info
#from shared.models.cls_department import DepartmentModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, class_name="7x", class_code="", start_date=None, lesson_id = 12, scheme_of_work_id = 11, auth_user=mock_auth_user)

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.save(self.fake_db, model, published=STATE.PUBLISH, auth_user=mock_auth_user)

    
    def test_should_call__update_with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, class_name="7x", class_code="", start_date=None, lesson_id = 12, scheme_of_work_id = 11, auth_user=mock_auth_user)
    
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                Model.save(self.fake_db, model)


    def test_should_call__update_with__is_new__false(self, mock_auth_user):
         # arrange
        model = Model(1, class_name="7x", class_code="ZYXWVU", start_date=None, lesson_id = 12, scheme_of_work_id = 11, auth_user=mock_auth_user)

        expected_result = model.id

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published=STATE.PUBLISH)
            
            # assert
            
            ExecHelper.update.assert_called_with(self.fake_db, 
                 'lesson_schedule__update'
                , (1, 'ZYXWVU', mock_auth_user.institute_id, mock_auth_user.department_id, 11, 12, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , handle_log_info)

            self.assertEqual(1, actual_result.id)


    def test_should_call__insert_insert__when__is_new__true(self, mock_auth_user):
        # arrange

        model = Model(0, class_name="7x", class_code="MNOPQR", start_date=None, lesson_id = 12, scheme_of_work_id = 11, auth_user=mock_auth_user)

        expected_result = (876,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published = STATE.PUBLISH)
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db,
                'lesson_schedule__insert'
                , (0, 'MNOPQR', mock_auth_user.institute_id, mock_auth_user.department_id, 11, 12, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , handle_log_info)
            
            self.assertEqual(876, actual_result.id)


    def test_should_call__delete__when__is_new__false__and__published_is_2(self, mock_auth_user):
        # arrange

        model = Model(101, class_name="7x", class_code="MNOPQR", start_date=None, lesson_id = 12, scheme_of_work_id = 11, auth_user=mock_auth_user)
        
        expected_result = model.id

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published=STATE.DELETE)

            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                "lesson_schedule__delete"
                , (101, mock_auth_user.auth_user_id)
                , handle_log_info)

            # check subsequent functions where called

            self.assertEqual(101, actual_result.id)
            self.assertEqual(STATE.DELETE, actual_result.published)