import sys
sys.path.append('../../schemeofwork/modules/')

from unittest import TestCase
from cls_schemeofwork import SchemeOfWorkModel


class Test_SchemeOfWork_Constructor(TestCase):

    test = None

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_validate_for_default_instance_returns_false(self):

        test = SchemeOfWorkModel(0)

        self.assertFalse(test.validate())
        self.assertFalse(test.is_valid)


    def test__constructor_default(self):
        # setup
        test = SchemeOfWorkModel(0)

        # assert
        self.assertEqual(0, test.id)
        self.assertEqual("", test.name, "name should be ''")
        self.assertEqual("", test.description, "description should be ''")
        self.assertEqual(0, test.exam_board_id, "exam_board_id should be 0")
        self.assertEqual("", test.exam_board_name, "exam_board_name should be ''")
        self.assertEqual(0, test.key_stage_id, "key_stage_id should be 0")
        self.assertEqual("", test.key_stage_name, "key_stage_name should be ''")
        self.assertTrue(test.published)
        self.assertFalse(test.is_recent)
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue(len(test.validation_errors) == 0, "Validation errors should be empty - %s" % test.validation_errors)


    def test_constructor_set_valid_values(self):
        # setup
        test = SchemeOfWorkModel(99,
                                 name="test name",
                                 description="test description",
                                 exam_board_id=1,
                                 exam_board_name="test exam board",
                                 key_stage_id=2,
                                 key_stage_name="test key stage",
                                 published=0)

        # test
        test.validate()

        # assert
        self.assertEqual(99, test.id)
        self.assertEqual("test name", test.name, "name should be ''")
        self.assertEqual("test description", test.description, "description should be ''")
        self.assertEqual(1, test.exam_board_id, "exam_board_id should be 0")
        self.assertEqual("test exam board", test.exam_board_name, "exam_board_name should be ''")
        self.assertEqual(2, test.key_stage_id, "key_stage_id should be 0")
        self.assertEqual("test key stage", test.key_stage_name, "key_stage_name should be ''")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse(test.is_recent)
        self.assertFalse(test.published)