from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, TeacherPermissionDataAccess as DataAccess, handle_log_info
from tests.test_helpers.mocks import fake_ctx_model, fake_teacher_permission_model, mock_scheme_of_work

class test_db__full_access(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(56, "Jane Mellor", join_code="ABCDEFGH", scheme_of_work = mock_scheme_of_work(id=14, ctx=fake_ctx_model()), ctx=fake_ctx_model())
        model.is_valid = True
        
        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.full_access(self.fake_db, model, fake_ctx_model())


    def test_should_not_call__insert__when_not_valid(self):
        # arrange

        model = Model(0, "", "ABCDEFGH", mock_scheme_of_work(id=14, ctx=fake_ctx_model()), SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=False, ctx=fake_ctx_model())
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        
        # mock functions not being tested

        expected_result = (14,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            model.validate()
            self.assertFalse(model.is_valid, "should not be valid for this test")

            Model.full_access(self.fake_db, model, auth_user=fake_ctx_model())
            
            # assert

            ExecHelper.insert.assert_not_called()

    @skip("review")
    def test_should_not_call__insert__when_access_already_granted(self):
        # arrange

        
        ''' set is_authorised/permission granted on model '''

        model = Model(56, "Jane Mellor", mock_scheme_of_work(id=14, ctx=fake_ctx_model()), SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD, is_authorised=True, ctx=fake_ctx_model()) 
        model.created = '2021-01-24 07:18:18.677084'


        with patch.object(ExecHelper, 'insert', return_value=0):
            # act

            model.validate()
            self.assertTrue(model.is_valid, "pre-checks failed")

            Model.full_access(self.fake_db, model, auth_user=fake_ctx_model())
            
            # assert

            ExecHelper.insert.assert_not_called()


    def test_should_call__insert_department__has__teacher_permissions(self):
        # arrange

        fake_ctx = fake_ctx_model(6079)

        model = Model(56, "Jane Mellor", join_code="ABCDEFGH", is_authorised=True, ctx=fake_ctx)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        model.is_valid = True
        
        # mock functions not being tested

        expected_result = model

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.full_access(self.fake_db, model, auth_user=fake_ctx)
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'department__has__teacher__insert$2'
                , (6079, 67, "ABCDEFGH", int(DEPARTMENT.ADMIN), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), 6079)
                , handle_log_info)

            
            self.assertEqual("Jane Mellor", actual_result.teacher_name)
            ''' is_authorised must be explicitly set to true '''
            self.assertTrue(actual_result.is_authorised)
