from enum import IntFlag

class DEPARTMENT(IntFlag):
    """ Teacher permissions for for viewing or adding """
    NONE = 1
    STUDENT = 2
    TEACHER = 4
    HEAD = 8


class SCHEMEOFWORK(IntFlag):
    """ Teacher permissions for schemes of work, keywords and curriculum content """
    NONE = 1
    VIEW = 2
    EDIT = 4
    DELETE = 16
    PUBLISH = 32
    OWNER = 128


class LESSON(IntFlag):
    """ Teacher permissions for lessons, keywords, learning objectives and resources """
    NONE = 1
    VIEW = 2
    EDIT = 4
    ADD = 8
    DELETE = 16
    PUBLISH = 32
    OWNER = 128
