from unittest import TestCase
from shared.models.cls_department import DepartmentModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

class test_DepartmentDataAccess___insert(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__save__with_exception(self):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "insert", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.save(self.fake_db, 99, "Lorum ipsum", auth_user = 6079)
            

    def test__should_call__save__if_valid(self):
        # arrange
        expected_result = [99]

        fake_model = Model(0, "Lorum ipsum")
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = True

        with patch.object(ExecHelper, "insert", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = 6079)
            
            # assert

            ExecHelper.insert.assert_called_with(self.fake_db,
                'department__insert'
                , (0, "Lorum ipsum", 6080, 0, "2021-01-24 07:20:01.907507", 6079)
                , handle_log_info)

            self.assertEqual(99, result.id)


    def test__should_not_call__save__if_not_valid(self):
        # arrange
        expected_result = [99]

        fake_model = Model(0, "Lorum ipsum")
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = False


        with patch.object(ExecHelper, "insert", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = 6079)
            
            # assert

            ExecHelper.insert.assert_not_called()

            self.assertEqual(0, result.id)
