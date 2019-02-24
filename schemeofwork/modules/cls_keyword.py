# -*- coding: utf-8 -*-
from basemodel import BaseModel
from db_helper import sql_safe

class KeywordModel(BaseModel):
    def __init__(self, id_, term, definition):
        self.id = id_
        self.term = term
        self.definition = definition


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("term", self.term, 1, 100)

        # validate page_uri
        self._validate_optional_string("definition", self.definition, 250)


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # trim term
        if self.term is not None:
            self.term = sql_safe(self.term)

        # trim definition
        if self.definition is not None:
            self.definition = sql_safe(self.definition)

