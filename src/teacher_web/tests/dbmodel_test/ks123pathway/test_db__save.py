from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_ks123pathway import KS123PathwayModel as Model
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

        model = Model(0, objective="Mauris ac velit ultricies, vestibulum.", year_id=1, topic_id=3, ctx=mock_auth_user)
        model.published = STATE.PUBLISH
        model.is_new = Mock(return_value=True)

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.save(self.fake_db, model, auth_ctx=mock_auth_user)


    def test_should_call___update___updatewith_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, objective="Mauris ac velit ultricies, vestibulum.", ctx=mock_auth_user)
        model.is_new = Mock(return_value=False)
        model.published = STATE.PUBLISH
        
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                
                Model.save(self.fake_db, model, auth_ctx=mock_auth_user)


    def test_should_call__update_with__is_new__false(self, mock_auth_user):
         # arrange

        model = Model(1, objective="Mauris ac velit ultricies, vestibulum.", year_id=1, topic_id=3, ctx=mock_auth_user)
        model.is_new = MagicMock(return_value=False)
        model.is_valid = MagicMock(return_value=True)
        model.published = STATE.PUBLISH

        #test_context._update_lesson_lessonobjectives = Mock()

        expected_result = model.id

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_ctx=mock_auth_user)
            
            # assert
            
            ExecHelper.update.assert_called_with(self.fake_db, 
                'ks123_pathway__update'
                , (1, 'Mauris ac velit ultricies, vestibulum.', mock_auth_user.department_id, 1, 3, 1, mock_auth_user.auth_user_id)
                ,  handle_log_info)

            self.assertEqual(expected_result, actual_result.id)


    def test_should_call__insert__when__is_new__true(self, mock_auth_user):
        # arrange

        model = Model(0, objective="Mauris ac velit ultricies, vestibulum.", year_id=1, topic_id=3, ctx=mock_auth_user)
        model.published = STATE.PUBLISH
        model.is_new = MagicMock(return_value=True)
        model.is_valid = MagicMock(return_value=True)
        
        expected_result = ([], "100")

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_ctx=mock_auth_user)

            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db,
                'ks123_pathway__insert'
                , (0, 'Mauris ac velit ultricies, vestibulum.', mock_auth_user.department_id, 1, 3, 1, mock_auth_user.auth_user_id)
                , handle_log_info)
                
            self.assertNotEqual(0, actual_result.id)
