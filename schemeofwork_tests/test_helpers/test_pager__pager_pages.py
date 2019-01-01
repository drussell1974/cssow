from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from pager import Pager

class test_pager__pager_pages(TestCase):


    def setUp(self):
        pass #self.test = Pager(page_size = 10, pager_size = 2)


    def test_show_page_1_of_1__for_1_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 2, pager_size = 2, data = ["Chlorine (Cl)"])

        # test
        result = self.test.pager_pages()

        # assert

        self.assertEqual((1, 2), result, "number of pages to display not as expected")


    def test_show_page_1_in_page_1_of_2_pages_for_11_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 2, pager_size = 2, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)","Copper (Cu)",])

        # test
        result = self.test.pager_pages()

        # assert

        self.assertEqual((1,3), result, "number of pages to display not as expected")


    def test_show_page_2_in_page_1_of_2_pages_for_11_record(self):
        # set up
        self.test = Pager(page = 2, page_size = 2, pager_size = 2, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)","Copper (Cu)",])

        # test
        result = self.test.pager_pages()

        # assert

        self.assertEqual((1,3), result, "number of pages to display not as expected")


    def test_show_page_1_in_page_2_of_2_pages_for_11_record(self):
        # set up
        self.test = Pager(page = 3, page_size = 2, pager_size = 2, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)","Copper (Cu)",])

        # test
        result = self.test.pager_pages()

        # assert

        self.assertEqual((3,5), result, "number of pages to display not as expected")


"""
    def test_show_2_pages_for_17_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 2)

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
        self.test = Pager(page = 1, page_size = 10, pager_size = 2)

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
        self.test = Pager(page = 1, page_size = 10, pager_size = 2)

        # test
        pages = self.test.pager_pages(page = 1, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)","Nickel (Ni)","Phospherus (P)","Magnesium (Mg)","Helium (He)"])

        # assert

        self.assertEqual((1,3), pages, "number of pages to display not as expected")
"""
