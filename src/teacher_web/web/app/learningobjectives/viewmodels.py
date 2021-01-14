import json
from django.http import Http404
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_lesson import LessonModel
from shared.models.cls_solotaxonomy import SoloTaxonomyModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.viewmodels.decorators.permissions import check_teacher_permission
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class LearningObjectiveIndexViewModel(BaseViewModel):
    
    @check_teacher_permission(LESSON.VIEW)
    def __init__(self, db, lesson_id, scheme_of_work_id, auth_user):
        self.model = []
        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = try_int(scheme_of_work_id, return_value=0)
        
        #253 check user id
        self.lesson = LessonModel.get_model(db, lesson_id, scheme_of_work_id, auth_user)
        
        if self.lesson is None:
            self.on_not_found(self.model, lesson_id, scheme_of_work_id)

        # get model
        data = Model.get_all(self.db, lesson_id, scheme_of_work_id, auth_user)
        self.model = data
        
        #253 check user id
        self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  



        # group objectives by solo taxonomy    

        solo_taxonomy_options = SoloTaxonomyModel.get_options(self.db, self.auth_user)

        self.learning_objectives_by_solo_group = {}

        for solo in solo_taxonomy_options:
            """ create dictionary item for each group """
            self.learning_objectives_by_solo_group[solo.id] = solo


        for learning_objective in self.model:
            """ add the learning objective to it's respective group """
            self.learning_objectives_by_solo_group[learning_objective["solo_taxonomy_id"]].learning_objectives.append(learning_objective)
        

    def view(self):
        
        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "lesson_id":int(self.lesson.id),
            "lesson": self.lesson,
            "learning_objectives": self.model,
            "learning_objectives_by_solo_group": self.learning_objectives_by_solo_group,
            "lesson_options": self.lesson_options,
        }

        return ViewModel("", self.lesson.title, self.lesson.summary, data=data)
        

class LearningObjectiveGetModelViewModel(BaseViewModel):

    #248 Add parameters
    @check_teacher_permission(LESSON.VIEW)
    def __init__(self, db, learning_objective_id, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        model = Model.get_model(self.db, learning_objective_id, lesson_id, scheme_of_work_id, auth_user)

        if learning_objective_id > 0:
            if model is None or model.is_from_db == False:
                self.on_not_found(model, learning_objective_id, lesson_id, scheme_of_work_id) 
        self.model = model


class LearningObjectiveEditViewModel(BaseViewModel):

    @check_teacher_permission(LESSON.EDIT)
    def __init__(self, db, scheme_of_work_id, model, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id
        self.model = model


    def execute(self, published):
        self.model.validate()

        if self.model.is_valid == True:
            data = Model.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            handle_log_warning(self.db, self.scheme_of_work_id, "saving learning objective", "learning objective is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model


class LearningObjectiveDeleteUnpublishedViewModel(BaseViewModel):

    @check_teacher_permission(LESSON.DELETE)
    def __init__(self, db, scheme_of_work_id, lesson_id, auth_user):
        data = Model.delete_unpublished(db, scheme_of_work_id, lesson_id, auth_user)
        self.model = data


class LearningObjectivePublishModelViewModel(BaseViewModel):

    @check_teacher_permission(LESSON.PUBLISH)
    def __init__(self, db, learning_objective_id, lesson_id, scheme_of_work_id, auth_user):
        data = Model.publish_item(db, learning_objective_id, scheme_of_work_id, auth_user)
        self.model = data
