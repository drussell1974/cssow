from tests.model_test._unittest import TestCase, FakeDb
import cls_topic as db_topic


class test_db_topic__get_options__level_1(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__lvl_1__should_return_6_items(self):
        # test
        rows = db_topic.get_options(self.fake_db, lvl = 1)
        # assert
        self.assertEqual(6, len(rows))
        self.assertEqual("Algorithms", rows[0].name, "First item not as expected")
        self.assertEqual("Information technology", rows[len(rows)-1].name, "Last item not as expected")


    def test__lvl_2_topic_1__should_return_6_items(self):
        # test
        rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 1)
        # assert
        self.assertEqual(7, len(rows))
        self.assertEqual("Problem solving", rows[0].name, "First item not as expected")
        self.assertEqual("Boolean algebra", rows[len(rows)-1].name, "Last item not as expected")


    def test__lvl_2_topic_2__should_return_6_items(self):
        # test
        rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 2)
        # assert
        self.assertEqual(16, len(rows))
        self.assertEqual("Operators", rows[0].name, "First item not as expected")
        self.assertEqual("Run-time environment", rows[len(rows)-1].name, "Last item not as expected")


    def test__lvl_2_topic_3__should_return_6_items(self):
        # test
        rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 3)
        # assert
        self.assertEqual(8, len(rows))
        self.assertEqual("Binary", rows[0].name, "First item not as expected")
        self.assertEqual("Data compression", rows[len(rows)-1].name, "Last item not as expected")


    def test__lvl_2_topic_4__should_return_6_items(self):
        # test
        rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 4)
        # assert
        self.assertEqual(8, len(rows))
        self.assertEqual("CPU", rows[0].name, "First item not as expected")
        self.assertEqual("Optical storage", rows[len(rows)-1].name, "Last item not as expected")


    def test__lvl_2_topic_5__should_return_6_items(self):
        # test
        rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 5)
        # assert
        self.assertEqual(15, len(rows))
        self.assertEqual("Networks", rows[0].name, "First item not as expected")
        self.assertEqual("Hacking", rows[len(rows)-1].name, "Last item not as expected")


    def test__lvl_2_topic_6__should_return_6_items(self):
        # test
        rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 6)
        # assert
        self.assertEqual(12, len(rows))
        self.assertEqual("Internet services", rows[0].name, "First item not as expected")
        self.assertEqual("Environment", rows[len(rows)-1].name, "Last item not as expected")



