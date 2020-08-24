from enum import IntEnum
class LOG_TYPE(IntEnum):
    Verbose = 8
    Information = 4
    Warning = 2
    Error = 1
    NONE = 7

    @staticmethod
    def parse(num):
        for typ in LOG_TYPE:
            if typ == int(num):
                return str(typ)
        