from datetime import datetime
import json
from rest_framework import serializers, status
from django.http.response import Http404
from app.default.viewmodels import DefaultIndexViewModel
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_institute import InstituteModel
from shared.models.cls_academic_year import AcademicYearModel as Model
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class AcademicYearIndexViewModel(DefaultIndexViewModel):

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


class AcademicYearEditViewModel(BaseViewModel):

    def __init__(self, db, request, year, auth_user):
        self.db = db
        self.model = Model.default(for_academic_year=year)
        self.auth_user = auth_user

        if request.method == "GET":
            ## GET request from client ##

            model = Model.get_model(self.db, year, auth_user)
            if model is None or model.is_from_db == False:
                self.on_not_found(model, auth_user.department.id) 
            
            self.model = model
        
        elif request.method == "POST":
            ## POST back from client ##

            # create instance of model from request
            self.model = Model(
                start_date=request.POST.get("start_date", ""),
                end_date=request.POST.get("end_date", 0),
                #created=datetime.now(),
                #created_by_id=self.auth_user.auth_user_id,
                is_from_db=False,
                auth_ctx=auth_user)
            
            try:
                self.model.validate()
                
                if self.model.is_valid == True:

                    data = Model.save(self.db, self.model, self.auth_user, STATE.parse(request.POST.get("published", "PUBLISH")))
                    
                    self.on_post_complete(True)
                    self.model = data
                else:
                    self.alert_message = "validation errors %s" % self.model.validation_errors 
                    handle_log_warning(self.db, year, "saving academic year", "academicy year is not valid (id:{}, name:{}, validation_errors (count:{}).".format(self.model.id, self.model.year, len(self.model.validation_errors)))
                    
            except Exception as ex:
                self.error_message = ex
                handle_log_exception(db, year, "An error occurred processing academic year", ex)
                raise ex
                

    def view(self, heading):
                
        # view data
        data = {
            "academic_year": self.model,
        }
        
        # build alert message to be displayed
        
        return ViewModel("", heading, self.model.name if len(self.model.name) != 0 else "Create academic year", ctx=self.auth_user, data=data, active_model=self.model, error_message=self.error_message, alert_message=self.alert_message)
