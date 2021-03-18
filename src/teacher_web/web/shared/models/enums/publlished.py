from enum import IntEnum


class STATE(IntEnum):
    """ Published Status """
    PUBLISH = 1 # for visibility for all visitors (PUBLIC)
    PUBLISH_INTERNAL = 4 # for visibilitiy of logged in members 
    # PUBLISH_INSTITUTE = 8 # RESERVE for visibilitiy of members of the organisation
    # PUBLISH_PRIVATE = 16 # RESERVE for visibilitiy of members of the department
    DRAFT = 32 # SHOW ONLY CREATOR for visibilitiy of creator
    DELETE = 64


    @staticmethod
    def parse(state):
        if len(state.split('.')) > 0:
            state = state.split('.')[0]
        return STATE[state]

    