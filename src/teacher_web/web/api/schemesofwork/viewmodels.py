from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.serializers.srl_schemeofwork import SchemeOfWorkModelSerializer

class SchemeOfWorkGetAllViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user, key_stage_id=0):

        self.db = db
        # get model
        data = SchemeOfWorkModel.get_all(self.db, auth_user, key_stage_id)
        
        srl_list = list(map(lambda m: SchemeOfWorkModelSerializer(m).data, data))
        self.model = srl_list


class SchemeOfWorkGetModelViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, auth_user):
        self.db = db
        # get model
        model = SchemeOfWorkModel.get_by_id(self.db, scheme_of_work_id, auth_user)

        if model is not None:

            srl = SchemeOfWorkModelSerializer(model)
            self.model = srl.data

