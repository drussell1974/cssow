from tests.model_test._unittest import TestCase
from learningobjective_testcase import LearningObjective_TestCase


class test_LearningObjectiveModel_validate__description(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.description = "A"

        # test
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.description = " x "

        # test
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.description, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")

    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.description = ""

        # test
        test.validate()

        # assert
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.description = None

        # test
        test.validate()

        # assert
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse elementum malesuada sagittis. Morbi vel"\
                "felis et tortor laoreet blandit ut eget nibh. Etiam feugiat, justo non semper bibendum, est nisl cursus lectus, quis varius elit mi nec purus. "\
                "Nulla dapibus, est eu tincidunt scelerisque, felis velit viverra nunc, ut bibendum eros urna non dolor. Integer vitae dapibus risus. Suspendisse "\
                "nec magna eu mauris tristique viverra sed quis massa. Donec in lorem tristique, accumsan mi sed, semper est. Aliquam enim dui, semper at scelerisque ac,"\
                "pretium eu felis. Vivamus in lectus vehicula, hendrerit diam non, efficitur ante. Maecenas suscipit eget nisl ut iaculis. Phasellus et viverra mauris. "\
                "Pellentesque sed metus hut dolor dignissim ultrices eget ac mi. Nullam id mi sit amet dui ultrices malesuada at vel ex. Phasellus fringilla est mauris, "\
                "efficitur blandit purus sodales ut. Donec gravida id velit ullamcorper facilisis. Sed porta leo quis nunc aliquet laoreet. Ut ac massa eu tellus sed." # length 1000 characters

        # test
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse elementum malesuada sagittis. Morbi vel"\
                "felis et tortor laoreet blandit ut eget nibh. Etiam feugiat, justo non semper bibendum, est nisl cursus lectus, quis varius elit mi nec purus. "\
                "Nulla dapibus, est eu tincidunt scelerisque, felis velit viverra nunc, ut bibendum eros urna non dolor. Integer vitae dapibus risus. Suspendisse "\
                "nec magna eu mauris tristique viverra sed quis massa. Donec in lorem tristique, accumsan mi sed, semper est. Aliquam enim dui, semper at scelerisque ac,"\
                "pretium eu felis. Vivamus in lectus vehicula, hendrerit diam non, efficitur ante. Maecenas suscipit eget nisl ut iaculis. Phasellus et viverra mauris. "\
                "Pellentesque sed metus hut dolor dignissim ultrices eget ac mi. Nullam id mi sit amet dui ultrices malesuada at vel ex. Phasellus fringilla est mauris, "\
                "efficitur blandit purus sodales ut. Donec gravida id velit ullamcorper facilisis. Sed porta leo quis nunc aliquet laoreet. Ut ac massa eu tellus sed.x" # length 1001 characters

        # test
        test.validate()

        # assert
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LearningObjectiveModel_validate__notes(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.notes = "A"

        # test
        test.validate()

        # assert
        self.assertFalse("notes" in test.validation_errors, "notes should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.notes = " "

        # test
        test.validate()

        # assert
        self.assertFalse("notes" in test.validation_errors, "notes should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.notes, "")
        self.assertTrue(test.is_valid, "is_valid should be True")

    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.notes = ""

        # test
        test.validate()

        # assert
        self.assertFalse("notes" in test.validation_errors, "notes should have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "should not be is_valid")


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.notes = None

        # test
        test.validate()

        # assert
        self.assertFalse("notes" in test.validation_errors, "notes should have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()


        test.notes = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis ligula ipsum. Donec lacus justo, accumsan luctus velit vel, " \
                     "ultricies consectetur nisl. Suspendisse potenti. Mauris lacus sem, congue nec aliquam vitae, imperdiet euismod mi. Morbi at mollis elit. " \
                     "Vivamus rutrum sollicitudin tincidunt. Nam eleifend ligula massa, vitae bibendum dolor finibus a. Vestibulum laoreet lorem ut ipsum imperdiet, " \
                     "quis pulvinar neque imperdiet. Pellentesque varius nulla sit amet sagittis volutpat. Proin eros orci, auctor vel neque nec, dapibus suscipit purus. " \
                     "Phasellus magna risus, congue sit amet dolor at, maximus tempor nisl. Sed sollicitudin viverra posuere. Sed a nulla quis dui bibendum maximus. Praesent in nisi quam."\
                     "Nullam vehicula eu libero sit amet efficitur. Suspendisse potenti. Suspendisse sed commodo tortor. Nam laoreet nulla eu enim semper, quis vulputate massa " \
                     "elementum. Quisque ut ante in mauris feugiat mattis tincidunt et elit. Vivamus iaculis commodo feugiat. Suspendisse in urna non magna auctor auctor. In ornare, " \
                     "nibh quis semper faucibus, quam elit posuere neque, ac consectetur odio augue vitae diam. Mauris accumsan odio a venenatis interdum. Sed pretium arcu dolor. Aliquam " \
                     "faucibus libero ut erat varius posuere. Vestibulum ultricies augue non tellus interdum mollis. Suspendisse dictum, ligula ac tempus pharetra, dolor erat ornare dui, " \
                     "eu blandit tortor enim sed urna. Sed rutrum, velit in finibus condimentum, tortor nunc dictum felis, id elementum odio leo quis felis."\
                     "Mauris sit amet augue orci. Curabitur aliquet finibus risus non luctus. Praesent placerat volutpat mi, id consequat justo semper at. Cras ac semper leo. Proin ac " \
                     "tortor nulla. Proin non sem in erat ullamcorper ornare. Phasellus ligula nunc, finibus sit amet gravida nec, varius eget erat. Cras non velit turpis. Phasellus vitae " \
                     "turpis est. Aliquam rhoncus purus non malesuada viverra. Etiam erat nibh, fringilla a diam nec, efficitur pellentesque odio. Quisque malesuada fermentum enim sit amet " \
                     "tempus. Vestibulum mattis dictum eleifend. Vivamus tincidunt, odio et porta ornare, nisi massa fringilla leo, vel blandit enim mi vel lectus. Aenean gravida ipsum sed " \
                     "libero blandit sollicitudin id in massa. Nulla malesuada vestibulum libero in tempus." \
                     "Cras cursus convallis dolor id dapibus. Sed sodales elit et nulla ultrices, vitae malesuada turpis ullamcorper. Nullam non turpis ac dolor suscipit gravida vitae vel urna. " \
                     "Aliquam ullamcorper dui id gravida iaculis. Fusce commodo ultricies ante amet." # length 2500 characters

        # test
        test.validate()

        # assert
        self.assertFalse("notes" in test.validation_errors, "notes should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.notes = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis ligula ipsum. Donec lacus justo, accumsan luctus velit vel, " \
                     "ultricies consectetur nisl. Suspendisse potenti. Mauris lacus sem, congue nec aliquam vitae, imperdiet euismod mi. Morbi at mollis elit. " \
                     "Vivamus rutrum sollicitudin tincidunt. Nam eleifend ligula massa, vitae bibendum dolor finibus a. Vestibulum laoreet lorem ut ipsum imperdiet, " \
                     "quis pulvinar neque imperdiet. Pellentesque varius nulla sit amet sagittis volutpat. Proin eros orci, auctor vel neque nec, dapibus suscipit purus. " \
                     "Phasellus magna risus, congue sit amet dolor at, maximus tempor nisl. Sed sollicitudin viverra posuere. Sed a nulla quis dui bibendum maximus. Praesent in nisi quam."\
                     "Nullam vehicula eu libero sit amet efficitur. Suspendisse potenti. Suspendisse sed commodo tortor. Nam laoreet nulla eu enim semper, quis vulputate " \
                     "massa elementum. Quisque ut ante in mauris feugiat mattis tincidunt et elit. Vivamus iaculis commodo feugiat. Suspendisse in urna non magna auctor auctor. In ornare, " \
                     "nibh quis semper faucibus, quam elit posuere neque, ac consectetur odio augue vitae diam. Mauris accumsan odio a venenatis interdum. Sed pretium arcu dolor. Aliquam " \
                     "faucibus libero ut erat varius posuere. Vestibulum ultricies augue non tellus interdum mollis. Suspendisse dictum, ligula ac tempus pharetra, dolor erat ornare dui, " \
                     "eu blandit tortor enim sed urna. Sed rutrum, velit in finibus condimentum, tortor nunc dictum felis, id elementum odio leo quis felis."\
                     "Mauris sit amet augue orci. Curabitur aliquet finibus risus non luctus. Praesent placerat volutpat mi, id consequat justo semper at. Cras ac semper leo. Proin ac " \
                     "tortor nulla. Proin non sem in erat ullamcorper ornare. Phasellus ligula nunc, finibus sit amet gravida nec, varius eget erat. Cras non velit turpis. Phasellus vitae " \
                     "turpis est. Aliquam rhoncus purus non malesuada viverra. Etiam erat nibh, fringilla a diam nec, efficitur pellentesque odio. Quisque malesuada fermentum enim sit amet " \
                     "tempus. Vestibulum mattis dictum eleifend. Vivamus tincidunt, odio et porta ornare, nisi massa fringilla leo, vel blandit enim mi vel lectus. Aenean gravida ipsum sed libero " \
                     "blandit sollicitudin id in massa. Nulla malesuada vestibulum libero in tempusx." \
                     "Cras cursus convallis dolor id dapibus. Sed sodales elit et nulla ultrices, vitae malesuada turpis ullamcorper. Nullam non turpis ac dolor suscipit gravida vitae vel urna. " \
                     "Aliquam ullamcorper dui id gravida iaculis. Fusce commodo ultricies ante amet." # length 2501 characters

        # test
        test.validate()

        # assert
        self.assertTrue("notes" in test.validation_errors, "notes should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LearningObjectiveModel_validate__content_id(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.content_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("content_id" in test.validation_errors, "content_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.content_id = 0

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "should not be is_valid")
        self.assertTrue("content_id" in test.validation_errors, "content_id should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.content_id = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("content_id" in test.validation_errors, "content_id should not have validation errors - %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.content_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("content_id" in test.validation_errors, "content_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.content_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("content_id" in test.validation_errors, "content_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LearningObjectiveModel_validate__solo_taxonomy_id(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.solo_taxonomy_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("solo_taxonomy_id" in test.validation_errors, "solo_taxonomy_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.solo_taxonomy_id = 0

        # test
        test.validate()

        # assert
        self.assertTrue("solo_taxonomy_id" in test.validation_errors, "solo_taxonomy_id should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.solo_taxonomy_id = None

        # test
        test.validate()

        # assert
        self.assertTrue("solo_taxonomy_id" in test.validation_errors, "solo_taxonomy_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.solo_taxonomy_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("solo_taxonomy_id" in test.validation_errors, "solo_taxonomy_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.solo_taxonomy_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("solo_taxonomy_id" in test.validation_errors, "solo_taxonomy_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LearningObjectiveModel_validate__lesson_id(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.lesson_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("lesson_id" in test.validation_errors, "lesson_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.lesson_id = 0

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "should not be is_valid")
        self.assertTrue("lesson_id" in test.validation_errors, "lesson_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.lesson_id = None

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("lesson_id" in test.validation_errors, "lesson_id should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.lesson_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("lesson_id" in test.validation_errors, "lesson_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.lesson_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("lesson_id" in test.validation_errors, "lesson_id should have validation error %s" % test.validation_errors)


class test_LearningObjectiveModel_validate__key_stage_id(LearningObjective_TestCase):

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
        self.assertTrue(test.is_valid, "should not be is_valid")
        self.assertFalse("key_stage_id" in test.validation_errors, "key_stage_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.key_stage_id = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_stage_id" in test.validation_errors, "key_stage_id should have validation error %s" % test.validation_errors)


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
        self.assertTrue(test.is_valid, "is_valid should be False")
        self.assertFalse("key_stage_id" in test.validation_errors, "key_stage_id should have validation error %s" % test.validation_errors)


class test_LearningObjectiveModel_validate__parent_id(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.parent_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("parent_id" in test.validation_errors, "parent_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.parent_id = 0 # values should not be negative

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "should not be is_valid")
        self.assertTrue("parent_id" in test.validation_errors, "parent_id should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.parent_id = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("parent_id" in test.validation_errors, "parent_id should not have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.exam_board_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("parent_id" in test.validation_errors, "parent_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.parent_id = 10000 # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("parent_id" in test.validation_errors, "parent_id should have validation error %s" % test.validation_errors)


class test_LearningObjectiveModel_validate__group_name(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.group_name = ""

        # test
        test.validate()

        # assert
        self.assertEqual(test.group_name, "")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("group_name" in test.validation_errors, "group_name should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.group_name = "  "

        # test
        test.validate()

        # assert
        self.assertEqual(test.group_name, "")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("group_name" in test.validation_errors, "group_name should have no validation errors - %s" % test.validation_errors)


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.group_name = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be False")
        self.assertFalse("group_name" in test.validation_errors, "group_name should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.group_name = "Loerm ipsum dol" # 15 characters

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")

        self.assertFalse("group_nam" in test.validation_errors, "group_name should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.group_name = "Lorem ipsum dolc" # 16 characters + 1

        # test
        test.validate()

        # assert
        self.assertTrue("group_name" in test.validation_errors, "group_name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
