from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.models.core.context import Ctx
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.serializers.srl_lesson_schedule import LessonScheduleModelSerializer

class LessonScheduleClassCodeViewModel(BaseViewModel):

    def __init__(self, db, class_code, auth_ctx):
        self.db = db
        
        # get model
        model = LessonScheduleModel.get_model_by_class_code(self.db, class_code, auth_ctx)

        if model is None or model.is_from_db == False:
            self.on_not_found(model)
        else:
            srl = LessonScheduleModelSerializer(model)
            self.model = srl.data


class LessonScheduleViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, lesson_id, auth_ctx, fn_resolve_url):
        self.db = db
        
        # get list
        data = LessonScheduleModel.get_all(self.db, scheme_of_work_id=scheme_of_work_id, lesson_id=lesson_id, auth_user=auth_ctx, fn_resolve_url=fn_resolve_url)
        
        srl_list = list(map(lambda m: LessonScheduleModelSerializer(m).data, data))
        self.model = srl_list