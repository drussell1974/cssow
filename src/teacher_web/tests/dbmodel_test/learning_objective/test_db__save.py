from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, LearningObjectiveDataAccess, handle_log_info
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

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

        model = Model(1, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.save(self.fake_db, model, mock_auth_user, published=STATE.PUBLISH),


    def test_should_call__update_with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                
                Model.save(self.fake_db, model, mock_auth_user, published=STATE.PUBLISH)


    def test_should_call__update_with__is_new__false(self, mock_auth_user):
         # arrange
        model = Model(1, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        model.is_new = MagicMock(return_value=False)
        model.is_valid = MagicMock(return_value=True)

        expected_result = model.id

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, mock_auth_user, published=STATE.PUBLISH)
            
            # assert
            
            ExecHelper.update.assert_called_with(self.fake_db, 
                "lesson_learning_objective__update"
                , (1, 12, 'Mauris ac velit ultricies, vestibulum.', '', '', '', 1, None, None, 1, mock_auth_user.auth_user_id)
                , handle_log_info)


            self.assertEqual(expected_result, actual_result.id)


    def test_should_call__insert__when__is_new__true(self, mock_auth_user):
        # arrange

        model = Model(0, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = MagicMock(return_value=True)
        model.is_valid = MagicMock(return_value=True)
        
        expected_result = ("100",23)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, mock_auth_user, published=STATE.PUBLISH)

            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                "lesson_learning_objective__insert"
                , (0, 12, 'Mauris ac velit ultricies, vestibulum.', '', '', '', 1, None, None, '2021-01-24 07:18:18.677084', 0, 1, mock_auth_user.auth_user_id)
                , handle_log_info)
                
            self.assertEqual(23, actual_result.id)


    def test_should_call__delete__when__published_state_is_delete__true(self, mock_auth_user):
        # arrange

        model = Model(909, description="Mauris ac velit ultricies, vestibulum.", lesson_id=12, solo_taxonomy_id=1)
        
        model.is_new = MagicMock(return_value=True)
        model.is_valid = MagicMock(return_value=True)

        expected_result = (23,)

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, mock_auth_user, published=STATE.DELETE)

            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                "lesson_learning_objective__delete"
                , (909,mock_auth_user.auth_user_id)
                , handle_log_info)
                
            self.assertEqual(909, actual_result.id)

