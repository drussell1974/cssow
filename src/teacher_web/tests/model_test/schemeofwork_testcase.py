from unittest import TestCase
from shared.models.core.context import Ctx
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.publlished import STATE

class SchemeOfWork_TestCase(TestCase):
    """ Shared functions """
    def _construct_valid_object(self):#
        """ Create a valid Object """
        # set up
        test = SchemeOfWorkModel(99, name="test name",
                                     description="test description",
                                     exam_board_id=1,
                                     exam_board_name="test exam board",
                                     key_stage_id=2,
                                     key_stage_name="test key stage",
                                     #department_id=3,
                                     department_name="test department",
                                     #institute_id=4,
                                     school_name="test school",
                                     published=STATE.PUBLISH,
                                     auth_user = Ctx(4,3))
        test.key_words = []
        
        # test
        test.validate()

        # assert
        self.assertEqual(99, test.id)
        self.assertEqual("test name", test.name, "--- setUp --- name should be ''")
        self.assertEqual("test description", test.description, "--- setUp --- description should be ''")
        self.assertEqual(1, test.exam_board_id, "--- setUp --- exam_board_id should be 0")
        self.assertEqual("test exam board", test.exam_board_name, "--- setUp --- exam_board_name should be ''")
        self.assertEqual(2, test.key_stage_id, "--- setUp --- key_stage_id should be 0")
        self.assertEqual("test key stage", test.key_stage_name, "--- setUp --- key_stage_name should be ''")
        self.assertTrue(len(test.validation_errors) == 0, "There should be no validation errors ---- test.validation_errors = %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "--- setUp --- is_valid should be True")

        return test
