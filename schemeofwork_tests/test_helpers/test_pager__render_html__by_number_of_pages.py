from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from pager import Pager

class test_pager__render_html__by_number_of_pages(TestCase):


    def setUp(self):
        pass #self.test = Pager(page_size = 10)


    def test_show_1_page_for_1_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 5, data = ["Chlorine (Cl)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(1, self.test.start_pager_at, "start_pager_at not as expected")
        self.assertEqual(2, self.test.end_pager_at, "end_pager_at not as expected")


    def test_show_1_page_for_3_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 5, data = ["Cobalt (Co)","Chlorine (Cl)","Potassium (K)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(1, self.test.start_pager_at, "start_pager_at not as expected")
        self.assertEqual(2, self.test.end_pager_at, "end_pager_at not as expected")

    def test_show_1_page_for_10_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 5, data = ["foo","bar","fie","fi","fo","fum","fie","fi","fo","fum"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(1, self.test.start_pager_at, "start_pager_at not as expected")
        self.assertEqual(6, self.test.end_pager_at, "end_pager_at not as expected")


    def test_show_2_pages_for_11_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 5, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)","Copper (Cu)",])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(1, self.test.start_pager_at, "start_pager_at not as expected")
        self.assertEqual(6, self.test.end_pager_at, "end_pager_at not as expected")


    def test_show_2_pages_for_17_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 5, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(1, self.test.start_pager_at, "start_pager_at not as expected")
        self.assertEqual(6, self.test.end_pager_at, "end_pager_at not as expected")


    def test_show_2_pages_for_20_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 5, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)","Nickel (Ni)","Phospherus (P)","Magnesium (Mg)",])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(1, self.test.start_pager_at, "start_pager_at not as expected")
        self.assertEqual(6, self.test.end_pager_at, "end_pager_at not as expected")


    def test_show_3_pages_for_21_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 10, pager_size = 5, data = [
            "Cobalt (Co)","Chlorine (Cl)","Potassium (K)","Tin (Sn)","Mercury (Pb)",
            "Iron (Fe)","Gold (Au)","Carbon (C)","Hydroen (H)","Oxygen (O)",
            "Arsenic (As)","Vanadium (V)","Indium (In)","Sodium (Na)","Beryllium (Be)",
            "Nitrogen (N)","Fluorine (F)","Nickel (Ni)","Phospherus (P)","Magnesium (Mg)","Helium (He)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(1, self.test.start_pager_at, "start_pager_at not as expected")
        self.assertEqual(6, self.test.end_pager_at, "end_pager_at not as expected")
