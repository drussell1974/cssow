# -*- coding: utf-8 -*-
from basemodel import BaseModel

class LearningObjectiveModel (BaseModel):

    description = ""
    solo_taxonomy_id = 0
    solo_taxonomy_name = ""
    solo_taxonomy_level = ""
    topic_id = 0
    topic_name = ""
    parent_topic_id = 0
    parent_topic_name = ""
    content_id = 0
    content_description = ""
    exam_board_id = 0
    exam_board_name = ""
    learning_episode_id = 0
    learning_episode_name = ""
    key_stage_id = 0
    key_stage_name = ""
    parent_id = None

    def __init__(this, id_, description = "", solo_taxonomy_id = 0, solo_taxonomy_name = "", solo_taxonomy_level = "", topic_id = 0, topic_name = "", parent_topic_id = 0, parent_topic_name = "", content_id = 0, content_description = "", exam_board_id = 0, exam_board_name = "", key_stage_id = 0, key_stage_name = "", learning_episode_id = 0, learning_episode_name = "", parent_id = None, created = "", created_by = ""):
        this.id = int(id_)
        this.description = description
        this.solo_taxonomy_id = solo_taxonomy_id
        this.solo_taxonomy_name = solo_taxonomy_name
        this.solo_taxonomy_level = solo_taxonomy_level
        this.topic_id = topic_id
        this.topic_name = topic_name
        this.parent_topic_id = parent_topic_id
        this.parent_topic_name = parent_topic_name
        this.content_id = content_id
        this.content_name = content_description
        this.exam_board_id = exam_board_id
        this.exam_board_name = exam_board_name
        this.learning_episode_id = learning_episode_id
        this.learning_episode_name = learning_episode_name
        this.key_stage_id = key_stage_id
        this.key_stage_name = key_stage_name
        this.parent_id = None if parent_id is None else parent_id
        this.created = created
        this.created_by = created_by


    def validate(this):
        this.is_valid = True
        return True



