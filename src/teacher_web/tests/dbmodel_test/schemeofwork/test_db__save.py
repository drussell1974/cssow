from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model, SchemeOfWorkDataAccess as DataAccess, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
# create test context

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

        model = Model(0)

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model)


    def test_should_call__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1)
    
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model)


    def test_should_call__update_with__is_new__false(self):
         # arrange
        model = Model(89)
        model.is_new = Mock(return_value=False)

        with patch.object(ExecHelper, 'update', return_value=model):
            # act

            actual_result = save(self.fake_db, model, 6079)
            
            # assert
            ExecHelper.update.assert_called_with(self.fake_db,
                'scheme_of_work__update'
                , (89, '', '', 0, 0, 1, 6079)
                , handle_log_info)
            
            self.assertEqual(89, actual_result.id)


    def test_should_call__scheme_of_work__insert__when__is_new__true(self):
        # arrange

        model = Model(0)

        DataAccess._insert_as__teacher = Mock(return_value=1)

        with patch.object(ExecHelper, 'insert', return_value=(101)):
            # act

            actual_result = save(self.fake_db, model, 6079)

            # assert

            ExecHelper.insert.assert_called_with(self.fake_db,
                 'scheme_of_work__insert'
                 , (0, '', '', 0, 0, '', 0, 1, 6079)
                 , handle_log_info)
                 
            DataAccess._insert_as__teacher.assert_called()

            self.assertEqual(101, actual_result.id)


    def test_should_call__scheme_of_work__has_teacher__insert__when__is_new__true(self):
        # arrange

        model = Model(0)

        with patch.object(ExecHelper, 'insert', return_value=(101)):
            # act

            actual_result = save(self.fake_db, model, 6079)

            # assert

            ExecHelper.insert.assert_called_with(self.fake_db,
                 'scheme_of_work__has__teacher__insert'
                 , (101, 6079, DEPARTMENT.HEAD, SCHEMEOFWORK.OWNER, LESSON.OWNER)
                 , handle_log_info)
                 

            self.assertEqual(101, actual_result.id)


    def test_should_call__delete_when_published_is_delete(self):
        # arrange

        model = Model(99)


        with patch.object(ExecHelper, 'delete', return_value=([], 101)):
            # act

            actual_result = save(self.fake_db, model, auth_user=6079, published=2)

            # assert

            ExecHelper.delete.assert_called_with(self.fake_db,
            'scheme_of_work__delete'
            , (99, 6079)
            , handle_log_info)

            self.assertEqual(99, actual_result.id)