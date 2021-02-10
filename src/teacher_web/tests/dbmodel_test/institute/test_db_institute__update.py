from unittest import TestCase, skip
from shared.models.cls_institute import InstituteModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@skip("not implemented")
@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_InstituteDataAccess___update(TestCase):

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
                Model.save(self.fake_db, 99, "Lorum ipsum", auth_user = mock_auth_user)
            

    def test__should_call__save__if_valid(self, mock_auth_user):
        # arrange
        expected_result = [101]

        fake_model = Model(101, "Lorum ipsum")
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = True

        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db,
                'institute__update'
                , (101, 'Lorum ipsum', 6080, mock_auth_user.id)
                , handle_log_info)

            self.assertEqual(101, result.id)


    def test__should_not_call__save__if_not_valid(self, mock_auth_user):
        # arrange
        expected_result = [99]

        fake_model = Model(99, "Lorum ipsum")
        fake_model.created = "2021-01-24 07:20:01.907507"
        fake_model.is_valid = False

        with patch.object(ExecHelper, "update", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.update.not_called()

            self.assertEqual(99, result.id)
            self.assertFalse(result.is_valid)
