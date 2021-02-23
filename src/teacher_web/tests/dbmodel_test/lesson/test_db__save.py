from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess, handle_log_info
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model.save(self.fake_db, model, 99)


    def test_should_call_update_with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, "")
    
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                Model.save(self.fake_db, model)


    def test_should_call__copy_objective_ids__when_copying(self, mock_auth_user):
         # arrange
        model = Model(0, "CPU and RAM")
        
        model.is_copy = MagicMock(return_value=True)

        # Mock functions not being tested
        
        LessonDataAccess._upsert_related_topic_ids = MagicMock()
        LessonDataAccess._upsert_pathway_objective_ids = MagicMock()
        LessonDataAccess._upsert_pathway_ks123_ids = MagicMock()
        LessonDataAccess._upsert_key_words = MagicMock()
        LessonDataAccess._copy_objective_ids = Mock()

        expected_result = (341,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published = STATE.PUBLISH)
            
            # assert
            
            LessonDataAccess._copy_objective_ids.assert_called()
            
            self.assertEqual(341, actual_result.id)


    def test_should_not_call__copy_objective_ids__when_not_copying(self, mock_auth_user):
         # arrange
        model = Model(0, "CPU and RAM")
        model.is_copy = Mock(return_value=False)

        # Mock functions not being tested
        
        LessonDataAccess._upsert_related_topic_ids = Mock()
        LessonDataAccess._upsert_pathway_objective_ids = Mock()
        LessonDataAccess._upsert_pathway_ks123_ids = Mock()
        LessonDataAccess._upsert_key_words = Mock()
        LessonDataAccess._copy_objective_ids = MagicMock()

        expected_result = (454,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published = STATE.PUBLISH)
            
            # assert
            
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(454, actual_result.id)


    def test_should_call__update_with__is_new__false(self, mock_auth_user):
         # arrange
        model = Model(1, "CPU and RAM")
        
        # Mock functions not being tested
        LessonDataAccess._upsert_related_topic_ids = Mock()
        LessonDataAccess._upsert_pathway_objective_ids = Mock()
        LessonDataAccess._upsert_pathway_ks123_ids = Mock()
        LessonDataAccess._copy_objective_ids = Mock()


        expected_result = model.id

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published=STATE.PUBLISH)
            
            # assert
            
            ExecHelper.update.assert_called_with(
                self.fake_db, 
                'lesson__update'
                , (1, 'CPU and RAM', '', 1, 0, 0, 0, 0, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                ,handle_log_info)

            # check subsequent functions where called
            
            LessonDataAccess._upsert_related_topic_ids.assert_called()
            LessonDataAccess._upsert_pathway_objective_ids.assert_called()
            LessonDataAccess._upsert_pathway_ks123_ids.assert_called()
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(expected_result, actual_result.id)


    def test_should_call__insert__when__is_new__true(self, mock_auth_user):
        # arrange

        model = Model(0, "")
        model.created = '2021-01-24 07:18:18.677084'
        

        # mock functions not being tested    
        LessonDataAccess._upsert_related_topic_ids = MagicMock()
        LessonDataAccess._upsert_pathway_objective_ids = MagicMock()
        LessonDataAccess._upsert_pathway_ks123_ids = MagicMock()
        LessonDataAccess._copy_objective_ids = MagicMock()
        LessonDataAccess._copy_objective_ids.assert_not_called()

        expected_result = (876,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published = STATE.PUBLISH)
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db, 
                'lesson__insert'
                , (0, '', '', 1, 0, 0, 0, 0, int(STATE.PUBLISH), 0, '2021-01-24 07:18:18.677084')
                , handle_log_info)

            # check subsequent functions where called
            
            LessonDataAccess._upsert_related_topic_ids.assert_called()
            LessonDataAccess._upsert_pathway_objective_ids.assert_called()
            LessonDataAccess._upsert_pathway_ks123_ids.assert_called()
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(876, actual_result.id)


    def test_should_call__delete__when__is_new__false__and__published_is_2(self, mock_auth_user):
        # arrange

        model = Model(23, "")
        
        # mock functions not being tested    
        LessonDataAccess._upsert_related_topic_ids = MagicMock()
        LessonDataAccess._upsert_pathway_objective_ids = MagicMock()
        LessonDataAccess._upsert_pathway_ks123_ids = MagicMock()
        LessonDataAccess._copy_objective_ids = MagicMock()

        expected_result = model.id

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, auth_user=mock_auth_user, published=STATE.DELETE)

            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                'lesson__delete'
                , (23, mock_auth_user.auth_user_id)
                , handle_log_info)

            # check subsequent functions where called
            
            LessonDataAccess._upsert_related_topic_ids.assert_not_called()
            LessonDataAccess._upsert_pathway_objective_ids.assert_not_called()
            LessonDataAccess._upsert_pathway_ks123_ids.assert_not_called()
            LessonDataAccess._copy_objective_ids.assert_not_called()

            self.assertEqual(expected_result, actual_result.id)
