from unittest import TestCase
from shared.models.core.pager import Pager

class test_pager__data_to_display__return_data(TestCase):


    def setUp(self):
        self.mock_data = ["Cobalt (Co)", #1
                          "Chlorine (Cl)", #2
                          "Potassium (K)", #3
                          "Tin (Sn)", #4
                          "Mercury (Pb)", #5
                          "Iron (Fe)", #6
                          "Gold (Au)", #7
                          "Carbon (C)", #8
                          "Hydroen (H)", #9
                          "Oxygen (O)", #10
                          "Arsenic (As)", #11
                          "Vanadium (V)", #12
                          "Indium (In)", #13
                          "Sodium (Na)", #14
                          "Beryllium (Be)", #15
                          "Nitrogen (N)", #16
                          "Fluorine (F)", #17
                          "Nickel (Ni)", #18
                          "Phospherus (P)", #19
                          "Magnesium (Mg)", #20
                          "Helium (He)"] #21


    # page size 1

    def test_page_1__page_size_1(self):

        # set up
        self.test = Pager(page_size = 1, page = 1, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        # assert
        #  "Cobalt (Co)", # record 1

        self.assertEqual("Cobalt (Co)", result[0], "first item not as expected")


    def test_page_2__page_size_1(self):

        # set up
        self.test = Pager(page_size = 1, page = 2, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        #assert
        #  "Chlorine (Cl)", # record 2

        self.assertEqual("Chlorine (Cl)", result[0], "first item not as expected")


    def test_page_10__page_size_1(self):

        # set up
        self.test = Pager(page_size = 1, page = 10, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        #assert
        #  "Oxygen (O)", # record 10

        self.assertEqual("Oxygen (O)", result[0], "first item not as expected")


    # page size 2

    def test_page_1__page_size_2(self):

        # set up
        self.test = Pager(page_size = 2, page = 1, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        #assert
        #  "Cobalt (Co)", # record 1
        # "Chlorine (Cl)", # record 2

        self.assertEqual("Cobalt (Co)", result[0], "first item not as expected")
        self.assertEqual("Chlorine (Cl)", result[len(result)-1], "last item not as expected")


    def test_page_2__page_size_2(self):

        # set up
        self.test = Pager(page_size = 2, page = 2, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        #assert
        #  "Potassium (K)", # record 3
        #  "Tin (Sn)", # record 4

        self.assertEqual("Potassium (K)", result[0], "first item not as expected")
        self.assertEqual("Tin (Sn)", result[len(result)-1], "last item not as expected")


    def test_page_10__page_size_2(self):
        # set up
        self.test = Pager(page_size = 2, page = 10, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        #assert
        #  "Phospherus (P)", # record 19
        #  "Magnesium (Mg)", # record 20

        self.assertEqual("Phospherus (P)", result[0], "first item not as expected")
        self.assertEqual("Magnesium (Mg)", result[len(result)-1], "last item not as expected")


    # page size 10

    def test_page_1__page_size_10(self):

        # set up
        self.test = Pager(page_size = 10, page = 1, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        #assert
        """
        "Cobalt (Co)", #1
        "Oxygen (O)", #10
        """

        self.assertEqual("Cobalt (Co)", result[0], "first item not as expected")
        self.assertEqual("Oxygen (O)", result[len(result)-1], "last item not as expected")


    def test_page_2__page_size_10(self):

        # set up
        self.test = Pager(page_size = 10, page = 2, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        # assert
        """
        "Arsenic (As)", # record 11 
        "Magnesium (Mg)", # reccord 20
        """
        self.assertEqual("Arsenic (As)", result[0], "first item not as expected")
        self.assertEqual("Magnesium (Mg)", result[len(result)-1], "last item not as expected")


    def test_page_3__page_size_10(self):

        # set up
        self.test = Pager(page_size = 10, page = 3, data = self.mock_data)

        # test
        result = self.test.data_to_display()

        # assert
        #  "Helium (He)"] #21
        self.assertEqual("Helium (He)", result[0], "first item not as expected")
        self.assertEqual("Helium (He)", result[len(result)-1], "last item not as expected")


