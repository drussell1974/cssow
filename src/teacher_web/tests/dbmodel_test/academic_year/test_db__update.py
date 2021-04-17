from datetime import datetime
from unittest import TestCase
from shared.models.cls_academic_year import AcademicYearModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
#from shared.models.cls_institute import InstituteModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

class test_AcademicYearDataAccess___update(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__save__with_exception(self):

        # arrange
        fake_ctx = fake_ctx_model()
        
        fake_model = Model(2020, "2020-01-24", "2021-01-24", is_from_db=True, auth_ctx=fake_ctx)
        fake_model.is_valid = True

        expected_result = KeyError('Bang')

        with patch.object(ExecHelper, "update", side_effect=expected_result):
            # act and assert
            with self.assertRaises(KeyError):
                Model.save(self.fake_db, fake_model, published=1, auth_ctx = fake_ctx)
            

    def test__should_call__save__if_valid(self):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = 2020

        fake_model = Model(2020, "2020-09-01", "2021-07-25", is_from_db=True, auth_ctx=fake_ctx)
        fake_model.is_valid = True

        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, published=1, auth_ctx=fake_ctx)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db,
                'academic_year__update'
                , (fake_model.id, datetime(2020, 9, 1, 0, 0), datetime(2021, 7, 25, 0, 0), 127671276711, int(STATE.PUBLISH), 6079)
                , handle_log_info)

            self.assertEqual(2020, result)


    def test__should_not_call__save__if_not_valid(self):
        # arrange
        expected_result = 2021

        fake_ctx = fake_ctx_model()

        fake_model = Model(2021, "2021-01-24", "2100-11-22", False, auth_ctx=fake_ctx)
        fake_model.is_valid = False


        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, published=1, auth_ctx = fake_ctx)
            
            # assert

            ExecHelper.update.assert_not_called()

            self.assertEqual("2021-01-24", result.start)
            self.assertEqual("2100-11-22", result.end)
