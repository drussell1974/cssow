# -*- coding: utf-8 -*-
from basemodel import BaseModel

class ReferenceNoteModel (BaseModel):
    def __init__(self, id_, reference_id, learning_episode_id, page_note, page_uri=""):
        self.id = int(id_)
        self.page_note = page_note
        self.page_uri = page_uri
        self.learning_episode_id = learning_episode_id
        self.reference_id = reference_id


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("page_note", self.page_note, 1, 250)

        # validate page_uri
        self._validate_optional_uri("page_uri", self.page_uri)


    def _clean_up(self):
        """ clean up properties by removing whitespace etc """

        # trim title
        if self.page_note is not None:
            self.page_note = self.page_note.lstrip(' ').rstrip(' ')

        # trim authors
        if self.page_uri is not None:
            self.page_uri = self.page_uri.lstrip(' ').rstrip(' ')
