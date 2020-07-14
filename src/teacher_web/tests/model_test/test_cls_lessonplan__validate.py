from unittest import TestCase
from shared.models.cls_lessonplan import LessonPlanModel


class test_cls_lessonplan_validate__title(TestCase):

    test = None


    def setUp(self):
        valid_test_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                            " Etiam eleifend nunc eget sem ornare, sed placerat elit ultrices. " \
                            "Nullam sapien magna, lacinia sed placerat non, pretium at elit. Aenean " \
                            "sit amet tellus tristique, scelerisque sapien eget, egestas ipsum. Nulla " \
                            "at vehicula purus, in porta dolor. Proin facilisis arcu sed dolor iaculis " \
                            "hendrerit. Curabitur lorem lacus, iaculis et justo ac, euismod luctus tortor. " \
                            "Curabitur condimentum bibendum tellus et maximus. Morbi semper bibendum justo, " \
                            "nec consectetur arcu accumsan eget. Aliquam vel lobortis diam. Duis varius egestas " \
                            "dignissim. Praesent sagittis faucibus metus a fermentum. Nunc dignissim velit sapien, " \
                            "fermentum bibendum ipsum consectetur non. Nulla consectetur mollis massa auctor aliquam. " \
                            "Sed aliquet purus sit amet condimentum aliquet hasellus sagittis blandit diam, ut tempus " \
                            "ligula ornare in. Phasellus mi justo, mollis at cursus vel, tristique varius lectus. " \
                            "Quisque vel cursus ex, et viverra tortor. Sed vestibulum, augue metus."

        self.test = LessonPlanModel(id_=0, lesson_id = 0, title="Lorem ipsum dolor si", description=valid_test_description, order_of_delivery_id = 1, duration = 10, task_icon = "")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.title = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("title" in self.test.validation_errors, "title should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.title = " x "

        # test
        self.test.validate()

        # assert
        self.assertFalse("title" in self.test.validation_errors, "title should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.title, "x")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.title = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("title" in self.test.validation_errors, "title should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.title = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("title" in self.test.validation_errors, "title should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.title = "Lorem ipsum dolor siLorem ipsum dolor si" # length 40 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("title" in self.test.validation_errors, "title should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.title = "Lorem ipsum dolor sitLorem ipsum dolor si" # length 41 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("title" in self.test.validation_errors, "title should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_reference_validate__description(TestCase):

    test = None

    def setUp(self):
        valid_test_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                            " Etiam eleifend nunc eget sem ornare, sed placerat elit ultrices. " \
                            "Nullam sapien magna, lacinia sed placerat non, pretium at elit. Aenean " \
                            "sit amet tellus tristique, scelerisque sapien eget, egestas ipsum. Nulla " \
                            "at vehicula purus, in porta dolor. Proin facilisis arcu sed dolor iaculis " \
                            "hendrerit. Curabitur lorem lacus, iaculis et justo ac, euismod luctus tortor. " \
                            "Curabitur condimentum bibendum tellus et maximus. Morbi semper bibendum justo, " \
                            "nec consectetur arcu accumsan eget. Aliquam vel lobortis diam. Duis varius egestas " \
                            "dignissim. Praesent sagittis faucibus metus a fermentum. Nunc dignissim velit sapien, " \
                            "fermentum bibendum ipsum consectetur non. Nulla consectetur mollis massa auctor aliquam. " \
                            "Sed aliquet purus sit amet condimentum aliquet hasellus sagittis blandit diam, ut tempus " \
                            "ligula ornare in. Phasellus mi justo, mollis at cursus vel, tristique varius lectus. " \
                            "Quisque vel cursus ex, et viverra tortor. Sed vestibulum, augue metus."

        self.test = LessonPlanModel(id_=0, lesson_id = 0, title="Lorem ipsum dolor si", description=valid_test_description, order_of_delivery_id = 1, duration = 10, task_icon = "")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.description = "x"

        # test
        self.test.validate()

        # assert
        self.assertFalse("description" in self.test.validation_errors, "description should not have validation error %s" % self.test.validation_errors)
        self.assertEqual(self.test.description, "x")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.description = " x "

        # test
        self.test.validate()

        # assert
        self.assertFalse("description" in self.test.validation_errors, "description should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.description, "x")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.description = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("description" in self.test.validation_errors, "description should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.description = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("description" in self.test.validation_errors, "description should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                            " Etiam eleifend nunc eget sem ornare, sed placerat elit ultrices. " \
                            "Nullam sapien magna, lacinia sed placerat non, pretium at elit. Aenean " \
                            "sit amet tellus tristique, scelerisque sapien eget, egestas ipsum. Nulla " \
                            "at vehicula purus, in porta dolor. Proin facilisis arcu sed dolor iaculis " \
                            "hendrerit. Curabitur lorem lacus, iaculis et justo ac, euismod luctus tortor. " \
                            "Curabitur condimentum bibendum tellus et maximus. Morbi semper bibendum justo, " \
                            "nec consectetur arcu accumsan eget. Aliquam vel lobortis diam. Duis varius egestas " \
                            "dignissim. Praesent sagittis faucibus metus a fermentum. Nunc dignissim velit sapien, " \
                            "fermentum bibendum ipsum consectetur non. Nulla consectetur mollis massa auctor aliquam. " \
                            "Sed aliquet purus sit amet condimentum aliquet hasellus sagittis blandit diam, ut tempus " \
                            "ligula ornare in. Phasellus mi justo, mollis at cursus vel, tristique varius lectus. " \
                            "Quisque vel cursus ex, et viverra tortor. Sed vestibulum, augue metus." # length 1000 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("description" in self.test.validation_errors, "description should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                            " Etiam eleifend nunc eget sem ornare, sed placerat elit ultrices. " \
                            "Nullam sapien magna, lacinia sed placerat non, pretium at elit. Aenean " \
                            "sit amet tellus tristique, scelerisque sapien eget, egestas ipsum. Nulla " \
                            "at vehicula purus, in porta dolor. Proin facilisis arcu sed dolor iaculis " \
                            "hendrerit. Curabitur lorem lacus, iaculis et justo ac, euismod luctus tortor. " \
                            "Curabitur condimentum bibendum tellus et maximus. Morbi semper bibendum justo, " \
                            "nec consectetur arcu accumsan eget. Aliquam vel lobortis diam. Duis varius egestas " \
                            "dignissim. Praesent sagittis faucibus metus a fermentum. Nunc dignissim velit sapien, " \
                            "fermentum bibendum ipsum consectetur non. Nulla consectetur mollis massa auctor aliquam. " \
                            "Sed aliquet purus sit amet condimentum aliquet hasellus sagittis blandit diam, ut tempus " \
                            "ligula ornare in. Phasellus mi justo, mollis at cursus vel, tristique varius lectus. " \
                            "Quisque vel cursus ex, et viverra tortor. Sed vestibulum, Eaugue Ametus." # length 1001 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("description" in self.test.validation_errors, "description should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_reference_validate__task_icon(TestCase):

    test = None

    def setUp(self):
        valid_test_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                            " Etiam eleifend nunc eget sem ornare, sed placerat elit ultrices. " \
                            "Nullam sapien magna, lacinia sed placerat non, pretium at elit. Aenean " \
                            "sit amet tellus tristique, scelerisque sapien eget, egestas ipsum. Nulla " \
                            "at vehicula purus, in porta dolor. Proin facilisis arcu sed dolor iaculis " \
                            "hendrerit. Curabitur lorem lacus, iaculis et justo ac, euismod luctus tortor. " \
                            "Curabitur condimentum bibendum tellus et maximus. Morbi semper bibendum justo, " \
                            "nec consectetur arcu accumsan eget. Aliquam vel lobortis diam. Duis varius egestas " \
                            "dignissim. Praesent sagittis faucibus metus a fermentum. Nunc dignissim velit sapien, " \
                            "fermentum bibendum ipsum consectetur non. Nulla consectetur mollis massa auctor aliquam. " \
                            "Sed aliquet purus sit amet condimentum aliquet hasellus sagittis blandit diam, ut tempus " \
                            "ligula ornare in. Phasellus mi justo, mollis at cursus vel, tristique varius lectus. " \
                            "Quisque vel cursus ex, et viverra tortor. Sed vestibulum, augue metus."

        self.test = LessonPlanModel(id_=0, lesson_id = 0, title="Lorem ipsum dolor si", description=valid_test_description, order_of_delivery_id = 1, duration = 10, task_icon = "")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.task_icon = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should not have validation error %s" % self.test.validation_errors)
        self.assertEqual(self.test.task_icon, "")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.task_icon = " "

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.task_icon, "")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__valid_extreme(self):
        # set up

        self.test.task_icon = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                            " Etiam eleifend nunc eget sem ornare, sed placerat elit ultrices. " \
                            "Nullam sapien magna, lacinia sed placerat non, pretium at elit. Aenean " \
                            "sit amet tellus tristique, scelerisque sapien eget, egestas ipsum. Nulla " \
                            "at vehicula purus, in porta dolor. Proin facilisis arcu sed dolor iaculis " \
                            "hendrerit. Curabitur lorem lacus, iaculis et justo ac, euismod luctus tortor. " \
                            "nec consectetur arcu accumsan eget. Aliquam vel lobortis diam. Duis varius egestas" # length 500 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.task_icon = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                            " Etiam eleifend nunc eget sem ornare, sed placerat elit ultrices. " \
                            "Nullam sapien magna, lacinia sed placerat non, pretium at elit. Aenean " \
                            "sit amet tellus tristique, scelerisque sapien eget, egestas ipsum. Nulla " \
                            "at vehicula purus, in porta dolor. Proin facilisis arcu sed dolor iaculis " \
                            "hendrerit. Curabitur lorem lacus, iaculis et justo ac, euismod luctus tortor. " \
                            "nec consectetur arcu accumsan eget. Aliquam vel lobortis diam. Duis varius egestass" # length 501 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("task_icon" in self.test.validation_errors, "task_icon should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")
