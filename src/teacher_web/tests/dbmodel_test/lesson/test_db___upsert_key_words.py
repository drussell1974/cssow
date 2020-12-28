from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel, LessonDataAccess, handle_log_info

_save_keywords = LessonModel.save_keywords

class test_db___save_keywords(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.autocommit = True
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = LessonModel(0, "")

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                _save_keywords(self.fake_db, model, auth_user_id=99)
    
    
    def test_should_call__reinsert__key_words(self):
         # arrange
        model = LessonModel(10, "", scheme_of_work_id = 14)
        
        model.key_words = [
            KeywordModel(id_=12, term="CPU", definition="", scheme_of_work_id=14), 
            KeywordModel(id_=13, term="FDE", definition="", scheme_of_work_id=14)
        ]
        
        expected_rows = []

        with patch.object(ExecHelper, 'insert', return_value=expected_rows):
            # act

            actual_result = _save_keywords(self.fake_db, model, auth_user=6079)
            
            # assert
            ExecHelper.insert.assert_called()

            ExecHelper.insert.assert_called_with(self.fake_db, 
             'lesson__insert_keywords'
             , (13, 10, 14, 6079)
             , handle_log_info)

        self.assertEqual([], actual_result)

    
    
    def test_should_call__reinsert__key_words__insert_new(self):
         # arrange
        model = LessonModel(79, "", scheme_of_work_id = 13)
        
        model.key_words = [KeywordModel(id_ = 12, term="CPU", definition="", scheme_of_work_id=13)]
        
        expected_result = []

        with patch.object(ExecHelper, 'insert', return_value=[]):
            # act

            actual_result = _save_keywords(self.fake_db, model, auth_user=6079)
            
            # assert
            ExecHelper.insert.assert_called()

            ExecHelper.insert.assert_called_with(self.fake_db, 
             'lesson__insert_keywords'
             , (12, 79, 13, 6079)
             , handle_log_info)

        self.assertEqual(actual_result, expected_result)
    