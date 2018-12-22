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
        self.is_valid = True
        return True



