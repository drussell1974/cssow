from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, TeacherPermissionDataAccess as DataAccess, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

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

        scheme_of_work = MagicMock(id=99, name="A-Level Computer Science")

        model = Model(1, "", scheme_of_work)

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, 99)


    def test_should_call_update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        scheme_of_work = MagicMock(id=1, name="A-Level Computer Science")
        
        model = Model(13, "Dave Russell", scheme_of_work, SCHEMEOFWORK.EDITOR, LESSON.EDITOR, DEPARTMENT.TEACHER)
        model.is_new = Mock(return_value=False)

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model, 99)


    def test_should_call__update_with__is_new__false(self):
         # arrange

        scheme_of_work = MagicMock(id=11, name="A-Level Computer Science")
        
        model = Model(1069, "Dave Russell", scheme_of_work, SCHEMEOFWORK.VIEWER, LESSON.VIEWER, DEPARTMENT.STUDENT)
        model.is_new = Mock(return_value=False)
        
        with patch.object(ExecHelper, 'update', return_value=(1,)):
            # act

            actual_result = save(db=self.fake_db, model=model, auth_user=99)
            
            # assert
            
            ExecHelper.update.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__update'
                , (11, 1069, int(DEPARTMENT.STUDENT), int(SCHEMEOFWORK.VIEWER), int(LESSON.VIEWER), 99)
                ,handle_log_info)

            self.assertEqual(11, actual_result.scheme_of_work.id)
            self.assertEqual(1069, actual_result.teacher_id)


    def test_should_call__insert__when__is_new__true(self):
        # arrange

        scheme_of_work = MagicMock(id=14, name="A-Level Computer Science")

        model = Model(56, "Jane Mellor", scheme_of_work, SCHEMEOFWORK.OWNER, LESSON.OWNER, DEPARTMENT.HEAD)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=True)
        
        # mock functions not being tested

        expected_result = (14,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__insert'
                , (14, 56, int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), 99, False)
                , handle_log_info)
            
            self.assertEqual(14, actual_result.scheme_of_work.id)
            self.assertEqual(56, actual_result.teacher_id)


    def test_should_call__delete__when__is_new__is_false__and__published_is_2(self):
        # arrange

        scheme_of_work = MagicMock(id=19, name="A-Level Computer Science")

        model = Model(79, "Jane Mellor", scheme_of_work, SCHEMEOFWORK.VIEWER, SCHEMEOFWORK.EDITOR, DEPARTMENT.TEACHER)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=False)
        model.published = 2

        # mock functions not being tested

        expected_result = (19,)

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=99)
            
            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__delete'
                , (19, 79, 99)
                , handle_log_info)
            
            self.assertEqual(19, actual_result.scheme_of_work.id)
            self.assertEqual(79, actual_result.teacher_id)
