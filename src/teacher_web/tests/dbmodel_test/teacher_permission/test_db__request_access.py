from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, TeacherPermissionDataAccess as DataAccess, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

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

        fake_scheme_of_work = SchemeOfWorkModel(99, name="A-Level Computer Science")

        model = Model(1, "En Tus Pupiles", fake_scheme_of_work)
        model.is_valid = True
        
        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.request_access(self.fake_db, model, 99)


    def test_should_not_call__insert__when_not_valid(self):
        # arrange

        fake_scheme_of_work = SchemeOfWorkModel(14, name="A-Level Computer Science")

        model = Model(56, "", fake_scheme_of_work, SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=False)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        
        # mock functions not being tested

        expected_result = (14,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            Model.request_access(self.fake_db, model, auth_user=99)
            
            # assert

            ExecHelper.insert.assert_not_called()


    def test_should_not_call__insert__when_access_already_granted(self):
        # arrange

        fake_scheme_of_work = SchemeOfWorkModel(14, name="A-Level Computer Science")

        ''' set is_authorised/permission granted on model '''

        model = Model(56, "Tu Boca", fake_scheme_of_work, SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=True) 
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        
        # mock functions not being tested

        expected_result = (14,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            Model.request_access(self.fake_db, model, auth_user=99)
            
            # assert

            ExecHelper.insert.assert_not_called()


    @patch.object(DataAccess, "insert_department__has__teacher")
    def test_should_call__insert_scheme_of_work__has__teacher_permissions(self, TeacherPermissionDataAccess_insert_department__has__teacher):
        ''' NOTE: mock @patch.object insert_department__has__teacher to only test scheme_of_work__has__teacher_permission__insert ''' 
        # arrange

        fake_scheme_of_work = SchemeOfWorkModel(14, name="A-Level Computer Science", department_id = 34)

        model = Model(56, "Jane Mellor", fake_scheme_of_work, SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=False)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        model.is_valid = True
        
        # mock functions not being tested

        expected_result = model

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.request_access(self.fake_db, model, auth_user=99)
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__insert'
                , (14, 56, int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), 99, False)
                , handle_log_info)

            TeacherPermissionDataAccess_insert_department__has__teacher.assert_called_with(self.fake_db, model, 99)
            
            self.assertEqual(14, actual_result.scheme_of_work.id)
            self.assertEqual("Jane Mellor", actual_result.teacher_name)
            ''' is_authorised must be explicitly set to false '''
            self.assertFalse(actual_result.is_authorised)


    @patch.object(DataAccess, "insert_access_request", return_value=Model(56, "Jane Mellor", SchemeOfWorkModel(14, name="A-Level Computer Science", department_id = 34), SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=False))
    def test_should_call__insert_department__has__teacher(self, TeacherPermissionDataAccess_insert_access_request):
        ''' NOTE: mock @patch.object insert_access_request to only test **** ''' 
        
        # arrange

        fake_scheme_of_work = SchemeOfWorkModel(14, name="A-Level Computer Science", department_id=67)

        model = Model(56, "Jane Mellor", fake_scheme_of_work, SCHEMEOFWORK.VIEWER, LESSON.EDITOR, DEPARTMENT.HEAD, is_authorised=False)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        model.is_valid = True
        
        # mock functions not being tested

        expected_result = model

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.request_access(self.fake_db, model, auth_user=99)
            
            # assert
            
            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'department__has__teacher__insert'
                , (56, 67, int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.VIEWER), int(LESSON.EDITOR), 99)
                , handle_log_info)
            
            TeacherPermissionDataAccess_insert_access_request.assert_called_with(self.fake_db, model, 99)

            self.assertEqual(14, actual_result.scheme_of_work.id)
            self.assertEqual("Jane Mellor", actual_result.teacher_name)
            ''' is_authorised must be explicitly set to false '''
            self.assertFalse(actual_result.is_authorised)
