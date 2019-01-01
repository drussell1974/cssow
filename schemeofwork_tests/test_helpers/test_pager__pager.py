from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from pager import Pager

class test_pager__pager_pages(TestCase):


    def setUp(self):
        pass #self.test = Pager(page_size = 10)


    def test_show_1_page_for_1_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10)

        # test
        pages = self.test.pager_pages(data = ["Chlorine (Cl)"])

        # assert

        self.assertEqual((1, 1), pages, "number of pages to display not as expected")


    def test_show_1_page_for_3_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10)

        # test
        pages = self.test.pager_pages(data = ["Cobalt (Co)","Chlorine (Cl)","Potassium (K)"])

        # assert

        self.assertEqual((1, 1), pages, "number of pages to display not as expected")

    def test_show_1_page_for_10_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10)

        # test
        pages = self.test.pager_pages(data = ["foo","bar","fie","fi","fo","fum","fie","fi","fo","fum"])

        # assert

        self.assertEqual((1, 1), pages, "number of pages to display not as expected")


    def test_show_2_pages_for_11_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10)

        # test
        pages = self.test.pager_pages(data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)","Copper (Cu)",])

        # assert

        self.assertEqual((1,2), pages, "number of pages to display not as expected")


    def test_show_2_pages_for_17_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10)

        # test
        pages = self.test.pager_pages(data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)"])

        # assert

        self.assertEqual((1,2), pages, "number of pages to display not as expected")


    def test_show_2_pages_for_20_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10)

        # test
        pages = self.test.pager_pages(data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)","Nickel (Ni)","Phospherus (P)","Magnesium (Mg)",])

        # assert

        self.assertEqual((1, 2), pages, "number of pages to display not as expected")


    def test_show_3_pages_for_21_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10)

        # test
        pages = self.test.pager_pages(data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)","Nickel (Ni)","Phospherus (P)","Magnesium (Mg)","Helium (He)"])

        # assert

        self.assertEqual((1,3), pages, "number of pages to display not as expected")
