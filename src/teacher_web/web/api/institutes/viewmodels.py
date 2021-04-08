from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.models.cls_institute import InstituteModel
from shared.serializers.srl_institute import InstituteModelSerializer

class InstituteGetAllViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user):

        self.db = db
        # get model
        data = InstituteModel.get_all(self.db, auth_user)
        
        srl_list = list(map(lambda m: InstituteModelSerializer(m).data, data))
        self.model = srl_list


class InstituteGetModelViewModel(BaseViewModel):

    def __init__(self, db, institute_id, auth_user):
        self.db = db
        # get model
        model = InstituteModel.get_model(self.db, institute_id, auth_user)
        if model is None or model.is_from_db == False:
            self.on_not_found(model, institute_id)
        else:
            srl = InstituteModelSerializer(model)
            self.model = srl.data
