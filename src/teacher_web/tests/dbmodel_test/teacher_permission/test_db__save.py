from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, TeacherPermissionDataAccess as DataAccess, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

save = Model.save

class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        scheme_of_work = MagicMock(id=99, name="A-Level Computer Science", auth_user=fake_ctx_model())

        model = Model(343430908034, "Loren Ipsum", scheme_of_work, ctx = fake_ctx_model()) # ADD ctx
        model.is_valid = True

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, 99)


    def test_should_call_update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        scheme_of_work = MagicMock(id=1, name="A-Level Computer Science", auth_user=fake_ctx_model())
        
        model = Model(343430908034, "Loren Ipsum", scheme_of_work, SCHEMEOFWORK.EDITOR, LESSON.EDITOR, DEPARTMENT.TEACHER, is_authorised=True, ctx=fake_ctx_model())
        model.is_new = Mock(return_value=False)
        model.is_valid = True

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model, 99)


    def test_should_call__update_with__is_new__false(self):
         # arrange

        scheme_of_work = MagicMock(id=11, name="A-Level Computer Science", auth_user=fake_ctx_model())
        
        model = Model(343430908034, "Loren Ipsum", scheme_of_work, SCHEMEOFWORK.VIEWER, LESSON.VIEWER, DEPARTMENT.STUDENT, is_authorised=False, ctx=fake_ctx_model())
        model.is_new = Mock(return_value=False)
        model.is_valid = True
        
        with patch.object(ExecHelper, 'update', return_value=(1,)):
            # act

            actual_result = save(db=self.fake_db, model=model, auth_user=fake_ctx_model())
            
            # assert
            
            ExecHelper.update.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__update'
                , (12323232, 343430908034, int(DEPARTMENT.STUDENT), int(SCHEMEOFWORK.VIEWER), int(LESSON.VIEWER), 6079, False)
                ,handle_log_info)

            self.assertEqual(11, actual_result.scheme_of_work_id)
            self.assertEqual(343430908034, actual_result.teacher_id)


    def test_should_call__insert__when__is_new__true(self):
        # arrange

        scheme_of_work = MagicMock(id=14, name="A-Level Computer Science", auth_user=fake_ctx_model())
        # 56, "Jane Mellor"

        model = Model(343430908034, "Loren Ipsum",scheme_of_work, SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=True, ctx=fake_ctx_model())
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        model.is_valid = True
        
        # mock functions not being tested

        expected_result = (14,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=fake_ctx_model())
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__insert'
                , (12323232, 343430908034, int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), fake_ctx_model().auth_user_id, True)
                , handle_log_info)
            
            self.assertEqual(14, actual_result.scheme_of_work_id)
            self.assertEqual(343430908034, actual_result.teacher_id)


    def test_should_call__delete__when__is_new__is_false__and__published_is_2(self):
        # arrange

        scheme_of_work = MagicMock(id=19, name="A-Level Computer Science", auth_user=fake_ctx_model())
        #
        model = Model(343430908034, "Loren Ipsum", scheme_of_work, SCHEMEOFWORK.VIEWER, SCHEMEOFWORK.EDITOR, DEPARTMENT.TEACHER, is_authorised=False, ctx=fake_ctx_model())
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=False)
        model.is_valid = True
        model.published = STATE.DELETE
        # mock functions not being tested

        expected_result = (19,)

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=fake_ctx_model())
            
            # assert
            
            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__delete'
                , (19, 343430908034, fake_ctx_model().auth_user_id)
                , handle_log_info)
            
            self.assertEqual(19, actual_result.scheme_of_work_id)
            self.assertEqual(343430908034, actual_result.teacher_id)
