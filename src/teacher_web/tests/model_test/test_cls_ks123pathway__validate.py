from unittest import TestCase, skip
from shared.models.cls_ks123pathway import KS123PathwayModel


class test_cls_ks123pathway__validate__objective(TestCase):

    test = None

    def setUp(self):
        self.test = KS123PathwayModel(1, objective="", year_id=1, topic_id=1)


    def tearDown(self):
        pass


    def test_min__valid(self):
        # set up

        self.test.objective = "A"

        # test
        self.test.validate(skip_validation="")

        # assert
        self.assertFalse("objective" in self.test.validation_errors, "objective should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme_trim_whitespace(self):
        # set up

        self.test.objective = " "

        # test
        self.test.validate(skip_validation="")

        # assert
        self.assertTrue("objective" in self.test.validation_errors, "objective should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.objective, "")
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_min__valid_extreme(self):
        # set up

        self.test.objective = "a"

        # test
        self.test.validate(skip_validation="")

        # assert
        self.assertFalse("objective" in self.test.validation_errors, "objective should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.objective = None

        # test
        self.test.validate(skip_validation="")

        # assert
        self.assertTrue("objective" in self.test.validation_errors, "objective should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up
        
        self.test.objective = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eu maximus leo, convallis sollicitudin sapien. Vestibulum "\
            "turpis ipsum, sollicitudin ac feugiat in, fringilla id nibh. Donec accumsan magna erat, vel ornare ex lobortis nec. Praesent consectetur, "\
            "nibh ut efficitur ornare, odio risus mollis metus, quis viverra tellus risus in dolor. Nullam tortor turpis, imperdiet eget rutrum dictum, "\
            "rutrum eget urna. Sed ut ornare mi, at varius turpis. Aenean magna urna, varius ultrices orci sit biam."
            # length 500 characters

        # test
        self.test.validate(skip_validation="")

        # assert
        self.assertFalse("objective" in self.test.validation_errors, "objective should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.objective = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eu maximus leo, convallis sollicitudin sapien. Vestibulum "\
            "turpis ipsum, sollicitudin ac feugiat in, fringilla id nibh. Donec accumsan magna erat, vel ornare ex lobortis nec. Praesent consectetur, "\
            "nibh ut efficitur ornare, odio risus mollis metus, quis viverra tellus risus in dolor. Nullam tortor turpis, imperdiet eget rutrum dictum, "\
            "rutrum eget urna. Sed ut ornare mi, at varius turpis. Aenean magna urna, varius ultrices orci sit biamx."
            # length 501 characters

        # test
        self.test.validate(skip_validation="")

        # assert
        self.assertTrue("objective" in self.test.validation_errors, "objective should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_keyword__validate__year_id(TestCase):

    test = None

    def setUp(self):
        self.test = KS123PathwayModel(1, objective="lorem ipsum", year_id=1, topic_id=1)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.year_id = 1

        # test
        self.test.validate()

        # assert
        self.assertFalse("year_id" in self.test.validation_errors, "year_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.year_id = 0

        # test
        self.test.validate()

        # assert
        self.assertTrue("year_id" in self.test.validation_errors, "year_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_max__valid_extreme(self):
        # set up
        
        self.test.year_id = KS123PathwayModel.MAX_INT

        # test
        self.test.validate()

        # assert
        self.assertFalse("year_id" in self.test.validation_errors, "year_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.year_id = KS123PathwayModel.MAX_INT + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("year_id" in self.test.validation_errors, "year_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_keyword__validate__topic_id(TestCase):

    test = None

    def setUp(self):
        self.test = KS123PathwayModel(1, objective="lorem ipsum", year_id=1, topic_id=1)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.topic_id = 1

        # test
        self.test.validate()

        # assert
        self.assertFalse("topic_id" in self.test.validation_errors, "topic_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.topic_id = 0

        # test
        self.test.validate()

        # assert
        self.assertTrue("topic_id" in self.test.validation_errors, "topic_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_max__valid_extreme(self):
        # set up
        
        self.test.topic_id = KS123PathwayModel.MAX_INT

        # test
        self.test.validate()

        # assert
        self.assertFalse("topic_id" in self.test.validation_errors, "topic_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.topic_id = KS123PathwayModel.MAX_INT + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("topic_id" in self.test.validation_errors, "topic_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")
