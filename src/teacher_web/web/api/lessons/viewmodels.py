from shared.models.cls_lesson import LessonModel, LessonDataAccess
from shared.serializers.srl_lesson import LessonModelSerializer

class LessonGetAllViewModel:
    model = []
    
    def __init__(self, db, scheme_of_work_id, auth_user):

        self.db = db
        # get model
        data = LessonDataAccess.get_all(self.db, scheme_of_work_id, auth_user)
        
        srl_list = list(map(lambda m: LessonModelSerializer(m).data, data))
        self.model = srl_list


class LessonGetModelViewModel:
    model = None

    def __init__(self, db, lesson_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        model = LessonDataAccess.get_model(self.db, lesson_id, auth_user, resource_type_id)

        if model is not None:
            #model.key_words = list(map(lambda x: x.toJSON(), model.key_words))

            srl = LessonModelSerializer(model)
            self.model = srl.data

