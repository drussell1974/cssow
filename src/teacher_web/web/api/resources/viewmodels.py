import markdown
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.serializers.srl_resource import ResourceSerializer
from shared.models.cls_resource import ResourceModel
from django.conf import settings

class ResourceGetModelViewModel(BaseViewModel):

    def __init__(self, db, resource_id, lesson_id, scheme_of_work_id, auth_user):
        self.db = db
        # get model
        model = ResourceModel.get_model(db, resource_id, lesson_id, scheme_of_work_id, auth_user)
        
        if model is not None:
            #model.key_words = list(map(lambda x: x.toJSON(), model.key_words))
            #TODO: #254: check for markdown to override page_uri
            if ResourceModel.is_markdown(model):
                model.page_uri = "x" #TODO: #254 build uri from route

            srl = ResourceSerializer(model)
            self.model = srl.data


class ResourceGetMarkdownViewModel(BaseViewModel):

    def __init__(self, resource_id, lesson_id, scheme_of_work_id, md_document_name):
        
        #TODO: #254 use python-markdown api to get md_document_name from MEDIA_ROOT - see https://python-markdown.github.io/reference/#markdown
        html = ""
        try:
            document_path = "{root}/{sow}/{lesson}/{resource}/{document}".format(root=settings.MARKDOWN_STORAGE, sow=scheme_of_work_id, lesson=lesson_id, resource=resource_id, document=md_document_name) 
            with open( document_path, "r", encoding="utf-8") as input_file:
                text = input_file.read()
                html = markdown.markdown(text)
        except Exception as e:
            # if in debug mode show error, or ask visitor to try refreshing the page
            html = "Document could not be retrieved at this time. {}.".format(e if settings.DEBUG else "Try refreshing the page.")
            
        self.model = html