import sys
sys.path.insert(0, '../../schemeofwork/modules/')

from schemeofwork_testcase import SchemeOfWork_TestCase


class test_SchemeOfWork_validate__name(SchemeOfWork_TestCase):

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
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.name = " x "

        # test
        test.validate()

        # assert
        self.assertEqual(test.name, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("name" in test.validation_errors, "name should have no validation errors - %s" % test.validation_errors)

    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.name = ""

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "should not be is_valid")
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.name = None

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.name = "Lorem ipsum dolor sit ame" # length 25 characters

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.name = "Lorem ipsum dolor sit amet" # length 25 characters + 1

        # test
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_SchemeOfWork_validate__description(SchemeOfWork_TestCase):

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
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("description" in test.validation_errors, "description should have no validation error %s" % test.validation_errors)


    def test_min__valid_extreme_is_NONE(self):

        test = self._construct_valid_object()

        test.description = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("description" in test.validation_errors, "description should have no validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.description = " x "

        # test
        test.validate()

        # assert
        self.assertEqual(test.description, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("description" in test.validation_errors, "description should have no validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nec sem vehicula, ultricies neque sit amet, luctus velit. Suspendisse vehicula ultricies felis, ut mollis sapien tempus sed. Cras congue euismod augue. Vivamus viverra, ligula eu laoreet hendrerit, turpis enim maximus massa, ac gravida mauris orci sed velit. Maecenas vulputate nulla vitae nisl laoreet, nec fringilla quam eleifend. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi eget leo eget metus hendrerit euismod at ut enim. Nunc dignissim magna est, sit amet dictum nisi euismod tincidunt. Etiam varius eleifend tortor, sed ultrices eros facilisis non. In risus mauris, vulputate aliquet vestibulum aliquam, interdum ut risus. Etiam in pharetra sem. Vestibulum vulputate porttitor augue, ut sollicitudin tellus egestas quis. Suspendisse vestibulum, libero eget tempor accumsan, leo ligula dignissim neque, eu feugiat sapien leo ac lacus."\
                "Proin nec turpis eu nibh porttitor rhoncus. Integer eget accumsan eros. Donec ligula erat, tempor in finibus a, tempus quis nisl. Phasellus tortor erat, posuere at odio eget, dictum tempor nunc. Suspendisse porta tortor id mauris vestibulum fermentum. Duis posuere scelerisque felis, eget commodo orci venenatis sed. Sed at mi nec libero tincidunt gravida non in ligula. Mauris lobortis elementum dolor vitae hendrerit. Fusce eu laoreet enim. Fusce non magna condimentum velit porta porta. Nunc volutpat est non gravida dignissim. Morbi quis turpis nec justo porta lobortis amet."

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("description" in test.validation_errors, "description should have no validation error %s" % test.validation_errors)


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


class test_SchemeOfWork_validate__exam_board_id(SchemeOfWork_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.exam_board_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.exam_board_id = 0 # values should not be negative

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "should not be is_valid")
        self.assertTrue("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.exam_board_id = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.exam_board_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.exam_board_id = 10000 # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("exam_board_id" in test.validation_errors, "exam_board_id should have validation error %s" % test.validation_errors)


class test_SchemeOfWork_clean_up__exam_board_name(SchemeOfWork_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.exam_board_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.exam_board_name, "x")


class test_SchemeOfWork_validate__key_stage_id(SchemeOfWork_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.key_stage_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_stage_id" in test.validation_errors, "key_stage_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.key_stage_id = 0

        # test
        test.validate()

        # assert
        self.assertTrue("key_stage_id" in test.validation_errors, "key_stage_id should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.key_stage_id = None

        # test
        test.validate()

        # assert
        self.assertTrue("key_stage_id" in test.validation_errors, "key_stage_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.key_stage_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_stage_id" in test.validation_errors, "key_stage_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.key_stage_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("key_stage_id" in test.validation_errors, "key_stage_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


