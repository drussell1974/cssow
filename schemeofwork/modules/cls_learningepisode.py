# -*- coding: utf-8 -*-
from basemodel import BaseModel

class LearningEpisodeModel (BaseModel):

    order_of_delivery_id = 0
    scheme_of_work_id = 0
    scheme_of_work_name = ""
    topic_id = 0
    topic_name = ""
    parent_topic_id = 0
    parent_topic_name = ""
    key_stage_id = 0
    key_stage_name = ""

    def __init__(self, id_, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", topic_id = 0, topic_name = "", parent_topic_id = 0, parent_topic_name = "", key_stage_id = 0, key_stage_name = "", created = "", created_by_id = 0, created_by_name = ""):
        self.id = int(id_)
        self.order_of_delivery_id = int(order_of_delivery_id)
        self.scheme_of_work_id = int(scheme_of_work_id)
        self.scheme_of_work_name = scheme_of_work_name
        self.topic_id = int(topic_id)
        self.topic_name = topic_name
        self.parent_topic_id = parent_topic_id
        #self.parent_topic_name = parent_topic_name,
        self.key_stage_id = key_stage_id
        self.key_stage_name = key_stage_name
        self.created = created
        self.created_by_id = created_by_id
        self.created_by_name = created_by_name

    def validate(self):
        self.is_valid = True
        self.validation_errors.clear()

        # Validate order_of_delivery_id
        if self.order_of_delivery_id is None or self.order_of_delivery_id < 1 or self.order_of_delivery_id > 9999:
            self.validation_errors["order_of_delivery_id"] = "{} is not a valid selection".format(self.order_of_delivery_id)
            self.is_valid = False

        # Validate scheme_of_work_id
        if self.scheme_of_work_id is None or self.scheme_of_work_id < 1 or self.scheme_of_work_id > 9999:
            self.validation_errors["scheme_of_work_id"] = "{} is not a valid selection for scheme of work".format(self.order_of_delivery_id)
            self.is_valid = False

        # Validate topic_id
        if self.topic_i is None or self.topic_id < 1 or self.topic_id > 9999:
            self.validation_errors["topic_id"] = "{} is not a valid selection for scheme of work".format(self.order_of_delivery_id)
            self.is_valid = False

        # Validate key_stage_id
        if self.key_stage_id is None or self.key_stage_id < 1 or self.key_stage_id > 9999:
            self.validation_errors["key_stage_id"] = "{} is not a valid selection".format(self.key_stage_id)
            self.is_valid = False

        return self.is_valid




