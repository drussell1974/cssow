from enum import IntEnum


class STATE(IntEnum):
    """ Published Status """
    PUBLISH = 1
    DRAFT = 32
    DELETE = 64


    @staticmethod
    def parse(state):
        return STATE[state]
