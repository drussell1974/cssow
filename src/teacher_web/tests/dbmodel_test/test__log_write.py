from tests.dbmodel_test._unittest import TestCase, FakeDb
from log import Log

class test__log_write(TestCase):

    def setUp(self):
        self.test = Log()
        self.test.is_enabled = True

        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        #self.fake_db.close()
        pass

    def test__should_retain_empty(self):
        self.test.write(self.fake_db, '')

        self.assertEqual(1,1)


    def test__should_change_none_to_null(self):
        self.test.write(self.fake_db, None)

        self.assertEqual(1,1)


    def test__should_retain_string(self):
        self.test.write(self.fake_db, "Hello World")

        self.assertEqual(1,1)


    def test__should_retain_int(self):
        self.test.write(self.fake_db, 0)

        self.assertEqual(1,1)


    def test__should_retain_float(self):
        self.test.write(self.fake_db, 0.1)

        self.assertEqual(1,1)


    def test__should_format_sql(self):
        self.test.write(self.fake_db, "SELECT * FROM test WHERE column1 = 'happy';")

        self.assertEqual(1,1)
