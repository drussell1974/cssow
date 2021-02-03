from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info

publish_item = Model.publish_item


class test_db__publish_item(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                publish_item(self.fake_db, 999, 99)


    def test_should_call__update(self):
         # arrange
        model = Model(123, "CPU, RAM and ", lesson_id = 101)
        
        expected_result = []

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = publish_item(self.fake_db, 123, 78, 99)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db, 
            'lesson_learning_objective__publish_item'
            , (123, 0, 78, 1, 99)
            )
            
            self.assertEqual(len(expected_result), len(actual_result))

