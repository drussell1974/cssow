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
    key_stage_id = None

    def __init__(this, id_, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", topic_id = 0, topic_name = "", parent_topic_id = 0, parent_topic_name = "", key_stage_id = 0, created = "", created_by_id = 0, created_by_name = ""):
        this.id = int(id_)
        this.order_of_delivery_id = int(order_of_delivery_id)
        this.scheme_of_work_id = int(scheme_of_work_id)
        this.scheme_of_work_name = scheme_of_work_name if scheme_of_work_id > 0 else ""
        this.topic_id = int(topic_id)
        this.topic_name = topic_name
        this.parent_topic_id = parent_topic_id
        this.parent_topic_name = parent_topic_name,
        this.key_stage_id = key_stage_id
        this.created = created
        this.created_by_id = created_by_id
        this.created_by_name = created_by_name

    def validate(this):
        this.is_valid = True
        return True




