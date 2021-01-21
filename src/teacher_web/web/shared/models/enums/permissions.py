from enum import IntFlag

class DEPARTMENT(IntFlag):
    """ Teacher permissions for for viewing or adding """
    NONE = 1
    STUDENT = 2
    TEACHER = 4
    HEAD = 8
    ADMIN = 64
    

class SCHEMEOFWORK(IntFlag):
    """ Teacher permissions for schemes of work, keywords and curriculum content """
    NONE = 1
    VIEWER = 2
    EDITOR = 4
    OWNER = 64


class LESSON(IntFlag):
    """ Teacher permissions for lessons, keywords, learning objectives and resources """
    NONE = 1
    VIEWER = 2
    EDITOR = 4
    OWNER = 64
