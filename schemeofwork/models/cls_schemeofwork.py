# -*- coding: utf-8 -*-
from basemodel import BaseModel


class SchemeOfWorkModel(BaseModel):
    name = ""
    description = ""
    exam_board_id = 0
    exam_board_name = ""
    key_stage_id = 0
    key_stage_name = ""


    def __init__(self, id_, name = "", description = "", exam_board_id = 0, exam_board_name = "", key_stage_id = 0, key_stage_name = "", created = "", created_by = ""):
        self.id = int(id_)
        self.name = name
        self.description = description
        self.exam_board_id = exam_board_id
        self.exam_board_name = exam_board_name if exam_board_id > 0 else ""
        self.key_stage_id = key_stage_id
        self.key_stage_name = key_stage_name if key_stage_id > 0 else ""
        self.created = created
        self.created_by = created_by


    def validate(self):
        # set to True while validating
        self.is_valid = True
        self.validation_errors.clear()

        if self.name is None or len(self.name) == 0:
            self.validation_errors["name"]= ("name required")
            self.is_valid = False
        elif len(self.name) > 25:
            self.validation_errors["name"] = "name cannot exceed 25 characters {}".format(len(self.name))
            self.is_valid = False

        if len(self.description) > 1500:
            self.validation_errors["description"] = "description is {} characters (cannot exceed 1500)".format(len(self.description))
            self.is_valid = False



