from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel, handle_log_info
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

class test_db__get_context_model(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkContextModel.get_context_model(self.fake_db, 4, fake_ctx.auth_user_id)


    def test__should_call__select__return_no_items(self):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            model = SchemeOfWorkContextModel.get_context_model(self.fake_db, 127671112711, 67, 99, fake_ctx.auth_user_id)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_context_model"
                , (99,)
                , None
                , handle_log_info)
                
            self.assertEqual(0, model.id)
            #self.assertEqual(None, model.get("parent_id"))
            self.assertEqual(0, model.created_by_id)
            self.assertEqual(1, model.published)
            self.assertEqual("published", model.published_state)


    def test__should_call__select__return_single_item(self):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = [(6, "Lorem ipsum dolor sit amet", 12, 1, int(STATE.DRAFT))]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            model = SchemeOfWorkContextModel.get_context_model(self.fake_db, 127671112711, 67, 6, fake_ctx.auth_user_id)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_context_model"
                , (6,)
                , None
                , handle_log_info)
                 
            self.assertEqual(6, model.id)
            self.assertEqual("Lorem ipsum dolor sit amet", model.name)
            #self.assertEqual(None, model.parent_id)
            #self.assertEqual(0, model.topic_id)
            self.assertEqual(1, model.created_by_id)
            self.assertEqual(32, model.published)
            self.assertEqual("unpublished", model.published_state)




