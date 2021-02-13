from unittest import TestCase, skip, skip
from shared.models.cls_institute import InstituteModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_institute___delete(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__save__with_exception(self, mock_ctx):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "delete", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.save(self.fake_db, Mock(id=99, name="Lorum ipsum", published=2), "Lorum ipsum", auth_user = mock_ctx)
            

    def test__should_call__delete__if_valid(self, mock_ctx):
        # arrange
        expected_result = [99]

        fake_model = Model(101, "Lorum ipsum")
        fake_model.published = 2
        fake_model.created = "2021-01-24 07:20:01.907507"
    
        with patch.object(ExecHelper, "delete", return_value=expected_result):
                
            # act
            
            result = Model.save(self.fake_db, fake_model, 6080, auth_user = mock_ctx)
            
            # assert

            ExecHelper.delete.assert_called_with(self.fake_db,
                'institute__delete'
                , (101, mock_ctx.id)
                , handle_log_info)

            self.assertEqual(101, result.id)
