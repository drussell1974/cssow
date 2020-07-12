from tests.model_test._unittest import TestCase
from learningepisode_testcase import Lesson_TestCase
from web.shared.models.cls_lesson import LessonModel


class Test_Lesson_Constructor(TestCase):

    test = None

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_validate_for_default_instance_returns_false(self):

        # setup
        test = LessonModel(0, "Data Representation: Images")

        # test
        test.validate()

        # validate
        self.assertFalse(test.is_valid)


    def test_constructor_default(self):

        # test
        test = LessonModel(0, "Data Representation: Images")

        # assert
        self.assertEqual(0, test.id)
        self.assertEqual("Data Representation: Images", test.title)
        self.assertEqual(1, test.order_of_delivery_id, "order_of_delivery_id should be 0")
        self.assertEqual(0, test.scheme_of_work_id, "scheme_of_work_id should be 0")
        self.assertEqual("", test.scheme_of_work_name, "scheme_of_work_name should be ''")
        self.assertEqual(0, test.topic_id, "topic_id should be 0")
        self.assertEqual("", test.topic_name, "topic_name should be ''")
        self.assertEqual(0, test.parent_topic_id, "parent_topic_id should be 0")
        self.assertEqual("", test.parent_topic_name)
        self.assertEqual(0, test.key_stage_id, "key_stage_id should be 0")
        self.assertEqual("", test.key_stage_name, "key_stage_name should be ''")
        self.assertEqual(0, test.year_id, "year_id should be 0")
        self.assertEqual("", test.year_name, "year_name should be ''")
        #self.assertEqual("", test.key_words, "key_words should be ''")
        self.assertEqual("", test.summary, "summary should be ''")
        self.assertEqual(0, test.orig_id)

        self.assertEqual(False, test.is_valid, "is_valid should be False")
        self.assertTrue(len(test.validation_errors) == 0)


    def test_constructor_set_valid_values(self):

        # setup

        test = LessonModel(1,
                                 title="Data Representation: Images",
                                 order_of_delivery_id=2,
                                 scheme_of_work_id=3,
                                 topic_id=4,
                                 #key_words='unit,test',
                                 summary='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.',
                                 parent_topic_id=5,
                                 key_stage_id=6,
                                 year_id=9)

        # test
        test.validate()

        # assert
        self.assertEqual(1, test.id)
        self.assertEqual("Data Representation: Images", test.title)
        self.assertEqual(2, test.order_of_delivery_id)
        self.assertEqual(3, test.scheme_of_work_id)
        self.assertEqual(4, test.topic_id)
        #self.assertEqual('unit,test', test.key_words)
        self.assertEqual('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.', test.summary)
        self.assertEqual(5, test.parent_topic_id)
        self.assertEqual(6, test.key_stage_id)
        self.assertTrue(test.is_valid)


    def test_is_copy(self):
        # setup
        test = LessonModel(1, "Data Representation: Images")

        # test
        test.copy()
        result = test.is_copy()

        # validate
        self.assertTrue(result)
        self.assertEqual(1, test.orig_id)


    def test_is_not_copy(self):
        # setup
        test = LessonModel(1, "Data Representation: Images")

        # test
        result = test.is_copy()

        # validate
        self.assertFalse(result)
        self.assertEqual(0, test.orig_id)
