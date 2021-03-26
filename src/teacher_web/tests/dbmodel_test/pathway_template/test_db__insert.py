from unittest import TestCase
from shared.models.cls_pathway_template import PathwayTemplateModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db___insert(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__save__with_exception(self, mock_auth_user):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "insert", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.save(self.fake_db, 99, "Lorum ipsum", auth_user=mock_auth_user)


    def test__should_call__save__if_has_option(self, mock_auth_user):
        # arrange

        expected_result = [99]

        fake_model = Model(671, "Lorum ipsum", 3, ctx=mock_auth_user)
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = True

        with patch.object(ExecHelper, "insert", return_value=expected_result):
                
            # act
            
            act_reault = Model.save(self.fake_db, fake_model, auth_user=mock_auth_user)

            # assert

            ExecHelper.insert.assert_called_with(self.fake_db,
                'keystage__insert_from_pathway_template'
                , (671, 3, "2021-01-24 07:20:01.907507", mock_auth_user.auth_user_id, 1)
                , handle_log_info)



    def test__should_call__save__if_has_multiple_options(self, mock_auth_user):
        # arrange

        expected_result = [99]

        fake_model = Model(67, "Lorum ipsum", 2, ctx=mock_auth_user)
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = True

        with patch.object(ExecHelper, "insert", return_value=expected_result):
            
            # act
            
            act_result = Model.save(self.fake_db, fake_model, auth_user = mock_auth_user)

            # assert

            ExecHelper.insert.assert_called_with(self.fake_db,
                'keystage__insert_from_pathway_template'
                , (67, 2, "2021-01-24 07:20:01.907507", mock_auth_user.auth_user_id, 1)
                , handle_log_info)
        