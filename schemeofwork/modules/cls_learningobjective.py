# -*- coding: utf-8 -*-
from basemodel import BaseModel, try_int
from db_helper import sql_safe

class LearningObjectiveModel (BaseModel):

    def __init__(self, id_, description = "", notes = "", scheme_of_work_name = "", solo_taxonomy_id = 0, solo_taxonomy_name = "", solo_taxonomy_level = "", topic_id = 0, topic_name = "", parent_topic_id = None, parent_topic_name = "", content_id = None, content_description = "", exam_board_id = None, exam_board_name = "", key_stage_id = 0, key_stage_name = "", learning_episode_id = 0, learning_episode_name = "", parent_id = None, key_words = "", group_name = "", created = "", created_by_id = 0, created_by_name = "", published=1):
        self.id = int(id_)
        self.description = description
        self.notes = notes
        self.scheme_of_work_name = scheme_of_work_name
        self.solo_taxonomy_id = int(solo_taxonomy_id)
        self.solo_taxonomy_name = solo_taxonomy_name
        self.solo_taxonomy_level = solo_taxonomy_level
        self.topic_id = int(topic_id)
        self.topic_name = topic_name
        self.parent_topic_id =  try_int(parent_topic_id)
        self.parent_topic_name = parent_topic_name
        self.content_id = try_int(content_id)
        self.content_description = content_description
        self.exam_board_id = try_int(exam_board_id)
        self.exam_board_name = exam_board_name
        self.learning_episode_id = int(learning_episode_id)
        self.learning_episode_name = learning_episode_name
        self.key_stage_id = int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.parent_id = try_int(parent_id)
        self.key_words = key_words.replace(', ', ',')
        self.group_name = group_name
        self.created=created
        self.created_by_id=try_int(created_by_id)
        self.created_by_name=created_by_name
        self.published=published


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate description
        self._validate_required_string("description", self.description, 1, 1000)

        # validate group_name
        self._validate_optional_string("group_name", self.group_name, 15)

        # validate notes
        self._validate_optional_string("notes", self.notes, 2500)

        # validate exam_board_id
        self._validate_optional_integer("exam_board_id", self.exam_board_id, 1, 9999)

        # validate topic_id
        self._validate_required_integer("topic_id", self.topic_id, 1, 9999)

        # validate parent_topic_id
        self._validate_optional_integer("parent_topic_id", self.parent_topic_id, 1, 9999)

        # validate content_id
        self._validate_optional_integer("content_id", self.content_id, 1, 9999)

        # validate solo_taxonomy_id
        self._validate_required_integer("solo_taxonomy_id", self.solo_taxonomy_id, 1, 9999)

        # validate learning_episode_id
        self._validate_required_integer("learning_episode_id", self.learning_episode_id, 1, 9999)

        # validate learning_episode_id
        self._validate_required_integer("key_stage_id", self.key_stage_id, 1, 9999)

        # validate parent_id
        self._validate_optional_integer("parent_id", self.parent_id, 1, 9999)

        # Validate key_words
        self._validate_optional_list("key_words", self.key_words, sep=",", max_items=15)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)

        # trim notes
        if self.notes is not None:
            self.notes = sql_safe(self.notes)

        # trim topic_name
        if self.topic_name is not None:
            self.topic_name = sql_safe(self.topic_name)

        # trim parent_topic_name
        if self.parent_topic_name is not None:
            self.parent_topic_name = sql_safe(self.parent_topic_name)

        # trim content_description
        if self.content_description is not None:
            self.content_description = sql_safe(self.content_description)

        # trim exam_board_name
        if self.exam_board_name is not None:
            self.exam_board_name = sql_safe(self.exam_board_name)

        # trim learning_episode_name
        if self.learning_episode_name is not None:
            self.learning_episode_name = sql_safe(self.learning_episode_name)

        # trim key_stage_name
        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.key_words is not None:
            self.key_words = sql_safe(self.key_words).replace(', ',',')

        # trim group_name
        if self.group_name is not None:
            self.group_name = sql_safe(self.group_name)


def sort_by_solo_taxonomy_level(unsorted_list):
    """
    Bubble sort by solo taxonomy level
    :param unsorted_list: the unsorted data
    :return: a sorted list
    """

    staging_list = unsorted_list

    while True:
        swapped = False
        for i in range(len(staging_list)-1):
            if staging_list[i].solo_taxonomy_level > staging_list[i+1].solo_taxonomy_level:
                """ put item in the correct position """
                temp1 = staging_list[i]
                temp2 = staging_list[i+1]

                staging_list[i] = temp2
                staging_list[i+1] = temp1
                swapped = True

        if swapped == False:
            """ no more sorting required so finish """
            break

    return staging_list
