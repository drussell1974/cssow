from datetime import datetime
import json
import traceback
from rest_framework import serializers, status
from django.conf import settings
from django.http.response import Http404
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_department import DepartmentModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel
from app.default.viewmodels import DefaultIndexViewModel

class SchemeOfWorkScheduleIndexViewModel(DefaultIndexViewModel):

    def __init__(self, db, request, institute_id, department_id, scheme_of_work_id, auth_user):
        super().__init__(db, 0, auth_user)
        self.scheme_of_work_id = scheme_of_work_id
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, id=scheme_of_work_id, auth_user=auth_user)
        
        # if not found then raise error
        if self.scheme_of_work_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)

        self.schemeofwork_options = SchemeOfWorkModel.get_options(self.db, self.auth_user)  
        self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  

        # get default from settings
        self.show_next_days = request.session.get("lesson_schedule.show_next_days", settings.PAGER["schedule"]["pagesize"])

        if request.method == "POST":
            # get show_next_days from POST or use default set above
            self.show_next_days = try_int(request.POST.get("show_next_days", self.show_next_days))
            request.session["lesson_schedule.show_next_days"] = self.show_next_days

        #lesson_id, scheme_of_work_id, auth_user
        data = LessonScheduleModel.get_all(db, lesson_id=0, scheme_of_work_id=scheme_of_work_id, show_next_days=self.show_next_days, auth_user=auth_user)
        self.model = data


    def view(self, request, main_heading, sub_heading):
        super().view(request, self.scheme_of_work.name, sub_heading)
        
        data = {
            "schemeofwork": self.scheme_of_work,
            "scheme_of_work_id": self.scheme_of_work_id,
            "schemeofwork_options": self.schemeofwork_options,
            "lesson_options": self.lesson_options,
            "schedules": self.model,
            "show_next_days": self.show_next_days,
            "days_to_show__options": settings.PAGER["schedule"]["pagesize_options"],
        }

        return ViewModel(request, "", main_heading, sub_heading, ctx=self.auth_user, data=data, active_model=self.scheme_of_work)

