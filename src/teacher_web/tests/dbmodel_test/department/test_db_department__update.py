from unittest import TestCase
from shared.models.cls_department import DepartmentModel as Model, handle_log_info
from shared.models.cls_institute import InstituteModel
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *


class test_DepartmentDataAccess___update(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__save__with_exception(self):

        # arrange

        mock_ctx = fake_ctx_model()

        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "insert", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.save(self.fake_db, 99, "Lorum ipsum", auth_user = mock_ctx)
            

    def test__should_call__save__if_valid(self):
        # arrange
        
        mock_ctx = fake_ctx_model()

        expected_result = [101]

        fake_model = Model(101, "Lorum ipsum", hod_id=56, institute = InstituteModel(12767111276711, "Lorum ipsum"))
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = True

        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = mock_ctx)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db,
                'department__update'
                , (101, 'Lorum ipsum', 12767111276711, int(STATE.PUBLISH), mock_ctx.auth_user_id)
                , handle_log_info)

            self.assertEqual(101, result.id)


    def test__should_not_call__save__if_not_valid(self):
        # arrange

        mock_ctx = fake_ctx_model()
        
        expected_result = [99]
        
        fake_model = Model(99, "Lorum ipsum",  hod_id=56, institute = InstituteModel(12767111276711, "Lorum ipsum"))
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = False

        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = mock_ctx)
            
            # assert

            ExecHelper.update.not_called()

            self.assertEqual(99, result.id)
            self.assertFalse(result.is_valid)
