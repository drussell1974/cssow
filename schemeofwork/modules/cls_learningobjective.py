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

    def __init__(self, id_, description = "", solo_taxonomy_id = 0, solo_taxonomy_name = "", solo_taxonomy_level = "", topic_id = 0, topic_name = "", parent_topic_id = 0, parent_topic_name = "", content_id = 0, content_description = "", exam_board_id = 0, exam_board_name = "", key_stage_id = 0, key_stage_name = "", learning_episode_id = 0, learning_episode_name = "", parent_id = None, created = "", created_by_id = 0, created_by_name = ""):
        self.id = int(id_)
        self.description = description
        self.solo_taxonomy_id = solo_taxonomy_id
        self.solo_taxonomy_name = solo_taxonomy_name
        self.solo_taxonomy_level = solo_taxonomy_level
        self.topic_id = topic_id
        self.topic_name = topic_name
        self.parent_topic_id = parent_topic_id
        self.parent_topic_name = parent_topic_name
        self.content_id = content_id
        self.content_description = content_description
        self.exam_board_id = exam_board_id
        self.exam_board_name = exam_board_name
        self.learning_episode_id = learning_episode_id
        self.learning_episode_name = learning_episode_name
        self.key_stage_id = key_stage_id
        self.key_stage_name = key_stage_name
        self.parent_id = parent_id
        self.created = created
        self.created_by_id = created_by_id
        self.created_by_name = created_by_name


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate description
        self._validate_required_string("description", self.description, 1, 25)
        # validate exam_board_id
        self._validate_optional_integer("exam_board_id", self.exam_board_id, 1, 9999)
        # validate topic_id
        self._validate_required_integer("topic_id", self.topic_id, 1, 9999)
        # validate content_id
        self._validate_required_integer("content_id", self.content_id, 1, 9999)
        # validate solo_taxonomy_id
        self._validate_required_integer("solo_taxonomy_id", self.solo_taxonomy_id, 1, 9999)

    def _clean_up(self):
        """ clean up properties """

        if self.description is not None:
            self.description = self.description.lstrip(' ').rstrip(' ')


