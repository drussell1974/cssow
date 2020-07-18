from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
import shared.models.cls_lessonplan as test_context 

# create test context

save = test_context.save
handle_log_info = test_context.handle_log_info
Model = test_context.LessonPlanModel

class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, title="Data Representation", description="Covering Sound, Image, Binary", lesson_id = 34)
        model.is_new = Mock(return_value=True)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(12, title="Data Representation", description="Covering Sound, Image, Binary", lesson_id = 34)
        model.is_new = Mock(return_value=False)
        
        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save(self.fake_db, model)


    def test_should_call_execCRUDSql__update_with__is_new__false(self):
         # arrange
        model = Model(123, title="Data Representation", description="Covering Sound, Image, Binary", lesson_id = 34)
        model.is_new = Mock(return_value=False)

        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "UPDATE sow_lesson_plan SET lesson_id = 34, order_of_delivery_id = 0, title = 'Data Representation', description = 'Covering Sound, Image, Binary', duration_minutes = 0, task_icon = '' WHERE id = 123;"
            , log_info=handle_log_info)
            
            self.assertEqual(expected_result, actual_result.id)


    def test_should_call_execCRUDSql__insert__when__is_new__true(self):
        # arrange

        model = Model(0, title="Data Representation", description="Covering Sound, Image, Binary", lesson_id = 34)
        model.is_new = Mock(return_value=True)
        
        expected_result = model.id

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model)

            # assert

            ExecHelper.execCRUDSql.assert_called_with(
                self.fake_db, 
                "INSERT INTO sow_lesson_plan (lesson_id, order_of_delivery_id, title, description, duration_minutes, task_icon) VALUES (34, 0, 'Data Representation', 'Covering Sound, Image, Binary', 0, '');" 
                , log_info=handle_log_info)

            self.assertEqual(expected_result, actual_result.id)