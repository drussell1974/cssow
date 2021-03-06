from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from tests.viewmodel_test.viewmodel_testcase import ViewModelTestCase
from app.resources.viewmodels import ResourceIndexViewModel as ViewModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_resource import ResourceModel as Model
from shared.models.utils.breadcrumb_generator import BreadcrumbGenerator
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(BreadcrumbGenerator, "get_items", return_value=fake_breadcrumbs())
class test_viewmodel_GetAllViewModel(ViewModelTestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass

    
    def test_init_called_fetch__no_return_rows(self, mock_auth_user, mock_bc):
        
        # arrange
        
        data_to_return = []
        

        lesson = LessonModel(12)
        lesson.is_from_db = True

        with patch.object(LessonModel, 'get_model', return_value=lesson):
            with patch.object(Model, "get_all", return_value=data_to_return):

                db = MagicMock()
                db.cursor = MagicMock()

                mock_request = Mock()

                # act
                self.viewmodel = ViewModel(db=db, request=mock_request, lesson_id=99, scheme_of_work_id=12, auth_user=mock_auth_user)

                # assert functions was called
                Model.get_all.assert_called()
                self.assertEqual(0, len(self.viewmodel.model))
                
                self.assertViewModelContent(mock_request, self.viewmodel
                    , ""
                    , ""
                    , "Lesson"
                    , {}
                )



    def test_init_called_fetch__single_row(self, mock_auth_user, mock_bc):
        
        # arrange
        
        data_to_return = [Model(56)]
        

        lesson = LessonModel(12)
        lesson.is_from_db = True

        with patch.object(LessonModel, 'get_model', return_value=lesson):
            with patch.object(Model, "get_all", return_value=data_to_return):

                db = MagicMock()
                db.cursor = MagicMock()

                mock_request = Mock()

                # act
                self.viewmodel = ViewModel(db=db, request=mock_request, lesson_id=92, scheme_of_work_id=12, auth_user=mock_auth_user)

                # assert functions was called
                Model.get_all.assert_called()
                self.assertEqual(1, len(self.viewmodel.model))

                self.assertViewModelContent(mock_request, self.viewmodel
                    , ""
                    , ""
                    , "Lesson"
                    , {}
                )


    
    def test_init_called_fetch__multiple_rows(self, mock_auth_user, mock_bc):
        
        # arrange
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        lesson = LessonModel(12)
        lesson.is_from_db = True

        with patch.object(LessonModel, 'get_model', return_value=lesson):
            with patch.object(Model, "get_all", return_value=data_to_return):

                db = MagicMock()
                db.cursor = MagicMock()

                mock_request = Mock()

                # act
                self.viewmodel = ViewModel(db=db, request=mock_request, lesson_id=20, scheme_of_work_id=100, auth_user=mock_auth_user)

                # assert functions was called
                Model.get_all.assert_called()
                self.assertEqual(3, len(self.viewmodel.model))

                self.assertViewModelContent(mock_request, self.viewmodel
                    , ""
                    , ""
                    , "Lesson"
                    , {}
                )
