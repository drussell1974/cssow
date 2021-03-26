from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model, SchemeOfWorkDataAccess as DataAccess, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from shared.models.cls_department import DepartmentModel
from tests.test_helpers.mocks import fake_ctx_model

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

        model = Model(0, "", study_duration=2, start_study_in_year=10, auth_user=fake_ctx_model())

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model.save(self.fake_db, model)


    def test_should_call__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, "", study_duration=2, start_study_in_year=10, auth_user=fake_ctx_model())
    
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                Model.save(self.fake_db, model)


    def test_should_call__update_with__is_new__false(self):
        # arrange

        fake_ctx = fake_ctx_model()
        
        model = Model(89, "KS3 Computing", study_duration=3, start_study_in_year=7, auth_user=fake_ctx)
        model.key_stage_id = 4
        model.start_study_in_year = 10
        model.is_new = Mock(return_value=False)

        with patch.object(ExecHelper, 'update', return_value=model):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=fake_ctx)
            # assert
            ExecHelper.update.assert_called_with(self.fake_db,
                'scheme_of_work__update$2'
                , (89, 'KS3 Computing', 3, 10, '', 0, 4, 67, int(STATE.PUBLISH), fake_ctx.auth_user_id)
                , handle_log_info)
            
            self.assertEqual(89, actual_result.id)


    def test_should_call__scheme_of_work__insert__when__is_new__true(self):
        # arrange
        
        fake_ctx = fake_ctx_model()

        model = Model(0, "", study_duration=2, start_study_in_year=10, auth_user=fake_ctx)
        model.exam_board_id = 2
        model.created = "2021-01-24 07:13:09.681409"

        DataAccess._insert_as__teacher = Mock(return_value=1)

        with patch.object(ExecHelper, 'insert', return_value=(101,)):
            # act


            actual_result = Model.save(self.fake_db, model, fake_ctx)

            # assert
            
            ExecHelper.insert.assert_called_with(self.fake_db,
                 'scheme_of_work__insert$2'
                 , (0, '', 2, 10, '', 2, 0, 67, '2021-01-24 07:13:09.681409', 0, STATE.PUBLISH, fake_ctx.auth_user_id)
                 , handle_log_info)
                 
            DataAccess._insert_as__teacher.assert_called()

            self.assertEqual(101, actual_result.id)


    def test_should_call__scheme_of_work__has_teacher__insert__when__is_new__true(self):
        # arrange

        model = Model(0, "", study_duration=2, start_study_in_year=10, auth_user=fake_ctx_model())

        with patch.object(ExecHelper, 'insert', return_value=[101]):
            # act

            actual_result = Model.save(self.fake_db, model, fake_ctx_model())

            # assert

            ExecHelper.insert.assert_called_with(self.fake_db,
                 'scheme_of_work__has__teacher_permission__insert'
                 , (101, fake_ctx_model().auth_user_id, DEPARTMENT.HEAD.value, SCHEMEOFWORK.OWNER.value, LESSON.OWNER.value, fake_ctx_model().auth_user_id, True)
                 , handle_log_info)

            self.assertEqual(101, actual_result.id)


    def test_should_call__delete_when_published_is_delete(self):
        # arrange

        model = Model(99, "", study_duration=2, start_study_in_year=10, auth_user=fake_ctx_model())


        with patch.object(ExecHelper, 'delete', return_value=([], 101)):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=fake_ctx_model(), published=STATE.DELETE)

            # assert

            ExecHelper.delete.assert_called_with(self.fake_db,
            'scheme_of_work__delete'
            
            , (99, fake_ctx_model().auth_user_id)
            , handle_log_info)

            self.assertEqual(99, actual_result.id)