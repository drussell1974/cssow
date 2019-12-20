from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import cls_learningepisode as db_learningepisode
import db_helper

class test_db_learningepisode__get_related_topics(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__learning_episode_id_0_for_topic_1_should_all_subtopics(self):
        # test
        rows = db_learningepisode.get_related_topic_ids(self.fake_db, 0, 1)

        # assert
        self.assertEqual(7, len(rows), "number of rows not as expected")
        ' first item '
        self.assertEqual(35, rows[0]["id"], "first item not as expected")
        self.assertEqual("Problem solving", rows[0]["name"])
        ' last item'
        self.assertEqual(41, rows[6]["id"], "last item not as expected")
        self.assertEqual("Boolean algebra", rows[6]["name"])


    def test__learning_episode_id_0_for_topic_2_should_all_subtopics(self):
        # test
        rows = db_learningepisode.get_related_topic_ids(self.fake_db, 0, 2)

        # assert
        self.assertEqual(16, len(rows), "number of rows not as expected")
        ' first item '
        self.assertEqual(42, rows[0]["id"], "first item not as expected")
        self.assertEqual("Operators", rows[0]["name"])
        ' last item'
        self.assertEqual(48, rows[6]["id"], "last item not as expected")
        self.assertEqual("Functions and procedures", rows[6]["name"])


    def test__learning_episode_id_0_for_topic_3_should_all_subtopics(self):
        # test
        rows = db_learningepisode.get_related_topic_ids(self.fake_db, 0, 3)

        # assert
        self.assertEqual(8, len(rows), "number of rows not as expected")
        ' first item '
        self.assertEqual(58, rows[0]["id"], "first item not as expected")
        self.assertEqual("Binary", rows[0]["name"])
        ' last item'
        self.assertEqual(64, rows[6]["id"], "last item not as expected")
        self.assertEqual("Sound", rows[6]["name"])


    def test__learning_episode_id_0_for_topic_4_should_all_subtopics(self):
        # test
        rows = db_learningepisode.get_related_topic_ids(self.fake_db, 0, 4)

        # assert
        self.assertEqual(8, len(rows), "number of rows not as expected")
        ' first item '
        self.assertEqual(7, rows[0]["id"], "first item not as expected")
        self.assertEqual("CPU", rows[0]["name"])
        ' last item'
        self.assertEqual(13, rows[6]["id"], "last item not as expected")
        self.assertEqual("Magnetic storage", rows[6]["name"])


    def test__learning_episode_id_0_for_topic_5_should_all_subtopics(self):
        # test
        rows = db_learningepisode.get_related_topic_ids(self.fake_db, 0, 5)

        # assert
        self.assertEqual(15, len(rows), "number of rows not as expected")
        ' first item '
        self.assertEqual(15, rows[0]["id"], "first item not as expected")
        self.assertEqual("Networks", rows[0]["name"])
        ' last item'
        self.assertEqual(21, rows[6]["id"], "last item not as expected")
        self.assertEqual("Network protocol", rows[6]["name"])


    def test__learning_episode_id_0_for_topic_6_should_all_subtopics(self):
        # test
        rows = db_learningepisode.get_related_topic_ids(self.fake_db, 0, 6)

        # assert
        self.assertEqual(12, len(rows), "number of rows not as expected")
        ' first item '
        self.assertEqual(30, rows[0]["id"], "first item not as expected")
        self.assertEqual("Internet services", rows[0]["name"])
        ' last item'
        self.assertEqual(67, rows[6]["id"], "last item not as expected")
        self.assertEqual("Legal", rows[6]["name"])


    def test__learning_episode_id_35__should_return__all_topics(self):

        rows = db_learningepisode.get_related_topic_ids(self.fake_db, 35, 2)

        # assert
        self.assertEqual(16, len(rows), "number of rows not as expected")

        ' first item - checked and disabled '
        self.assertEqual(42, rows[0]["id"], "first item not as expected")
        self.assertEqual("Operators", rows[0]["name"])
        self.assertTrue(rows[0]["checked"], "should be checked")
        self.assertTrue(rows[0]["disabled"], "should be disabled")

        ' second item - unchecked and enabled '
        self.assertEqual(43, rows[1]["id"], "last item not as expected")
        self.assertEqual("Variables and constants", rows[1]["name"])
        self.assertFalse(rows[1]["checked"], "should NOT be checked")
        self.assertFalse(rows[1]["disabled"], "should NOT be disabled")

        ' third item - checked and disabled '
        self.assertEqual(44, rows[2]["id"], "first item not as expected")
        self.assertEqual("Iteration and loops", rows[2]["name"])
        self.assertTrue(rows[2]["checked"], "should be checked")
        self.assertTrue(rows[2]["disabled"], "should be disabled")

        ' forth item - unchecked and enabled '
        self.assertEqual(45, rows[3]["id"], "last item not as expected")
        self.assertEqual("Arrays", rows[3]["name"])
        self.assertFalse(rows[3]["checked"], "should NOT be checked")
        self.assertFalse(rows[3]["disabled"], "should NOT be disabled")

        ' fifth item - checked and disabled '
        self.assertEqual(46, rows[4]["id"], "first item not as expected")
        self.assertEqual("Storing and accessing data: Files and SQL", rows[4]["name"])
        self.assertTrue(rows[4]["checked"], "should be checked")
        self.assertFalse(rows[4]["disabled"], "should be disabled")

        ' sixth item - unchecked and enabled '
        self.assertEqual(47, rows[5]["id"], "last item not as expected")
        self.assertEqual("String manipulation", rows[5]["name"])
        self.assertFalse(rows[5]["checked"], "should NOT be checked")
        self.assertFalse(rows[5]["disabled"], "should NOT be disabled")
