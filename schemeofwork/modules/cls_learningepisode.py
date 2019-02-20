# -*- coding: utf-8 -*-
from basemodel import BaseModel, try_int

class LearningEpisodeModel (BaseModel):


    def __init__(self, id_, title, orig_id = 0, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", topic_id = 0, topic_name = "", related_topic_ids = "", parent_topic_id = 0, parent_topic_name = "", key_stage_id = 0, key_stage_name = "", year_id = 0, year_name = "", key_words = "", summary = "", created = "", created_by_id = 0, created_by_name = "", published=1):
        self.id = int(id_)
        self.title = title
        self.order_of_delivery_id = int(order_of_delivery_id)
        self.scheme_of_work_id = int(scheme_of_work_id)
        self.scheme_of_work_name = scheme_of_work_name
        self.topic_id = int(topic_id)
        self.topic_name = topic_name
        self.parent_topic_id = None if parent_topic_id is None else int(parent_topic_id)
        self.parent_topic_name = parent_topic_name
        self.related_topic_ids = related_topic_ids
        self.key_stage_id = int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.year_id = int(year_id)
        self.year_name = year_name
        self.key_words = key_words.replace(', ', ',')
        self.other_key_words = []
        self.summary = summary
        self.pathway_objective_ids = []
        self.pathway_ks123_ids = []
        self.created=created
        self.created_by_id=try_int(created_by_id)
        self.created_by_name=created_by_name
        self.published=published
        self.orig_id = orig_id


    def copy(self):
        self.orig_id = self.id


    def is_copy(self):
        if self.orig_id > 0:
            return True
        else:
            return False


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # Validate summary
        self._validate_required_string("title", self.title, 1, 45)


        # Validate order_of_delivery_id
        if self.order_of_delivery_id is None or self.order_of_delivery_id < 1 or self.order_of_delivery_id > 9999:
            self.validation_errors["order_of_delivery_id"] = "{} is not a valid selection".format(self.order_of_delivery_id)
            self.is_valid = False

        # Validate scheme_of_work_id
        if self.scheme_of_work_id is None or self.scheme_of_work_id < 1 or self.scheme_of_work_id > 9999:
            self.validation_errors["scheme_of_work_id"] = "{} is not a valid selection for scheme of work".format(self.order_of_delivery_id)
            self.is_valid = False

        # Validate topic_id
        if self.topic_id is None or self.topic_id < 1 or self.topic_id > 9999:
            self.validation_errors["topic_id"] = "{} is not a valid selection for scheme of work".format(self.order_of_delivery_id)
            self.is_valid = False

        # Validate key_stage_id
        if self.key_stage_id is None or self.key_stage_id < 1 or self.key_stage_id > 9999:
            self.validation_errors["key_stage_id"] = "{} is not a valid selection".format(self.key_stage_id)
            self.is_valid = False

        # Validate year_id
        if self.year_id is None or self.year_id < 1 or self.year_id > 13:
            self.validation_errors["year_id"] = "{} is not a valid selection".format(self.key_stage_id)
            self.is_valid = False

        # Validate key_words
        self._validate_optional_list("key_words", self.key_words, sep=",", max_items=30)

        # Validate summary
        self._validate_optional_string("summary", self.summary, 80)

        return self.is_valid


    def _clean_up(self):
        """ clean up properties """

        if self.title is not None:
            self.title = self.title.lstrip(' ').rstrip(' ')

        if self.scheme_of_work_name is not None:
            self.scheme_of_work_name = self.scheme_of_work_name.lstrip(' ').rstrip(' ')

        if self.key_stage_name is not None:
            self.key_stage_name = self.key_stage_name.lstrip(' ').rstrip(' ')

        if self.topic_name is not None:
            self.topic_name = self.topic_name.lstrip(' ').rstrip(' ')

        if self.parent_topic_name is not None:
            self.parent_topic_name = self.parent_topic_name.lstrip(' ').rstrip(' ')

        if self.key_words is not None:
            self.key_words = self.key_words.lstrip(' ').rstrip(' ').replace(', ', ',')

        if self.summary is not None:
            self.summary = self.summary.lstrip(' ').rstrip(' ')

        if self.pathway_objective_ids is not None:
            """ remove duplicates """
            staging_list = []
            for ob in self.pathway_objective_ids:
                if ob not in staging_list:
                    staging_list.append(ob.lstrip(' ').rstrip(' '));
            self.pathway_objective_ids = staging_list



