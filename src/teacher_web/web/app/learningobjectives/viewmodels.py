import json
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_learningobjective import LearningObjectiveModel as Model
from shared.viewmodels.baseviewmodel import BaseViewModel


class LearningObjectiveIndexViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        self.model = []

        self.db = db
        # get model
        data = Model.get_all(self.db, scheme_of_work_id, auth_user)
        self.model = data


class LearningObjectiveGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, learning_objective_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        data = Model.get_model(self.db, learning_objective_id, auth_user)
        self.model = data


class LearningObjectiveSaveViewModel(BaseViewModel):

    def __init__(self, db, data, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.model = data


    def execute(self, published):
        self.model.validate()

        if self.model.is_valid == True:
            data = Model.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            #    raise Exception("Lesson is not valid! {}".format(self.model.validation_errors))
            handle_log_warning(self.db, "saving learning objective", "learning objective is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model


class LearningObjectiveDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, lesson_id, auth_user):
        data = Model.delete_unpublished(db, lesson_id, auth_user)
        self.model = data


class LearningObjectivePublishModelViewModel(BaseViewModel):

    def __init__(self, db, learning_objective_id, auth_user):
        data = Model.publish_item(db, learning_objective_id, auth_user)
        self.model = data
