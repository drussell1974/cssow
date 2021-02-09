from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, TeacherPermissionDataAccess as DataAccess, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

save = Model.save

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Jane Doe", department=DepartmentModel(67, "Computer Science")))
@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(9999, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_teacher_model, mock_auth_model):
        # arrange
        expected_exception = KeyError("Bang!")

        scheme_of_work = MagicMock(id=99, name="A-Level Computer Science")

        model = Model(mock_teacher_model, scheme_of_work)
        model.is_valid = True

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, 99)


    def test_should_call_update_with_exception(self, mock_teacher_model, mock_auth_model):
        # arrange
        expected_exception = KeyError("Bang!")

        scheme_of_work = MagicMock(id=1, name="A-Level Computer Science")
        
        model = Model(mock_teacher_model, scheme_of_work, SCHEMEOFWORK.EDITOR, LESSON.EDITOR, DEPARTMENT.TEACHER, is_authorised=True)
        model.is_new = Mock(return_value=False)
        model.is_valid = True

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model, 99)


    def test_should_call__update_with__is_new__false(self, mock_teacher_model, mock_auth_model):
         # arrange

        scheme_of_work = MagicMock(id=11, name="A-Level Computer Science")
        
        model = Model(mock_teacher_model, scheme_of_work, SCHEMEOFWORK.VIEWER, LESSON.VIEWER, DEPARTMENT.STUDENT, is_authorised=False)
        model.is_new = Mock(return_value=False)
        model.is_valid = True
        
        with patch.object(ExecHelper, 'update', return_value=(1,)):
            # act

            actual_result = save(db=self.fake_db, model=model, auth_user=mock_auth_model)
            
            # assert
            
            ExecHelper.update.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__update'
                , (11, mock_teacher_model.id, int(DEPARTMENT.STUDENT), int(SCHEMEOFWORK.VIEWER), int(LESSON.VIEWER), mock_auth_model.id, False)
                ,handle_log_info)

            self.assertEqual(11, actual_result.scheme_of_work.id)
            self.assertEqual(mock_teacher_model.id, actual_result.teacher.id)


    def test_should_call__insert__when__is_new__true(self, mock_teacher_model, mock_auth_model):
        # arrange

        scheme_of_work = MagicMock(id=14, name="A-Level Computer Science")
        # 56, "Jane Mellor"

        model = Model(mock_teacher_model, scheme_of_work, SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=True)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        model.is_valid = True
        
        # mock functions not being tested

        expected_result = (14,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=mock_auth_model)
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__insert'
                , (14, mock_teacher_model.id, int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), mock_auth_model.id, True)
                , handle_log_info)
            
            self.assertEqual(14, actual_result.scheme_of_work.id)
            self.assertEqual(mock_teacher_model.id, actual_result.teacher.id)


    def test_should_call__delete__when__is_new__is_false__and__published_is_2(self, mock_teacher_model, mock_auth_model):
        # arrange

        scheme_of_work = MagicMock(id=19, name="A-Level Computer Science")
        #
        model = Model(mock_teacher_model, scheme_of_work, SCHEMEOFWORK.VIEWER, SCHEMEOFWORK.EDITOR, DEPARTMENT.TEACHER, is_authorised=False)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=False)
        model.is_valid = True
        model.published = 2

        # mock functions not being tested

        expected_result = (19,)

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=mock_auth_model)
            
            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__delete'
                , (19, mock_teacher_model.id, mock_auth_model.id)
                , handle_log_info)
            
            self.assertEqual(19, actual_result.scheme_of_work.id)
            self.assertEqual(mock_teacher_model.id, actual_result.teacher.id)
