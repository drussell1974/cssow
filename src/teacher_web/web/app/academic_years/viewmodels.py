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

    def __init__(self, db, institute_id, auth_user):
        super().__init__(db, top=0, auth_user=auth_user)
        self.institute_id = institute_id
        self.institute = InstituteModel.get_model(db, id=institute_id, auth_user=auth_user)
        
        # if not found then raise error
        if self.institute_id > 0:
            if self.institute is None or self.institute.is_from_db == False:
                self.on_not_found(self.institute, self.institute_id)

        self.academic_years = Model.get_all(db, institute_id, auth_ctx=auth_user)

        
    def view(self, request):
        """ return View """

        data = {
            "academic_years": self.academic_years 
        }

        return ViewModel(request, "", self.institute.name, "Institute", content_heading="Academic years", ctx=self.auth_user, data=data)


class AcademicYearEditViewModel(BaseViewModel):

    def __init__(self, db, request, year, auth_user):
        self.db = db
        self.request = request
        self.auth_user = auth_user
        
        if request.method == "GET":
            if year == 0: # must be new
                if len(self.auth_user.academic_years) > 0:
                    # must be new, so get the last academic year (which is the id) and increment by 1
                    self.year = self.auth_user.academic_years[len(self.auth_user.academic_years)-1].id + 1
                    self.model = Model.new(start_year=self.year, ctx=auth_user)
                else:
                    self.model = Model.default(ctx=self.auth_user)
                    self.model.is_from_db = False
            else:
                self.model = Model.get_model(self.db, 
                    institute_id=self.auth_user.institute_id, 
                    for_academic_year=year,
                    auth_ctx=self.auth_user)
                if self.model is None:
                    self.on_not_found(self.model, year)
                else:
                    self.model.is_from_db = True


    def execute(self):
        if self.request.method == "POST":
            if self.model is None:
                # must be new and there are no other academic years
                self.model = Model.default(ctx=self.auth_user)
            ## POST back from client ##
            # create instance of model from request
            self.model.id = try_int(self.request.POST.get("id", self.model.id))
            self.model.start_date = self.request.POST.get("start_date", 0)
            self.model.end_date = self.request.POST.get("end_date", 0) 
            self.model.is_from_db = True if self.request.POST.get("is_from_db").upper() == "TRUE" else False
            self.model.auth_ctx = self.auth_user
            
            try:
                self.model.validate()
                
                if self.model.is_valid == True:

                    data = Model.save(self.db, self.model, STATE.parse(self.request.POST.get("published", "PUBLISH")), self.auth_user)
                    
                    self.on_post_complete(True)
                    self.model = data
                else:
                    self.alert_message = "validation errors %s" % self.model.validation_errors 
                    handle_log_warning(self.db, self.model.id, "saving academic year", "academicy year is not valid (id:{}, name:{}, validation_errors (count:{}).".format(self.model.id, self.model.id, len(self.model.validation_errors)))
                    
            except Exception as ex:
                self.error_message = ex
                handle_log_exception(self.db, self.model.id, "An error occurred processing academic year", ex)
                #raise ex
                

    def view(self, request):

        # view data
        data = {
            "academic_year": self.model
        }
        
        # build alert message to be displayed
        
        return ViewModel(request, "", self.auth_user.institute.name, "Institute", content_heading="Academic year", ctx=self.auth_user, data=data, active_model=self.model, error_message=self.error_message, alert_message=self.alert_message)
