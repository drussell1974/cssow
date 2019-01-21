# -*- coding: utf-8 -*-
from basemodel import BaseModel, try_int

class LearningEpisodeModel (BaseModel):


    def __init__(self, id_, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", topic_id = 0, topic_name = "", related_topic_ids = "", parent_topic_id = 0, parent_topic_name = "", key_stage_id = 0, key_stage_name = "", key_words = "", summary = "", created = "", created_by_id = 0, created_by_name = "", published=1):
        self.id = int(id_)
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
        self.key_words = key_words
        self.other_key_words = []
        self.summary = summary
        self.pathway_objective_ids = []
        self.created=created
        self.created_by_id=try_int(created_by_id)
        self.created_by_name=created_by_name
        self.published=published


    def get_ui_title(self):
        """ display title with order of delivery and topic name """

        """ format full title with order of delivery """

        title_to_show = "Week {} - {}".format(self.order_of_delivery_id, self.topic_name)

        return title_to_show


    def get_ui_sub_heading(self):
        """ show scheme of work name """
        sub_heading_to_show = "for {scheme_of_work_name} - {summary}".format(scheme_of_work_name=self.scheme_of_work_name, summary=self.summary if self.summary is not None else '')

        # trim if needed
        sub_heading_to_show = sub_heading_to_show.rstrip(" -") # remove hypen

        return sub_heading_to_show


    def get_list_of_key_words(self):
        if self.key_words == "" or self.key_words is None:
            return []
        else:
            return self.key_words.split(',')

    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

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

        # Validate key_words
        self._validate_optional_list("key_words", self.key_words, sep=",", max_items=15)

        # Validate summary
        self._validate_optional_string("summary", self.summary, 80)

        return self.is_valid


    def _clean_up(self):
        """ clean up properties """

        if self.scheme_of_work_name is not None:
            self.scheme_of_work_name = self.scheme_of_work_name.lstrip(' ').rstrip(' ')

        if self.key_stage_name is not None:
            self.key_stage_name = self.key_stage_name.lstrip(' ').rstrip(' ')

        if self.topic_name is not None:
            self.topic_name = self.topic_name.lstrip(' ').rstrip(' ')

        if self.parent_topic_name is not None:
            self.parent_topic_name = self.parent_topic_name.lstrip(' ').rstrip(' ')

        if self.key_words is not None:
            self.key_words = self.key_words.lstrip(' ').rstrip(' ').lower()

        if self.summary is not None:
            self.summary = self.summary.lstrip(' ').rstrip(' ')

        if self.pathway_objective_ids is not None:
            """ remove duplicates """
            staging_list = []
            for ob in self.pathway_objective_ids:
                if ob not in staging_list:
                    staging_list.append(ob.lstrip(' ').rstrip(' '));
            self.pathway_objective_ids = staging_list



