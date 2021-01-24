from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
from tests.viewmodel_test.viewmodel_testcase import ViewModelTestCase
from app.lessons.viewmodels import LessonIndexViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel as Model, LessonFilter
from shared.models.cls_teacher_permission import TeacherPermissionModel


class test_viewmodel_LessonIndexModelViewModel(ViewModelTestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_404_if_scheme_of_work_not_found(self):
        
        # arrange
        
        data_to_return = []
        with patch.object(SchemeOfWorkModel, "get_schemeofwork_name_only", return_value=None):
            with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")]):
                with patch.object(Model, "get_filtered", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    self.mock_request = Mock()
                    self.mock_request.method = "GET"

                    # act
                    with self.assertRaises(Http404):
                        self.viewmodel = ViewModel(db=db, request=self.mock_request, page=1, pagesize=10, pagesize_options=[5,10,20,40], scheme_of_work_id=999, keyword_search="", auth_user=99)

                        self.assertEqual("", self.viewmodel.error_message)
                        
                        # assert functions was called
                        Model.get_filtered.assert_called()

                        SchemeOfWorkModel.get_options.assert_called()
                
                        self.assertEqual(0, len(self.viewmodel.model))
                        
                        self.assertEqual("", self.viewmodel.error_message)


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange

        data_to_return = []
        with patch.object(SchemeOfWorkModel, "get_schemeofwork_name_only", return_value="Varum dosctes"):
            with patch.object(SchemeOfWorkModel, "get_options", return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")]):
                
                with patch.object(Model, "get_filtered", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    self.mock_request = Mock()
                    self.mock_request.method = "GET"
                    
                    # act
                    self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=83, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=99)

                    # assert functions was called
                    
                    Model.get_filtered.assert_called()

                    self.assertEqual(0, len(self.viewmodel.model))

                    self.assertEqual("", self.viewmodel.error_message)

                    self.assertViewModelContent(self.viewmodel
                        , ""
                        , "Varum dosctes"
                        , "Lessons"
                        , {}
                    )


    def test_init_called_fetch__single_row(self):
        
        # arrange
        SchemeOfWorkModel.get_schemeofwork_name_only = Mock(return_value="Varum dosctes")
        SchemeOfWorkModel.get_options = Mock(return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")])
        
        data_to_return = [Model(56)]
        with patch.object(Model, "get_filtered", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_request = Mock()
            self.mock_request.method = "GET"

            # act
            self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=75, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=99)


            # assert functions was called

            self.assertEqual("", self.viewmodel.error_message)

            Model.get_filtered.assert_called()

            self.assertEqual(1, len(self.viewmodel.model))

            self.assertViewModelContent(self.viewmodel
                , ""
                , "Varum dosctes"
                , "Lessons"
                , {}
            )


    def test_init_called_fetch__should_return_multiple_rows(self):
        
        # arrange
        SchemeOfWorkModel.get_schemeofwork_name_only = Mock(return_value="Varum dosctes")
        SchemeOfWorkModel.get_options = Mock(return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")])
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        with patch.object(Model, "get_filtered", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_request = Mock()
            self.mock_request.method = "GET"

            # act
            self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=96, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=99)

            # assert functions was called
            
            self.assertEqual("", self.viewmodel.error_message)

            Model.get_filtered.assert_called_with(db, 96, self.viewmodel.search_criteria, 99)

            self.assertEqual(3, len(self.viewmodel.model))


            self.assertViewModelContent(self.viewmodel
                , ""
                , "Varum dosctes"
                , "Lessons"
                , {}
            )


    
    def test_init_called_fetch__should_return__multiple_rows__with_post(self):
        
        # arrange
        SchemeOfWorkModel.get_schemeofwork_name_only = Mock(return_value="Varum dosctes")
        SchemeOfWorkModel.get_options = Mock(return_value=[SchemeOfWorkModel(101, "Test 1"),SchemeOfWorkModel(102, "Test 2"),SchemeOfWorkModel(103, "Test 3")])
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        with patch.object(Model, "get_filtered", return_value=data_to_return):
                        
            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_request = Mock()
            self.mock_request.method = "POST"
            self.mock_request.POST = { "page": 4, "pagesize": 5, "page_direction": 1 }

            # act

            self.viewmodel = ViewModel(db=db, request=self.mock_request, scheme_of_work_id=96, page=1, pagesize=10, pagesize_options=[5,10,20,40], keyword_search="", auth_user=99)

            # assert functions was called
            
            self.assertEqual("", self.viewmodel.error_message)

            Model.get_filtered.assert_called_with(db, 96, self.viewmodel.search_criteria, 99)

            self.assertEqual(3, len(self.viewmodel.model))

            self.assertViewModelContent(self.viewmodel
                , ""
                , "Varum dosctes"
                , "Lessons"
                , {}
            )
