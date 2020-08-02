from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

from shared.models.cls_lessonplan import LessonPlanModel as Model, LessonPlanDataAccess, handle_log_info

# create test context

delete = LessonPlanDataAccess.delete

@skip("Deprecated. No longer used.")
class test_db__delete(TestCase):


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
                delete(self.fake_db, model.id)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = Model(1334, title="CPU and the FDE cycle", description="A practical lesson for the FDE cycle", lesson_id=454)

        expected_result = [(1)]

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = delete(self.fake_db, model.id)
            
            # assert
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "DELETE FROM sow_lesson_plan WHERE id = 1334;"
                , log_info=handle_log_info)
