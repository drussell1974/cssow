from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from pager import Pager

class test_pager__data_to_display__start_end(TestCase):


    def setUp(self):
        pass


    # page size 1

    def test_page_1__page_size_1(self):

        # set up
        self.test = Pager(page_size = 1, page = 1, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(0, self.test.start)
        self.assertEqual(1, self.test.end)


    def test_page_2__page_size_1(self):

        # set up
        self.test = Pager(page_size = 1, page = 2, data = [])

        # test
        self.test.data_to_display()

        #assert
        self.assertEqual(1, self.test.start)
        self.assertEqual(2, self.test.end)


    def test_page_10__page_size_1(self):

        # set up
        self.test = Pager(page_size = 1, page = 10, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(9, self.test.start)
        self.assertEqual(10, self.test.end)


    # page size 2

    def test_page_1__page_size_2(self):

        # set up
        self.test = Pager(page_size = 2, page = 1, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(0, self.test.start)
        self.assertEqual(2, self.test.end)


    def test_page_2__page_size_2(self):

        # set up
        self.test = Pager(page_size = 2, page = 2, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(2, self.test.start)
        self.assertEqual(4, self.test.end)


    def test_page_9__page_size_2(self):

        # set up
        self.test = Pager(page_size = 2, page = 9, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(16, self.test.start)
        self.assertEqual(18, self.test.end)


    def test_page_10__page_size_2(self):
        # set up
        self.test = Pager(page_size = 2, page = 10, data = [])

        #test
        self.test.data_to_display()

        self.assertEqual(18, self.test.start)
        self.assertEqual(20, self.test.end)


    # page size 9

    def test_page_1__page_size_9(self):

        # set up
        self.test = Pager(page_size = 9, page = 1, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(0, self.test.start)
        self.assertEqual(9, self.test.end)


    def test_page_2__page_size_9(self):

        # set up
        self.test = Pager(page_size = 9, page = 2, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(9, self.test.start)
        self.assertEqual(18, self.test.end)


    def test_page_9__page_size_9(self):

        # set up
        self.test = Pager(page_size = 9, page = 9, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(72, self.test.start)
        self.assertEqual(81, self.test.end)


    def test_page_10__page_size_9(self):

        # set up
        self.test = Pager(page_size = 9, page = 10, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(81, self.test.start)
        self.assertEqual(90, self.test.end)


    # page size 10

    def test_page_1__page_size_10(self):

        # set up
        self.test = Pager(page_size = 10, page = 1, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(0, self.test.start)
        self.assertEqual(10, self.test.end)


    def test_page_2__page_size_10(self):

        # set up
        self.test = Pager(page_size = 10, page = 2, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(10, self.test.start)
        self.assertEqual(20, self.test.end)


    def test_page_9__page_size_10(self):

        # set up
        self.test = Pager(page_size = 10, page = 9, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(80, self.test.start)
        self.assertEqual(90, self.test.end)


    def test_page_10__page_size_10(self):

        # set up
        self.test = Pager(page_size = 10, page = 10, data = [])

        # test
        self.test.data_to_display()

        # assert
        self.assertEqual(90, self.test.start)
        self.assertEqual(100, self.test.end)
