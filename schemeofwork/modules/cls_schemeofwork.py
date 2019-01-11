# -*- coding: utf-8 -*-
from basemodel import BaseModel
from datetime import datetime

class SchemeOfWorkModel(BaseModel):

    def __init__(self, id_, name="", description="", exam_board_id=0, exam_board_name="", key_stage_id=0, key_stage_name="", created="", created_by_id=0, created_by_name="", is_recent = False, published = 1):
        self.id = int(id_)
        self.name = name
        self.description = description
        self.exam_board_id = self._try_int(exam_board_id)
        self.exam_board_name = exam_board_name
        self.key_stage_id = self._try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.is_recent = is_recent
        self.created=created
        self.created_by_id=self._try_int(created_by_id)
        self.created_by_name=created_by_name
        self.published=published


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # Validate name
        self._validate_required_string("name", self.name, 1, 40)
        # Validate description
        self._validate_optional_string("description", self.description, 1500)
        # Validate exam board
        self._validate_optional_integer("exam_board_id", self.exam_board_id, 1, 9999)
        # Validate key stage
        self._validate_required_integer("key_stage_id", self.key_stage_id, 1, 9999)


    def get_ui_title(self):
        self._clean_up()
        return self.name


    def get_ui_sub_heading(self):
        self._clean_up()

        heading = ""

        if self.key_stage_name is not None:
            heading = "{}".format(self.key_stage_name)
        if self.exam_board_name is not None:
            heading = heading + " - {}".format(self.exam_board_name)

        heading = heading.rstrip("- ")
        heading = heading.lstrip(" -")

        return heading


    def _clean_up(self):
        """ clean up properties """
        if self.name is not None:
            self.name = self.name.lstrip(' ').rstrip(' ')

        if self.description is not None:
            self.description = self.description.lstrip(' ').rstrip(' ')

        if self.key_stage_name is not None:
            self.key_stage_name = self.key_stage_name.strip(' ').rstrip(' ')

        if self.exam_board_name is not None:
            self.exam_board_name = self.exam_board_name.strip(' ').rstrip(' ')
