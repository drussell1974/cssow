from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from api.resources.viewmodels import ResourceGetMarkdownViewModel as ViewModel
from shared.models.cls_resource import ResourceModel as Model


class test_viewmodel_ResourceGetMarkdownViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__with_exception(self):
        
        # arrange        
        self.mock_model = Mock()

        with patch.object(Model, "get_markdown_html", side_effect=KeyError):
            # act and assert
            markdown_viewmodel = ViewModel("/path/to/folder/", resource_id=9999, lesson_id=34, scheme_of_work_id=90, document_name="README.md", auth_user=99)
            self.assertEqual("Document could not be retrieved at this time. Try refreshing the page..", markdown_viewmodel.model)

    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = ""
        
        Model.get_markdown_html = Mock(return_value=data_to_return)

        # act  resource_id, lesson_id, scheme_of_work_id, md_document_name
        self.viewmodel = ViewModel("/path/to/folder/", resource_id=9370, lesson_id=74, scheme_of_work_id=90, document_name="TEST.md", auth_user=99)

        # assert functions was called
        Model.get_markdown_html.assert_called()
        self.assertEqual("", self.viewmodel.model)


    def test_init_called_fetch__return_item(self):
        
        # arrange
        
        data_to_return = "<h1>Lorem ipsum</h1><p>dolor sit amet, consectetur adipiscing elit. Nunc in quam nunc</p>"
        
        Model.get_markdown_html = Mock(return_value=data_to_return)

        self.mock_model = Mock()

        # act
        markdown_viewmodel = ViewModel("/path/to/folder/", resource_id=4533, lesson_id=18, scheme_of_work_id=90, document_name="TEST.md", auth_user=99)

        # assert functions was called
        Model.get_markdown_html.assert_called()
        self.assertEqual("<h1>Lorem ipsum</h1><p>dolor sit amet, consectetur adipiscing elit. Nunc in quam nunc</p>", markdown_viewmodel.model)
        #self.assertEqual("", self.viewmodel.model["markdown"])
