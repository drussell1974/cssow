from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db___save_keywords(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.autocommit = True
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model._save_keywords(self.fake_db, model, auth_user_id=99)
    
    
    def test_should_call__reinsert__key_words(self, mock_auth_user):
         # arrange
        model = Model(10, "", scheme_of_work_id = 14)
        
        model.key_words = [
            KeywordModel(id_=12, term="CPU", definition="", scheme_of_work_id=14), 
            KeywordModel(id_=13, term="FDE", definition="", scheme_of_work_id=14)
        ]
        
        expected_rows = []

        with patch.object(ExecHelper, 'insert', return_value=expected_rows):
            # act

            actual_result = Model.save_keywords(self.fake_db, model, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.insert.assert_called()

            ExecHelper.insert.assert_called_with(self.fake_db, 
             'lesson__insert_keywords'
             , (13, 10, 14, mock_auth_user.id)
             , handle_log_info)

        self.assertEqual([], actual_result)

    
    
    def test_should_call__reinsert__key_words__insert_new(self, mock_auth_user):
         # arrange
        model = Model(79, "", scheme_of_work_id = 13)
        
        model.key_words = [KeywordModel(id_ = 12, term="CPU", definition="", scheme_of_work_id=13)]
        
        expected_result = []

        with patch.object(ExecHelper, 'insert', return_value=[]):
            # act

            actual_result = Model.save_keywords(self.fake_db, model, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.insert.assert_called()

            ExecHelper.insert.assert_called_with(self.fake_db, 
             'lesson__insert_keywords'
             , (12, 79, 13, mock_auth_user.id)
             , handle_log_info)

        self.assertEqual(actual_result, expected_result)
    