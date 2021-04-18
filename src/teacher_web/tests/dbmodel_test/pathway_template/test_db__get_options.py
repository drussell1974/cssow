from unittest import TestCase
from shared.models.cls_pathway_template import PathwayTemplateModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel
from tests.test_helpers.mocks import fake_ctx_model

#@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test__get_options(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange

        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_options(self.fake_db)
            

    def test__should_call__select__no_items(self):
        # arrange

        mock_auth_user = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_options(self.fake_db)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'pathway_template__get_options'
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows))
            self.assertEqual(("","- Select level taught up to -"), rows[0])


    def test__should_call__select__single_items(self):
        # arrange

        expected_result = [(1,"GCSE")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_options(self.fake_db)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'pathway_template__get_options'
                , []
                , handle_log_info)

            self.assertEqual(2, len(rows))
            self.assertEqual(("","- Select level taught up to -"), rows[0])
            self.assertEqual((1,"GCSE"), rows[1])
            

    def test__should_call__select__multiple_items(self):
        # arrange

        mock_auth_user = fake_ctx_model()

        expected_result = [(1,"GCSE"), (2, "BTEC"), (3, "NVQ")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_options(self.fake_db)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'pathway_template__get_options'
                , []
                , handle_log_info)

            self.assertEqual(4, len(rows))

            self.assertEqual(("","- Select level taught up to -"), rows[0])
            self.assertEqual((1,"GCSE"), rows[1])

            self.assertEqual((3,"NVQ"), rows[len(rows)-1])
