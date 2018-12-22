
from unittest import TestCase

import sys
sys.path.insert(0, '../')

from cls_schemeofwork import SchemeOfWorkModel

class TestCase_SchemeOfWork_Base(TestCase):
    """ Shared functions """
    def _construct_valid_object(self):#
        """ Create a valid Object """
        # set up
        test = SchemeOfWorkModel(99,
                                     name="test name",
                                     description="test description",
                                     exam_board_id=1,
                                     exam_board_name="test exam board",
                                     key_stage_id=2,
                                     key_stage_name="test key stage")

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
        self.assertTrue(test.is_valid, "--- setUp --- is_valid should be True")
        self.assertTrue(len(test.validation_errors) == 0, "There should be no validation errors ---- test.validation_errors = %s" % test.validation_errors)

        return test


class TestCase_SchemeOfWork_Name(TestCase_SchemeOfWork_Base):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):

        # set up
        test = self._construct_valid_object()

        test.name = "A"

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.name = "A"

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.name = "Lorem ipsum dolor sit ame" # length 25 characters

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):

        test = self._construct_valid_object()

        test.name = ""

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")

    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.name = None

        # test
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.name = "Lorem ipsum dolor sit amet" # length 25 characters + 1

        # test
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class TestCase_SchemeOfWork_Description(TestCase_SchemeOfWork_Base):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):

        test = self._construct_valid_object()

        test.description = ""

        # test
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should have no validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")

    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nec sem vehicula, ultricies neque sit amet, luctus velit. Suspendisse vehicula ultricies felis, ut mollis sapien tempus sed. Cras congue euismod augue. Vivamus viverra, ligula eu laoreet hendrerit, turpis enim maximus massa, ac gravida mauris orci sed velit. Maecenas vulputate nulla vitae nisl laoreet, nec fringilla quam eleifend. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi eget leo eget metus hendrerit euismod at ut enim. Nunc dignissim magna est, sit amet dictum nisi euismod tincidunt. Etiam varius eleifend tortor, sed ultrices eros facilisis non. In risus mauris, vulputate aliquet vestibulum aliquam, interdum ut risus. Etiam in pharetra sem. Vestibulum vulputate porttitor augue, ut sollicitudin tellus egestas quis. Suspendisse vestibulum, libero eget tempor accumsan, leo ligula dignissim neque, eu feugiat sapien leo ac lacus."\
                "Proin nec turpis eu nibh porttitor rhoncus. Integer eget accumsan eros. Donec ligula erat, tempor in finibus a, tempus quis nisl. Phasellus tortor erat, posuere at odio eget, dictum tempor nunc. Suspendisse porta tortor id mauris vestibulum fermentum. Duis posuere scelerisque felis, eget commodo orci venenatis sed. Sed at mi nec libero tincidunt gravida non in ligula. Mauris lobortis elementum dolor vitae hendrerit. Fusce eu laoreet enim. Fusce non magna condimentum velit porta porta. Nunc volutpat est non gravida dignissim. Morbi quis turpis nec justo porta lobortis amet."

        # test
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should have no validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")





    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.description = "XLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nec sem vehicula, ultricies neque sit amet, luctus velit. Suspendisse vehicula ultricies felis, ut mollis sapien tempus sed. Cras congue euismod augue. Vivamus viverra, ligula eu laoreet hendrerit, turpis enim maximus massa, ac gravida mauris orci sed velit. Maecenas vulputate nulla vitae nisl laoreet, nec fringilla quam eleifend. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi eget leo eget metus hendrerit euismod at ut enim. Nunc dignissim magna est, sit amet dictum nisi euismod tincidunt. Etiam varius eleifend tortor, sed ultrices eros facilisis non. In risus mauris, vulputate aliquet vestibulum aliquam, interdum ut risus. Etiam in pharetra sem. Vestibulum vulputate porttitor augue, ut sollicitudin tellus egestas quis. Suspendisse vestibulum, libero eget tempor accumsan, leo ligula dignissim neque, eu feugiat sapien leo ac lacus."\
                "Proin nec turpis eu nibh porttitor rhoncus. Integer eget accumsan eros. Donec ligula erat, tempor in finibus a, tempus quis nisl. Phasellus tortor erat, posuere at odio eget, dictum tempor nunc. Suspendisse porta tortor id mauris vestibulum fermentum. Duis posuere scelerisque felis, eget commodo orci venenatis sed. Sed at mi nec libero tincidunt gravida non in ligula. Mauris lobortis elementum dolor vitae hendrerit. Fusce eu laoreet enim. Fusce non magna condimentum velit porta porta. Nunc volutpat est non gravida dignissim. Morbi quis turpis nec justo porta lobortis amet."
                # length 1500 characters + 1

        # test
        test.validate()

        # assert
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")



