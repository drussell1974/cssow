from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.eventlogs.viewmodels import EventLogIndexViewModel as ViewModel
from shared.models.core.log_type import LOG_TYPE
from shared.models.cls_eventlog import EventLogModel as Model, EventLogFilter
from shared.models.cls_teacher_permission import TeacherPermissionModel

class fake_settings:
    MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS = 7
    MAX_NUMBER_OF_DAYS_TO_KEEP_LOGS = 30
    PAGER = {
        "default":{
            "page": 1,
            "pagesize": 20,
            "pagesize_options": [5,10,25,50,100]
        }
    }

class test_viewmodel_IndexViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        self.fake_settings = fake_settings()

    def tearDown(self):
        pass


    def test_view__request_method_get(self):
        
        # arrange
        mock_request = Mock()
        mock_request.method = "GET"
        mock_request.GET = { "page": 1, "pagesize":20 }

        on_get_all__data_to_return = [
            Model(101, 
                created="23-08-2020 02:31:23",
                event_type="INFO",
                message="Mauris dignissim mi at lorem varius condimentum.",
                details="Quisque ut magna eleifend, blandit lorem vitae, molestie magna. Maecenas suscipit, leo vitae pretium lobortis, felis augue euismod ex, nec maximus ex orci eu libero. Nullam fringilla mauris tellus, at consectetur est convallis nec. Curabitur in massa sed nisi egestas efficitur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nibh eros, imperdiet vel pharetra id, finibus id diam. Sed nibh libero, faucibus eget tristique ac, sollicitudin a ante. Mauris nulla felis, cursus eu nibh et, lobortis imperdiet leo. Morbi eu justo et turpis elementum mattis. Cras et magna sit amet leo vehicula posuere tempor eget ante. Phasellus in dui sed lectus consectetur tempor.",
                category="lesson",
                subcategory="save"
            ),
            Model(102, 
                created="2020-08-23 03:48:01", 
                event_type=LOG_TYPE.Warning, 
                message="Validation errors", 
                details="Donec ut viverra metus. Curabitur a massa in leo consequat tempus. Curabitur eget tristique diam. Morbi at nunc id ipsum volutpat porttitor sit amet ac tortor. In diam nunc, mollis nec pretium id, convallis id ipsum. Sed quis eros id justo suscipit euismod sit amet vel ante.", 
                category="V",
                subcategory="W"),
            Model(103, 
                created="2019-11-23 05:16:19", 
                event_type=LOG_TYPE.Error, 
                message="malesuada", 
                details="Vivamus auctor feugiat dolor vitae malesuada. Ut maximus nulla sem, non sagittis tortor blandit maximus. Sed suscipit porta dolor, vitae consectetur sem fringilla non. Phasellus imperdiet at dui non malesuada.", 
                category="lessonviewmodel",
                subcategory="view error")
            ]
        
        with patch.object(EventLogFilter, "is_valid", return_value=True):
            with patch.object(Model, "get_all", return_value=on_get_all__data_to_return):

                # act

                test_context = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=13, settings=self.fake_settings, auth_user=6079)
                test_context.view()
                            
                # assert functions was called
                
                Model.get_all.assert_called_with(self.mock_db, 13, test_context.search_criteria, 6079)

                self.assertEqual(3, len(test_context.model))

                self.assertEqual(101, test_context.model[0].id)
                self.assertEqual("INFO", test_context.model[0].event_type)
                self.assertEqual("Mauris dignissim mi at lorem varius condimentum.", test_context.model[0].message)
                self.assertEqual("Quisque ut magna eleifend, blandit lorem vitae, molestie magna. Maecenas suscipit, leo vitae pretium lobortis, felis augue euismod ex, nec maximus ex orci eu libero. Nullam fringilla mauris tellus, at consectetur est convallis nec. Curabitur in massa sed nisi egestas efficitur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nibh eros, imperdiet vel pharetra id, finibus id diam. Sed nibh libero, faucibus eget tristique ac, sollicitudin a ante. Mauris nulla felis, cursus eu nibh et, lobortis imperdiet leo. Morbi eu justo et turpis elementum mattis. Cras et magna sit amet leo vehicula posuere tempor eget ante. Phasellus in dui sed lectus consectetur tempor.", test_context.model[0].details)
                self.assertEqual("lesson", test_context.model[0].category)
                self.assertEqual("save", test_context.model[0].subcategory)

                self.assertEqual(103, test_context.model[2].id)
                self.assertEqual(LOG_TYPE.Error, test_context.model[2].event_type)
                self.assertEqual("malesuada", test_context.model[2].message)
                self.assertEqual("Vivamus auctor feugiat dolor vitae malesuada. Ut maximus nulla sem, non sagittis tortor blandit maximus. Sed suscipit porta dolor, vitae consectetur sem fringilla non. Phasellus imperdiet at dui non malesuada.", test_context.model[2].details)
                self.assertEqual("lessonviewmodel", test_context.model[2].category)
                self.assertEqual("view error", test_context.model[2].subcategory)


    def test_view__request_method_post(self):
        
        # arrange
        
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
            "date_from":"",
            "date_to":"",
            "event_type":"8",
            "category":"",
            "subcategory":"",
            "page":"1",
            "pagesize":"20",
            "page_direction":"1"
        }

        on_get_all__data_to_return = [
            Model(104, 
                created="2020-08-23 03:48:01", 
                event_type=LOG_TYPE.Warning, 
                message="Validation errors", 
                details="Donec ut viverra metus. Curabitur a massa in leo consequat tempus. Curabitur eget tristique diam. Morbi at nunc id ipsum volutpat porttitor sit amet ac tortor. In diam nunc, mollis nec pretium id, convallis id ipsum. Sed quis eros id justo suscipit euismod sit amet vel ante.", 
                category="V",
                subcategory="W"),
            Model(105, 
                created="2019-11-23 05:16:19", 
                event_type=LOG_TYPE.Error, 
                message="malesuada", 
                details="Vivamus auctor feugiat dolor vitae malesuada. Ut maximus nulla sem, non sagittis tortor blandit maximus. Sed suscipit porta dolor, vitae consectetur sem fringilla non. Phasellus imperdiet at dui non malesuada.", 
                category="lessonviewmodel",
                subcategory="view error"),
            Model(106, 
                created="23-08-2020 02:31:23",
                event_type="INFO",
                message="Mauris dignissim mi at lorem varius condimentum.",
                details="Quisque ut magna eleifend, blandit lorem vitae, molestie magna. Maecenas suscipit, leo vitae pretium lobortis, felis augue euismod ex, nec maximus ex orci eu libero. Nullam fringilla mauris tellus, at consectetur est convallis nec. Curabitur in massa sed nisi egestas efficitur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nibh eros, imperdiet vel pharetra id, finibus id diam. Sed nibh libero, faucibus eget tristique ac, sollicitudin a ante. Mauris nulla felis, cursus eu nibh et, lobortis imperdiet leo. Morbi eu justo et turpis elementum mattis. Cras et magna sit amet leo vehicula posuere tempor eget ante. Phasellus in dui sed lectus consectetur tempor.",
                category="lesson",
                subcategory="update"
            )]
        
        
        with patch.object(EventLogFilter, "is_valid", return_value=True):
            with patch.object(Model, "get_all", return_value=on_get_all__data_to_return):

                # act

                test_context = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=15, settings=self.fake_settings, auth_user=6079)
                test_context.view()
                            
                # assert functions was called
                
                Model.get_all.assert_called_with(self.mock_db, 15, test_context.search_criteria, 6079)

                self.assertEqual(3, len(test_context.model))

                self.assertEqual(104, test_context.model[0].id)
                self.assertEqual(LOG_TYPE.Warning, test_context.model[0].event_type)
                self.assertEqual("Validation errors", test_context.model[0].message)
                self.assertEqual("Donec ut viverra metus. Curabitur a massa in leo consequat tempus. Curabitur eget tristique diam. Morbi at nunc id ipsum volutpat porttitor sit amet ac tortor. In diam nunc, mollis nec pretium id, convallis id ipsum. Sed quis eros id justo suscipit euismod sit amet vel ante.", test_context.model[0].details)
                self.assertEqual("V", test_context.model[0].category)
                self.assertEqual("W", test_context.model[0].subcategory)

                self.assertEqual(106, test_context.model[2].id)
                self.assertEqual("INFO", test_context.model[2].event_type)
                self.assertEqual("Mauris dignissim mi at lorem varius condimentum.", test_context.model[2].message)
                self.assertEqual("Quisque ut magna eleifend, blandit lorem vitae, molestie magna. Maecenas suscipit, leo vitae pretium lobortis, felis augue euismod ex, nec maximus ex orci eu libero. Nullam fringilla mauris tellus, at consectetur est convallis nec. Curabitur in massa sed nisi egestas efficitur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nibh eros, imperdiet vel pharetra id, finibus id diam. Sed nibh libero, faucibus eget tristique ac, sollicitudin a ante. Mauris nulla felis, cursus eu nibh et, lobortis imperdiet leo. Morbi eu justo et turpis elementum mattis. Cras et magna sit amet leo vehicula posuere tempor eget ante. Phasellus in dui sed lectus consectetur tempor.", test_context.model[2].details)
                self.assertEqual("lesson", test_context.model[2].category)
                self.assertEqual("update", test_context.model[2].subcategory)


    def test_view__request_method_post__return_invalid(self):
        
        # arrange
        
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
            "date_from":"",
            "date_to":"",
            "event_type":"",
            "category":"",
            "subcategory":"",
            "page":"3",
            "pagesize":"20",
            "page_direction":"-1"
        }

        on_get_all__data_to_return = []
        
        
        with patch.object(EventLogFilter, "is_valid", return_value=False):
            with patch.object(Model, "get_all", return_value=on_get_all__data_to_return):

                # act

                test_context = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=12, settings=self.fake_settings, auth_user=6079)
                test_context.view()
                            
                # assert functions was called
                
                Model.get_all.assert_called_with(self.mock_db, 12, test_context.search_criteria, 6079)

                self.assertEqual(0, len(test_context.model))


    def test_view__request_method__should_have__settings(self):
        
        # arrange
        
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
            "date_from":"",
            "date_to":"",
            "event_type":"",
            "category":"",
            "subcategory":"",
            "page":"2",
            "pagesize":"25",
            "page_direction":"-1"
        }

        on_get_all__data_to_return = []
        
        with patch.object(EventLogFilter, "is_valid", return_value=True):
            with patch.object(Model, "get_all", return_value=on_get_all__data_to_return):

                # act

                test_context = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=13, settings=self.fake_settings, auth_user=6079)
                test_context.view()
                            
                # assert settings (from fake settings)

                self.assertEqual(7, test_context.settings.MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS)
                self.assertEqual(30, test_context.settings.MAX_NUMBER_OF_DAYS_TO_KEEP_LOGS)
