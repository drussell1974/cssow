# -*- coding: utf-8 -*-
from basemodel import BaseModel

class KS123PathwayModel(BaseModel):
    def __init__(self, id_, objective):
        self.id = id_
        self.objective = objective
        self.is_checked = False


