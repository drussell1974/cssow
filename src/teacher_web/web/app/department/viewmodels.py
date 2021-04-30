from datetime import datetime
import json
from rest_framework import serializers, status
from django.http.response import Http404
from django.urls import reverse
from app.default.viewmodels import DefaultIndexViewModel
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning, handle_log_info
from shared.models.core.log import LOG_TYPE
from shared.models.core.basemodel import try_int
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel as Model
from shared.models.cls_notification import NotifyModel
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class DepartmentIndexViewModel(DefaultIndexViewModel):

    def __init__(self, db, institute_id, top, auth_user):
        super().__init__(db, top, auth_user)
        self.institute_id = institute_id
        self.institute = InstituteModel.get_model(db, id=institute_id, auth_user=auth_user)
        
        # if not found then raise error
        if self.institute_id > 0:
            if self.institute is None or self.institute.is_from_db == False:
                self.on_not_found(self.institute, self.institute_id)


    def view(self, main_heading, sub_heading):
        view = super().view(self.institute.name, sub_heading)
        return view


class DepartmentAllViewModel(BaseViewModel):
    
    def __init__(self, db, institute_id, auth_user):
        self.model = []

        self.db = db
        self.institute_id = institute_id
        self.auth_user = auth_user
        
        self.institute = InstituteModel.get_model(db, id=institute_id, auth_user=auth_user)
        
        # if not found then raise error
        if self.institute_id > 0:
            if self.institute is None or self.institute.is_from_db == False:
                self.on_not_found(self.institute, self.institute_id)

        # get data
        data = Model.get_all(self.db, self.institute_id, auth_user)
        self.model = data


    def view(self):
        data = {
            "institute_id": self.institute_id,
            "institute": self.institute,
            "departments": self.model
        }
        #329 active_model = institue
        return ViewModel("", self.institute.name, "Departments", ctx=self.auth_user, data=data, active_model=self.institute)


class DepartmentEditViewModel(BaseViewModel):

    def __init__(self, db, request, auth_user):
        
        self.model = Model(id_=auth_user.department.id)
        self.auth_user = auth_user

        if request.method == "GET" and self.model.id > 0:
            ## GET request from client ##
                
            model = Model.get_model(self.db, auth_user)
            if model is None or model.is_from_db == False:
                self.on_not_found(model, auth_user.department.id) 
            
            self.model = model
        
        elif request.method == "POST":
            ## POST back from client ##

            # create instance of model from request.vars
            self.model = Model(
                id_=request.POST.get("id", 0),
                name=request.POST.get("name", ""),
                department_id=request.POST.get("department_id", 0),
                institute_id=request.POST.get("institute_id", 0),
                created=datetime.now(),
                created_by_id=self.auth_user)
        
            try:
                was_new = self.model.is_new()
                self.model.validate()
                
                if self.model.is_valid == True:

                    data = Model.save(db, self.model, self.auth_user, STATE.parse(request.POST.get("published", "PUBLISH")))
                    
                    self.on_post_complete(True)
                    self.model = data
                else:
                    self.alert_message = "validation errors %s" % self.model.validation_errors 
                    handle_log_warning(self.db, context.department_id, "saving department", "department is not valid (id:{}, name:{}, validation_errors (count:{}).".format(self.model.id, self.model.name, len(self.model.validation_errors)))
                    
            except Exception as ex:
                self.error_message = ex
                handle_log_exception(db, context.department_id, "An error occurred processing department", ex)
                

    def view(self):
        
        # get options
        self.institute_options = InstituteModel.get_options(self.db, self.auth_user)
        
        # view data
        data = {
            "department_id": self.model.id,
            "department": self.model,
        }
        
        # build alert message to be displayed
        delete_message = "<p>'{display_name}' ({id}) will be deleted!<ul>".format(display_name=self.model.name, id=self.model.id)
        if self.model.number_of_lessons > 0:
            delete_message = delete_message + "<li>{number_of_lessons} lesson(s)</li>".format(number_of_lessons=self.model.number_of_lessons)
        if self.model.number_of_learning_objectives > 0:
            delete_message = delete_message + "<li>{number_of_learning_objectives} learning objective(s)</li>".format(number_of_learning_objectives=self.model.number_of_learning_objectives)
        if self.model.number_of_resources > 0:
            delete_message = delete_message + "<li>{number_of_resources} resource(s)</li>".format(number_of_resources=self.model.number_of_resources)
        delete_message = delete_message + "</ul>"

        return ViewModel("", "Schemes of Work", self.model.name if len(self.model.name) != 0 else "Create new scheme of work", ctx=self.auth_user, data=data, active_model=self.model, error_message=self.error_message, alert_message=self.alert_message, delete_dialog_message=delete_message)

 
class DepartmentDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        data = Model.delete_unpublished(db, auth_user)
        self.model = data


class DepartmentPublishModelViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        data = Model.publish_by_id(db, auth_user, auth_user.department_id)
        self.model = data
