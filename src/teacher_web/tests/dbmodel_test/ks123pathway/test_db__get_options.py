from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from unittest import skip
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_ks123pathway import KS123PathwayModel, handle_log_info
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(TeacherPermissionModel, "get_model", return_value=fake_teacher_permission_model())
class test_db__get_options(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_auth_user, mock_teacher_permission):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                KS123PathwayModel.get_options(self.fake_db, year_id = 1, topic_id = 1)
          

    def test__should_call_select__return_no_items(self, mock_auth_user, mock_teacher_permission):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KS123PathwayModel.get_options(self.fake_db, key_stage_id = 3, topic_id = 2, auth_user=mock_auth_user)
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_options'
                , (3, 2, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user, mock_teacher_permission):
        # arrange
        expected_result = [(1,"Recognises that digital content can be represented in many forms. (AB) (GE)")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KS123PathwayModel.get_options(self.fake_db, key_stage_id = 4, topic_id = 3, auth_user=fake_ctx_model())
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_options'
                , (4, 3, int(STATE.PUBLISH_INTERNAL), 6079)
                ,  []
                , handle_log_info)

            self.assertEqual(1, len(rows))
            self.assertEqual("Recognises that digital content can be represented in many forms. (AB) (GE)", rows[0].objective, "First item not as expected")
            
            
    def test__should_call_select__return_multiple_items(self, mock_auth_user, mock_teacher_permission):
        # arrange
        expected_result = [
            (10,"Designs solutions (algorithms) that use repetition and two-way selection i.e. if, then and else. (AL)"),
            (74,"Makes appropriate improvements to solutions based on feedback received, and can comment on the success of the solution. (EV)"),
            (99,"Uses logical reasoning to predict outputs, showing an awareness of inputs. (AL)")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            rows = KS123PathwayModel.get_options(self.fake_db, key_stage_id = 5, topic_id = 4, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_options'
                , (5, 4, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(rows))

            self.assertEqual("Designs solutions (algorithms) that use repetition and two-way selection i.e. if, then and else. (AL)", rows[0].objective, "First item not as expected")
            self.assertEqual("Uses logical reasoning to predict outputs, showing an awareness of inputs. (AL)", rows[2].objective, "Last item not as expected")

