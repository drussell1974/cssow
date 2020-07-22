from rest_framework import serializers, status
from shared.models.core.log import handle_log_info
from shared.models.core.basemodel import try_int
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess
from shared.viewmodels.keyword_viewmodels import KeywordGetModelViewModel, KeywordGetModelByTermsViewModel, KeywordSaveViewModel

class LessonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = [
            "id", 
            "title", 
            "summary", 
            "order_of_delivery_id", 
            "scheme_of_work_id",
            "topic_id",
            "year_id",
            "key_stage_id",
            "published",
            "resources",
            "learning_objectives",
        ]


class LessonGetAllViewModel:
    list = []
    json = []
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        self.list = []

        self.db = db
        # get model
        data = LessonDataAccess.get_all(self.db, scheme_of_work_id, auth_user)
        self.list = data


class LessonGetModelViewModel:
    model = None
    json = {}



    def __init__(self, db, lesson_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        data = LessonDataAccess.get_model(self.db, lesson_id, auth_user, resource_type_id)
        self.model = data
        if self.model is not None:

            # get key_word objects
            self.model.key_words = LessonDataAccess.get_all_keywords(self.db, lesson_id)
            
            # get each terms for each item 
            key_word_map = map(lambda m: m.term, self.model.key_words)
            # assign as comma seperated list
            self.model.key_words_str = ",".join(list(key_word_map))

        # serialize model to json
        srl = LessonModelSerializer(data)
        self.json = srl.data


class LessonSaveViewModel:
    model = None

    def __init__(self, db, data, auth_user):
        
        self.db = db
        self.auth_user = auth_user

        if type(data) is Model:
            key_word_ids = data.key_words 

            # assign data directly to the model
            self.model = data

            # transform key_words
            self.model.key_words = []
    
            for keyword_id in key_word_ids.split(","):
                
                # get or insert
                keyword_id = try_int(keyword_id)
                if isinstance(keyword_id, int):
                    keyword_model = KeywordGetModelViewModel(db, keyword_id, auth_user)
                    self.model.key_words.append(keyword_model.model)
                elif isinstance(keyword_id, str) and len(keyword_id) > 0:
                    keyword_model = KeywordGetModelByTermsViewModel(db, keyword_id, allow_all=True, auth_user=auth_user)
                    if keyword_model.model is None:
                        # insert new key word
                        keyword_save = KeywordSaveViewModel(db)
                        keyword_save.execute(auth_user, 1)
                        self.model.key_words.append(keyword_save.model)
        #else:
        #    self.model = Model().from_json(data)


    def execute(self, published=1):
        data = LessonDataAccess.save(self.db, self.model, self.auth_user, published)
        self.model = data        
