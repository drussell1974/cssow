from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
from tests.viewmodel_test.viewmodel_testcase import ViewModelTestCase
from app.lessons.viewmodels import LessonIndexViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel as Model, LessonFilter
from shared.models.utils.breadcrumb_generator import BreadcrumbGenerator
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(BreadcrumbGenerator, "get_items", return_value=fake_breadcrumbs())
class test_viewmodel_LessonIndexModelViewModel(ViewModelTestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_404_if_scheme_of_work_not_found(self, mock_auth_user, mock_bc):
        
        # arrange
        
        data_to_return = []
        with patch.object(SchemeOfWorkModel, "get_schemeofwork_name_only", return_value=None):
            with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)]):
                with patch.object(Model, "get_filtered", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    self.mock_request = Mock()
                    self.mock_request.method = "GET"

                    # act
                    with self.assertRaises(Http404):
                        self.viewmodel = ViewModel(db=db, request=self.mock_request, page=1, pagesize=10, pagesize_options=[5,10,20,40], scheme_of_work_id=999, keyword_search="", auth_user=mock_auth_user)

                        self.assertEqual("", self.viewmodel.error_message)
                        
                        # assert functions was called
                        Model.get_filtered.assert_called()

                        SchemeOfWorkModel.get_options.assert_called()
                
                        self.assertEqual(0, len(self.viewmodel.model))
                        
                        self.assertEqual("", self.viewmodel.error_message)


    def test_init_called_fetch__no_return_rows(self, mock_auth_user, mock_bc):
        
        # arrange

        mock_auth_user.institute_id = 12767111276711
        mock_auth_user.department_id = 67
        
        data_to_return = []
        with patch.object(SchemeOfWorkModel, "get_schemeofwork_name_only", return_value="Varum dosctes"):
            with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)]):
                
                with patch.object(Model, "get_filtered", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    self.mock_request = Mock()
                    self.mock_request.method = "GET"
                    
                    # act
                    self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=83, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=mock_auth_user)

                    # assert functions was called
                    
                    Model.get_filtered.assert_called()

                    self.assertEqual(0, len(self.viewmodel.data))

                    self.assertEqual("", self.viewmodel.error_message)

                    self.assertViewModelContent(self.mock_request, self.viewmodel
                        , ""
                        , "Varum dosctes"
                        , "Scheme of work"
                        , {}
                    )


    def test_init_called_fetch__single_row(self, mock_auth_user, mock_bc):
        
        # arrange
        mock_auth_user.institute_id = 12767111276711
        mock_auth_user.department_id = 67
        
        SchemeOfWorkModel.get_schemeofwork_name_only = Mock(return_value="Varum dosctes")
        SchemeOfWorkModel.get_options = Mock(return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)])
        
        data_to_return = [Model(56)]
        with patch.object(Model, "get_filtered", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_request = Mock()
            self.mock_request.method = "GET"

            # act
            self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=75, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=mock_auth_user)


            # assert functions was called

            self.assertEqual("", self.viewmodel.error_message)

            Model.get_filtered.assert_called()

            self.assertEqual(1, len(self.viewmodel.data))

            self.assertViewModelContent(self.mock_request, self.viewmodel
                , ""
                , "Varum dosctes"
                , "Scheme of work"
                , {}
            )


    def test_init_called_fetch__should_return_multiple_rows(self, mock_auth_user, mock_bc):
        
        # arrange
        
        mock_auth_user.institute_id = 12767111276711
        mock_auth_user.department_id = 67

        SchemeOfWorkModel.get_schemeofwork_name_only = Mock(return_value="Varum dosctes")
        SchemeOfWorkModel.get_options = Mock(return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)])
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        with patch.object(Model, "get_filtered", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_request = Mock()
            self.mock_request.method = "GET"

            # act
            self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=96, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=mock_auth_user)

            # assert functions was called
            
            self.assertEqual("", self.viewmodel.error_message)

            Model.get_filtered.assert_called_with(db, 96, self.viewmodel.search_criteria, mock_auth_user)

            self.assertEqual(3, len(self.viewmodel.data))


            self.assertViewModelContent(self.mock_request, self.viewmodel
                , ""
                , "Varum dosctes"
                , "Scheme of work"
                , {}
            )


    
    def test_init_called_fetch__should_return__multiple_rows__with_post(self, mock_auth_user, mock_bc):
        
        # arrange

        mock_auth_user.institute_id = 12767111276711
        mock_auth_user.department_id = 67

        SchemeOfWorkModel.get_schemeofwork_name_only = Mock(return_value="Varum dosctes")
        SchemeOfWorkModel.get_options = Mock(return_value=[SchemeOfWorkModel(101, name="Lorem1", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(102, name="Lorem2", study_duration=2, start_study_in_year=10),SchemeOfWorkModel(103, name="Lorem3", study_duration=2, start_study_in_year=10)])
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        with patch.object(Model, "get_filtered", return_value=data_to_return):
                        
            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_request = Mock()
            self.mock_request.method = "POST"
            self.mock_request.POST = { "page": 4, "pagesize": 5, "page_direction": 1 }

            # act

            self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=96, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=mock_auth_user)

            # assert functions was called
            
            self.assertEqual("", self.viewmodel.error_message)

            Model.get_filtered.assert_called_with(db, 96, self.viewmodel.search_criteria, mock_auth_user)

            self.assertEqual(3, len(self.viewmodel.data))

            self.assertViewModelContent(self.mock_request, self.viewmodel
                , ""
                , "Varum dosctes"
                , "Scheme of work"
                , {}
            )
