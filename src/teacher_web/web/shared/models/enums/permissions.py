from enum import Enum

class TEACHER_SCHEMEOFWORK(Enum):
    """ Teacher permissions for schemes of work, keywords and curriculum content """
    CAN_VIEW = 1
    CAN_ADD = 2
    CAN_EDIT = 4


class TEACHER_LESSON(Enum):
    """ Teacher permissions for lessons, keywords, learning objectives and resources """
    CAN_VIEW = 1
    CAN_ADD = 2
    CAN_EDIT = 4
