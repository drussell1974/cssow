from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from api.institutes.viewmodels import InstituteGetScheduleViewModel as ViewModel
from shared.models.core.context import Ctx
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model
from tests.test_helpers.mocks import fake_ctx_model


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_InstituteGetScheduleViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_ctx=mock_ctx_model)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [Model(56, title="Vivamus at porta orci", class_name="Lorem Ipsum", start_date=None, class_code="ABCDEF", scheme_of_work_id=11, lesson_id=220)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_ctx=mock_ctx_model)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [
            Model(56, title="Vivamus at porta orci", class_name="Tic", start_date=None, class_code="ABCDEF", scheme_of_work_id=11, lesson_id=220),
            Model(57, title="Vivamus at porta orci", class_name="Tac", start_date=None, class_code="BBCDEF", scheme_of_work_id=11, lesson_id=220),
            Model(58, title="Vivamus at porta orci", class_name="Toe", start_date=None, class_code="CBCDEF", scheme_of_work_id=76, lesson_id=349)
        ]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_ctx=mock_ctx_model)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))