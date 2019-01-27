# -*- coding: utf-8 -*-
from basemodel import BaseModel, try_int

class ReferenceModel (BaseModel):

    def __init__(self, id_, title, publisher, year_published, scheme_of_work_id, authors = "", uri = "", last_accessed = "", created = "", created_by_id = 0, created_by_name = "", published=1):
        self.id = int(id_)
        self.title = title
        self.publisher = publisher
        self.year_published = try_int(year_published)
        self.authors = authors
        self.uri = uri
        self.scheme_of_work_id = scheme_of_work_id
        self.last_accessed = last_accessed
        self.created = created
        self.created_by_id = try_int(created_by_id)
        self.created_by_name = created_by_name
        self.published = published


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("title", self.title, 1, 300)

        # validate authors
        self._validate_optional_string("authors", self.authors, 200)

        # validate publisher
        self._validate_required_string("publisher", self.publisher, 1, 70)

        # validate year_published
        self._validate_required_integer("year_published", self.year_published, 1100, 2100)

        # validate uri
        self._validate_optional_uri("uri", self.uri)


    def _clean_up(self):
        """ clean up properties by removing whitespace etc """

        # trim title
        if self.title is not None:
            self.title = self.title.lstrip(' ').rstrip(' ')

        # trim authors
        if self.authors is not None:
            self.authors = self.authors.lstrip(' ').rstrip(' ')

        # trim publisher
        if self.publisher is not None:
            self.publisher = self.publisher.lstrip(' ').rstrip(' ')

        # trim uri
        if self.uri is not None:
            self.uri = self.uri.lstrip(' ').rstrip(' ')
