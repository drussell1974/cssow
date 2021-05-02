from datetime import datetime
import json
from rest_framework import serializers, status
from django.http.response import Http404
from django.conf import settings
from app.default.viewmodels import DefaultIndexViewModel
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_institute import InstituteModel as Model
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class InstituteIndexViewModel(DefaultIndexViewModel):

    def __init__(self, db, top, auth_user):
        super().__init__(db, top, auth_user)


    def view(self, request):
        view = super().view(request, settings.SITE_TITLE, settings.SITE_SUMMARY)
        return view


class InstituteAllViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user):
        self.model = []

        self.db = db
        self.auth_user = auth_user
        # get model
        data = Model.get_all(self.db, auth_user)

        # if not found then raise error
        if auth_user.institute_id > 0:
            if data is None:
                self.on_not_found(data)

        self.model = data


    def view(self, request):
        
        data = {
            "institutes": self.model
        }
        
        return ViewModel(request, "", settings.SITE_TITLE,  settings.SITE_SUMMARY, ctx=self.auth_user, data=data)


class InstituteEditViewModel(BaseViewModel):

    def __init__(self, db, request, auth_user):
        
        self.db = db
        self.auth_user = auth_user
        self.model = Model(id_=auth_user.institute_id, name="")

        if request.method == "GET" and self.model.id > 0:
            ## GET request from client ##
                
            model = Model.get_model(self.db, auth_user.institute_id, auth_user)
            if model is None or model.is_from_db == False:
                self.on_not_found(model, auth_user.institute_id) 
            
            self.model = model
        
        elif request.method == "POST":
            ## POST back from client ##

            # create instance of model from request.vars
            self.model = Model(
                id_=request.POST.get("id", 0),
                name=request.POST.get("name", ""),
                created=datetime.now(),
                created_by_id=self.auth_user)
        
            try:
                self.model.validate()
                
                if self.model.is_valid == True:
                    
                    published_state = STATE.parse(request.POST.get("published", "PUBLISH"))

                    data = Model.save(self.db, self.model, self.auth_user, published=published_state)
                    
                    self.on_post_complete(True)
                    self.model = data
                else:
                    self.alert_message = "validation errors %s" % self.model.validation_errors 
                    handle_log_warning(self.db, auth_user.institute_id, "saving institute", "institute is not valid (id:{}, name:{}, validation_errors (count:{}).".format(self.model.id, self.model.name, len(self.model.validation_errors)))
                    
            except Exception as ex:
                self.error_message = ex
                handle_log_exception(db, auth_user.institute_id, "An error occurred processing institute", ex)
                

    def view(self, request):
        
        # view data
        data = {
            "institute_id": self.model.id,
            "institute": self.model,
        }
        
        # build alert message to be displayed
        delete_message = "<p>'{display_name}' ({id}) will be deleted!<ul>"

        return ViewModel(request, "", self.model.name, "Institute", content_heading="Schedule", ctx=self.auth_user, data=data, active_model=self.model, error_message=self.error_message, alert_message=self.alert_message, delete_dialog_message=delete_message)


class InstituteScheduleViewModel(DefaultIndexViewModel):

    def __init__(self, db, request, institute_id, auth_user):
        super().__init__(db, 0, auth_user)
        self.institute_id = institute_id
        self.institute = Model.get_model(db, id=institute_id, auth_user=auth_user)
        
        # if not found then raise error
        if self.institute_id > 0:
            if self.institute is None or self.institute.is_from_db == False:
                self.on_not_found(self.institute, self.institute_id)

        # get default from settings
        self.show_next_days = request.session.get("lesson_schedule.show_next_days", settings.PAGER["schedule"]["pagesize"])

        if request.method == "POST":
            # get show_next_days from POST or use default set above
            self.show_next_days = try_int(request.POST.get("show_next_days", self.show_next_days))
            request.session["lesson_schedule.show_next_days"] = self.show_next_days

        #lesson_id, scheme_of_work_id, auth_user
        data = LessonScheduleModel.get_all(db, lesson_id=0, scheme_of_work_id=0, show_next_days=self.show_next_days, auth_user=auth_user)
        self.model = data


    def view(self, request):
        super().view(request, self.institute.name, "Institute")
        
        data = {
            "institute_id": self.institute.id,
            "institute": self.institute,
            "schedules": self.model,
            "show_next_days": self.show_next_days,
            "days_to_show__options": settings.PAGER["schedule"]["pagesize_options"],
        }

        return ViewModel(request, "", self.auth_user.institute.name, "Institute", content_heading="Schedule", ctx=self.auth_user, data=data, active_model=self.institute)


class InstituteDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        data = Model.delete_unpublished(db, auth_user)
        self.model = data


class InstitutePublishModelViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        data = Model.publish_by_id(db, auth_user, auth_user.institute_id)
        self.model = data
