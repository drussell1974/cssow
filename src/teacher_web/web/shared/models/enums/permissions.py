from enum import IntFlag


def parse_enum(permission):
    enum_type = permission.split('.')[0]
    value = permission.split('.')[1]

    if enum_type == "DEPARTMENT":
        return DEPARTMENT[value]
    elif enum_type == "SCHEMEOFWORK":
        return SCHEMEOFWORK[value]
    elif enum_type == "LESSON":
        return LESSON[value]
    return None


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
