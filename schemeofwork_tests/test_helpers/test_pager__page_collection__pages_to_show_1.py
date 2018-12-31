from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from pager import Pager

class test_pager__page_collection(TestCase):


    def setUp(self):
        self.test = Pager(page_size = 10)


    def test_show_1_page_for_1_record(self):

        # test
        pages = self.test.page_collection(["Chlorine (Cl)"])

        # assert

        self.assertEqual(1, len(pages), "number of pages to display not as expected")
        ' page numbers to display '
        self.assertEqual(1, pages[0], "first page number to display not as expected")
        self.assertEqual(1, pages[len(pages)-1], "last page number to display not as expected")


    def test_show_1_page_for_3_record(self):

        # test
        pages = self.test.page_collection(["Cobalt (Co)","Chlorine (Cl)","Potassium (K)"])

        # assert

        self.assertEqual(1, len(pages), "number of pages to display not as expected")
        ' page numbers to display '
        self.assertEqual(1, pages[0], "first page number to display not as expected")
        self.assertEqual(1, pages[len(pages)-1], "last page number to display not as expected")


    def test_show_1_page_for_10_record(self):

        # test
        pages = self.test.page_collection(["foo","bar","fie","fi","fo","fum","fie","fi","fo","fum"])

        # assert

        self.assertEqual(1, len(pages), "number of pages to display not as expected")
        ' page numbers to display '
        self.assertEqual(1, pages[0], "first page number to display not as expected")
        self.assertEqual(1, pages[len(pages)-1], "last page number to display not as expected")


    def test_show_2_pages_for_11_record(self):

        # test
        pages = self.test.page_collection([
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)","Copper (Cu)",])

        # assert

        self.assertEqual(2, len(pages), "number of pages to display not as expected")
        ' page numbers to display '
        self.assertEqual(1, pages[0], "first page number to display not as expected")
        self.assertEqual(2, pages[len(pages)-1], "last page number to display not as expected")


    def test_show_2_pages_for_17_record(self):

        # test
        pages = self.test.page_collection([
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)"])

        # assert

        self.assertEqual(2, len(pages), "number of pages to display not as expected")
        ' page numbers to display '
        self.assertEqual(1, pages[0], "first page number to display not as expected")
        self.assertEqual(2, pages[len(pages)-1], "last page number to display not as expected")


    def test_show_2_pages_for_20_record(self):

        # test
        pages = self.test.page_collection([
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)","Nickel (Ni)","Phospherus (P)","Magnesium (Mg)",])

        # assert

        self.assertEqual(2, len(pages), "number of pages to display not as expected")
        ' page numbers to display '
        self.assertEqual(1, pages[0], "first page number to display not as expected")
        self.assertEqual(2, pages[len(pages)-1], "last page number to display not as expected")


    def test_show_3_pages_for_21_record(self):

        # test
        pages = self.test.page_collection([
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)","Nickel (Ni)","Phospherus (P)","Magnesium (Mg)","Helium (He)"])

        # assert

        self.assertEqual(3, len(pages), "number of pages to display not as expected")
        ' page numbers to display '
        self.assertEqual(1, pages[0], "first page number to display not as expected")
        self.assertEqual(3, pages[len(pages)-1], "last page number to display not as expected")
