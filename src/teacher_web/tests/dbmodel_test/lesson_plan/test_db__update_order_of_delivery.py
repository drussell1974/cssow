from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

import shared.models.cls_lessonplan as test_context 

# create test context

update_order_of_delivery = test_context.update_order_of_delivery
handle_log_info = test_context.handle_log_info
Model = test_context.LessonPlanModel

class test_db__update_order_of_delivery(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
    def tearDown(self):
        pass

    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, title="How to make more unit tests", description="This will go bang!", lesson_id=454)

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                update_order_of_delivery(self.fake_db, model.id, model.lesson_id, order_of_delivery_id=9)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = Model(1334, title="CPU and the FDE cycle", description="A practical lesson for the FDE cycle", lesson_id=454)
        model.order_of_delivery = 11

        expected_result = [(1)]

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = update_order_of_delivery(self.fake_db, model.id, model.lesson_id, order_of_delivery_id=14)
            
            # assert
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "UPDATE sow_lesson_plan SET order_of_delivery_id = 14 WHERE id = 1334 AND lesson_id = 454;"
                , log_info=handle_log_info)
