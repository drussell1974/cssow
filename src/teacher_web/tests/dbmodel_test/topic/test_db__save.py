from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_topic import TopicModel as Model
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

        model = Model(0, name="Exceptions", auth_ctx=mock_auth_user)

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.save(self.fake_db, model, auth_ctx=mock_auth_user)


    def test_should_call__update_with__is_new__false(self, mock_auth_user):
         # arrange
        model = Model(23, name="Testing", auth_ctx=mock_auth_user)
        model.parent = Model(4, name="Implementation", auth_ctx=mock_auth_user)
        model.parent_id = 4
        model.lvl = 2

        with patch.object(ExecHelper, 'update', return_value=model):
            # act

            actual_result = Model.save(self.fake_db, model, auth_ctx=mock_auth_user)
            
            # assert
            #update(<Mock id='139717368393616'>, 'topic__update', (23, 'Testing', <MagicMock name='django_helper.department_id' id='139717368285648'>, 4, 2, 1, <MagicMock name='django_helper.auth_user_id' id='139717367809104'>), <function handle_log_info at 0x7f127f7f5050>)
            #update(<Mock id='139717368393616'>, 'topic__update', (23, 'Testing', <MagicMock name='django_helper.department_id' id='139717368285648'>, None, 2, 1, <MagicMock name='django_helper.auth_user_id' id='139717367809104'>), <function handle_log_info at 0x7f127f7f5050>)
            ExecHelper.update.assert_called_with(self.fake_db, 
             'topic__update'
             , (23, 'Testing', mock_auth_user.department_id, 4, 2, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
             , handle_log_info)
            
            self.assertEqual(23, actual_result.id)


    def test_should_call__insert__when__is_new__true(self, mock_auth_user):
        # arrange

        model = Model(0, name="Testing", auth_ctx=mock_auth_user)
        model.created = "2021-01-24 07:14:04"
        model.parent = Model(4, name="Implementation", auth_ctx=mock_auth_user)
        model.parent_id = 4
        model.lvl = 2

        expected_result = (102,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_ctx=mock_auth_user)

            # assert
            
            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'topic__insert'
                , (0, 'Testing', mock_auth_user.department_id, 4, 2, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , handle_log_info)

            self.assertEqual(102, actual_result.id)


    def test_should_call__delete(self, mock_auth_user):
         # arrange
        model = Model(23, name="Testing", auth_ctx=mock_auth_user)
        
        with patch.object(ExecHelper, 'delete', return_value=model):
            # act

            actual_result = Model.save(self.fake_db, model, auth_ctx=mock_auth_user, published=STATE.DELETE)
            
            # assert
            
            ExecHelper.delete.assert_called_with(self.fake_db, 
             'topic__delete'
             , (23, 1, mock_auth_user.auth_user_id)
             , handle_log_info)
            
            self.assertEqual(23, actual_result.id)
            self.assertEqual(STATE.DELETE, actual_result.published)
