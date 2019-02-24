# -*- coding: utf-8 -*-
from basemodel import BaseModel, try_int
from db_helper import sql_safe


class SchemeOfWorkModel(BaseModel):

    def __init__(self, id_, name="", description="", exam_board_id=0, exam_board_name="", key_stage_id=0, key_stage_name="", created="", created_by_id=0, created_by_name="", is_recent = False, published = 1):
        self.id = int(id_)
        self.name = name
        self.description = description
        self.exam_board_id = try_int(exam_board_id)
        self.exam_board_name = exam_board_name
        self.key_stage_id = try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.is_recent = is_recent
        self.created=created
        self.created_by_id=try_int(created_by_id)
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


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        if self.name is not None:
            self.name = sql_safe(self.name)

        if self.description is not None:
            self.description = sql_safe(self.description)

        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.exam_board_name is not None:
            self.exam_board_name = sql_safe(self.exam_board_name)
