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

        self.latest_schemes_of_work = []
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

        # get model
        self.latest_schemes_of_work = SchemeOfWorkModel.get_latest_schemes_of_work(self.db, top=5, auth_user=auth_user)



    def view(self, main_heading, sub_heading):
        
        data = {
            "latest_schemes_of_work":self.latest_schemes_of_work,
            "departments": self.departments,
            "institutes": self.institutes,
        }

        for dep in self.departments:
            if dep.number_of_topics == 0:
                self.alert_messages.append({"message":f"{dep.name}: You must create topics before you can create lessons and pathways. To add your first topic", "action": reverse('department_topic.new', args=[self.auth_user.institute.id, dep.id])})
            if dep.number_of_topics and dep.number_of_pathways == 0:
                self.alert_messages.append({"message":f"{dep.name}: Pathways allow mapped progress between different key stages. To add your first topic", "action": reverse('ks123pathways.new', args=[self.auth_user.institute_id, dep.id])})
            if dep.number_of_schemes_of_work == 0:
                self.info_messages.append({"message":f"{dep.name}: To create your first scheme of work", "action":reverse('schemesofwork.new', args=[self.auth_user.institute_id, dep.id]) })
        
        return ViewModel("", main_heading, sub_heading, ctx=self.auth_user, data=data, alert_message=self.alert_message, alert_messages=self.alert_messages, error_message=self.error_message, error_messages=self.error_messages, info_messages=self.info_messages)


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

