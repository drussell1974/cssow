from enum import IntFlag

class SCHEMEOFWORK(IntFlag):
    """ Teacher permissions for schemes of work, keywords and curriculum content """
    NONE = 7
    VIEW = 2
    EDIT = 4
    ADD = 8
    PUBLISH = 16


class LESSON(IntFlag):
    """ Teacher permissions for lessons, keywords, learning objectives and resources """
    NONE = 7
    VIEW = 2
    EDIT = 4
    ADD = 8
    PUBLISH = 16
