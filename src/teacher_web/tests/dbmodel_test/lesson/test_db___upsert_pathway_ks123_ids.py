from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, LessonDataAccess, handle_log_info
from shared.models.cls_ks123pathway import KS123PathwayModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__upsert_pathway_ks123_ids(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = LessonModel(0, "")
        model.pathway_ks123_ids = [KS123PathwayModel(201, objective="", ctx=mock_auth_user)]

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                results = []
                LessonModel.save_ks123pathway(self.fake_db, model=model, auth_user=mock_auth_user)
    
    
    def test_should_call__reinsert__pathway_ks123_ids(self, mock_auth_user):
         # arrange
        model = LessonModel(10, "")
        model.pathway_ks123_ids = [KS123PathwayModel(201, objective="", ctx=mock_auth_user), KS123PathwayModel(202, objective="", ctx=mock_auth_user)]
        expected_result = []

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = LessonModel.save_ks123pathway(self.fake_db, model, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.insert.assert_called()

            ExecHelper.insert.assert_called_with(self.fake_db, 
             'lesson__insert_ks123_pathway'
             , (10, 202, mock_auth_user.auth_user_id)
             , handle_log_info)

        self.assertEqual(actual_result, expected_result)
    