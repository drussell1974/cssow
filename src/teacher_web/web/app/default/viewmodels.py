import io
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.basemodel import try_int
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_topic import TopicModel
from shared.models.cls_keyword import KeywordModel
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class DefaultIndexViewModel(BaseViewModel):
    
    def __init__(self, db, top, auth_user):
        super().__init__(auth_user)

        self.schemes_of_work = []
        self.institutes = []
        self.departments = []
        self.db = db
        self.auth_user = auth_user

        # get institutes
        self.institutes = InstituteModel.get_my(self.db, auth_user=auth_user)

        # TODO: #371 get departments for each institute and append to institute
        for institute in self.institutes:
            #auth_user.institute_id = institute.id
            #auth_user.institute = institute

            departments = DepartmentModel.get_my(self.db, institute=institute, department_id=0, auth_user=auth_user)
            institute.departments = departments

            for department in institute.departments:
                department.schemes_of_work = SchemeOfWorkModel.get_my(self.db, institute=institute, department=department, auth_user=auth_user)
                self.departments.append(department)
                #for scheme_of_work in department.schemes_of_work:
                #    self.schemes_of_work.append(scheme_of_work)


    def view(self, main_heading, sub_heading):
        
        data = {
            "departments": self.departments,
            "institutes": self.institutes,
        }
        
        return ViewModel("", main_heading, sub_heading, ctx=self.auth_user, data=data, alert_message=self.alert_message, error_message=self.error_message)


class KeywordSaveViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, model, auth_user):
        self.db = db
        self.model = model
        self.auth_user = auth_user

    def execute(self, auth_user, published=STATE.PUBLISH):

        if type(self.model) is KeywordModel:
            
            self.model.validate()
            
            if self.model.is_valid == True:
                data = KeywordModel.save(self.db, self.model, auth_user)
                self.model = data
            else:
                handle_log_error(self.db, "saving keyword", "keyword not valid (keyword id:{}, term:'{}', definition:'{}', scheme_of_work_id:{}) validation_errors:{}".format(self.model.id, self.model.term, self.model.definition, self.model.scheme_of_work_id, self.model.validation_errors))
        else:
            raise AttributeError("Cannot save KeywordModel of type {}".format(type(self.model)))
        
        return self.model

