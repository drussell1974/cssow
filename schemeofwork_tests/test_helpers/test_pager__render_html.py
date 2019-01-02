from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from pager import Pager

class test_pager__render_html(TestCase):


    def setUp(self):
        pass #self.test = Pager(page_size = 10)


    def test_show_pages_1_for_1_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, pager_size = 5, data = ["Chlorine (Cl)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>", result)


    def test_show_pages_1_for_3_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, pager_size = 5, data = ["Cobalt (Co)","Chlorine (Cl)","Potassium (K)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>", result)


    def test_show_pages_1_to_5_for_25_record(self):
        # set up
        self.test = Pager(page = 5, page_size = 5, pager_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual("<li><a href='?page=1' class='btn'>1</a></li>"\
                         "<li><a href='?page=2' class='btn'>2</a></li>"\
                         "<li><a href='?page=3' class='btn'>3</a></li>"\
                         "<li><a href='?page=4' class='btn'>4</a></li>"\
                         "<li><a href='?page=5' class='btn btn-primary'>5</a></li>", result)


    def test_show_pages_1_to_5_with_next_for_26_records(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, pager_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Neptunium (Np)",])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>"\
                         "<li><a href='?page=2' class='btn'>2</a></li>"\
                         "<li><a href='?page=3' class='btn'>3</a></li>"\
                         "<li><a href='?page=4' class='btn'>4</a></li>"\
                         "<li><a href='?page=5' class='btn'>5</a></li>"\
                         "<li><a href='?page=6' class='btn'>&rarr;</a></li>", result)


    def test_show_pages_6_with_previous_for_26_records(self):
        # set up
        self.test = Pager(page = 6, page_size = 5, pager_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Neptunium (Np)",])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual("<li><a href='?page=5' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=6' class='btn btn-primary'>6</a></li>", result)


    def test_show_page_6_with_previous_for_30_records(self):
        # set up
        self.test = Pager(page = 6, page_size = 5, pager_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Tantalium (Ta)", "Antimony (Sb)",  "Niobium (Nb)",     "Neon (Ne)",        "Gallium (Ga)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual("<li><a href='?page=5' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=6' class='btn btn-primary'>6</a></li>", result)


