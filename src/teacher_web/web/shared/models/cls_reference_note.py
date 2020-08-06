# -*- coding: utf-8 -*-
from shared.models.core.basemodel import BaseModel
from shared.models.core.db_helper import sql_safe


class ReferenceNoteModel (BaseModel):
    def __init__(self, id_, reference_id, lesson_id, page_note, page_uri="", task_icon = ""):
        
        raise DeprecationWarning("No longer used.")

        self.id = int(id_)
        self.page_note = page_note
        self.page_uri = page_uri
        self.task_icon = task_icon
        self.lesson_id = lesson_id
        self.reference_id = reference_id


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate page_note
        self._validate_required_string("page_note", self.page_note, 1, 250)

        # validate page_uri
        self._validate_optional_uri("page_uri", self.page_uri)

        # validate task_icon
        self._validate_optional_string("task_icon", self.task_icon, 500)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        # trim title
        if self.page_note is not None:
            self.page_note = sql_safe(self.page_note)

        # trim task_icon
        if self.task_icon is not None:
            self.task_icon = sql_safe(self.task_icon)

        # trim page_uri
        if self.page_uri is not None:
            self.page_uri = sql_safe(self.page_uri)
