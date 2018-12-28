# -*- coding: utf-8 -*-
from basemodel import BaseModel

class TopicModel(BaseModel):
    def __init__(self, id_, name, created, created_by):
        self.id = id_
        self.name = name
        self.created = created
        self.created_by = created_by


