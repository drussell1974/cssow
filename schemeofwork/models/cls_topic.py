# -*- coding: utf-8 -*-
from basemodel import BaseModel

class TopicModel(BaseModel):
    def __init__(self, id_, name, parent_id, parent_name):
        self.id = id_
        self.name = name
        self.parent_id = parent_id
        self.parent_name = parent_name
    id = 0
    name = ""
    parent_id = 0
    parent_name = ""


