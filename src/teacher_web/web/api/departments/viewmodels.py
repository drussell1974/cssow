from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.models.cls_department import DepartmentModel
from shared.serializers.srl_department import DepartmentModelSerializer


class DepartmentGetAllViewModel(BaseViewModel):
    
    def __init__(self, db, institute_id, auth_user):

        self.db = db
        # get model
        data = DepartmentModel.get_all(self.db, institute_id, auth_user)
        
        srl_list = list(map(lambda m: DepartmentModelSerializer(m).data, data))
        self.model = srl_list


class DepartmentGetModelViewModel(BaseViewModel):

    def __init__(self, db, department_id, auth_user):
        self.db = db
        # get model
        model = DepartmentModel.get_model(self.db, department_id, auth_user)

        if model is not None:

            srl = DepartmentModelSerializer(model)
            self.model = srl.data

