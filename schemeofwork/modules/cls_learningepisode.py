# -*- coding: utf-8 -*-
from basemodel import BaseModel

class LearningEpisodeModel (BaseModel):


    def __init__(self, id_, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", topic_id = 0, topic_name = "", parent_topic_id = 0, parent_topic_name = "", key_stage_id = 0, key_stage_name = "", created = "", created_by_id = 0, created_by_name = ""):
        self.id = int(id_)
        self.order_of_delivery_id = int(order_of_delivery_id)
        self.scheme_of_work_id = int(scheme_of_work_id)
        self.scheme_of_work_name = scheme_of_work_name
        self.topic_id = int(topic_id)
        self.topic_name = topic_name
        self.parent_topic_id = None if parent_topic_id is None else int(parent_topic_id)
        self.parent_topic_name = parent_topic_name
        self.key_stage_id = int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.created = created
        self.created_by_id = int(created_by_id)
        self.created_by_name = created_by_name


    def get_ui_title(self):
        """ display title with order of delivery and topic name """

        """ format topics """

        topics_to_show = ""
        if self.parent_topic_name is not None or self.parent_topic_name != "":
            topics_to_show = topics_to_show + "{}".format(self.parent_topic_name)

        if self.topic_name is not None and self.topic_name != "":
            topics_to_show = topics_to_show + " : {}".format(self.topic_name)

        # trim if needed
        topics_to_show = topics_to_show.replace("None", "")
        topics_to_show = topics_to_show.lstrip(" :") # remove spaces and colon

        """ format full title with order of delivery """

        title_to_show = "Week {} - {}".format(self.order_of_delivery_id, topics_to_show)

        # trim if needed
        title_to_show = title_to_show.rstrip(" -") # remove hypen and colon

        return title_to_show


    def get_ui_sub_heading(self):
        """ show scheme of work name """
        return "for {}".format(self.scheme_of_work_name)


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



