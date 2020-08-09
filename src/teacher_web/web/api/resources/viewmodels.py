from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.serializers.srl_resource import ResourceSerializer
from shared.models.cls_resource import ResourceModel


class ResourceGetModelViewModel(BaseViewModel):

    def __init__(self, db, resource_id, lesson_id, scheme_of_work_id, auth_user):
        self.db = db
        # get model
        model = ResourceModel.get_model(db, resource_id, lesson_id, scheme_of_work_id, auth_user)
        
        if model is not None:
            #model.key_words = list(map(lambda x: x.toJSON(), model.key_words))

            srl = ResourceSerializer(model)
            self.model = srl.data
