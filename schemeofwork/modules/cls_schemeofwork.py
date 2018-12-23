# -*- coding: utf-8 -*-
from basemodel import BaseModel


class SchemeOfWorkModel(BaseModel):
    """
    id = 0
    name = ""
    description = ""
    exam_board_id = 0
    exam_board_name = ""
    key_stage_id = 0
    key_stage_name = ""
    """

    def __init__(self, id_, name="", description="", exam_board_id=0, exam_board_name="", key_stage_id=0, key_stage_name="", created="", created_by_id=0, created_by_name=""):
        self.id = int(id_)
        self.name = name
        self.description = description
        self.exam_board_id = self._try_int(exam_board_id)
        self.exam_board_name = exam_board_name
        self.key_stage_id = self._try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.created = created
        self.created_by_id = self._try_int(created_by_id)
        self.created_by_name = created_by_name


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # Validate name
        self._validate_required_string("name", self.name, 1, 25)

        # Validate description

        max_value = 1500

        if self.description is not None:
            if len(self.description) > max_value:
                self.validation_errors["description"] = "is {} characters (cannot exceed {} characters)".format(len(self.description), max_value)
                self.is_valid = False

        # Validate exam board
        if self.exam_board_id is not None:
            if self.exam_board_id < 1 or self.exam_board_id > 9999:
                self.validation_errors["exam_board_id"] = "{} is not a valid selection for exam board".format(self.exam_board_id)
                self.is_valid = False

        # Validate key stage
        if self.key_stage_id is None or self.key_stage_id < 1 or self.key_stage_id > 9999:
            self.validation_errors["key_stage_id"] = "{} is not a valid selection for key stage".format(self.key_stage_id)
            self.is_valid = False


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
