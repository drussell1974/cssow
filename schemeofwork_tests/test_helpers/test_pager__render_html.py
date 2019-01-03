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


    def test_show_pages_1_for_5_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, pager_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",     "Tin (Sn)",        "Mercury (Pb)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>", result)


    def test_show_pages_1_to_5_for_25_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, pager_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(0, self.test.starting_record_in_group, "starting_record_in_group not as expected")
        self.assertEqual(25, self.test.remaining_number_of_records, "remaining_number_of_records not as expected")
        self.assertEqual(5, self.test.remaining_number_of_pages, "remaining_number_of_pages not as expected")
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>"\
                         "<li><a href='?page=2' class='btn'>2</a></li>"\
                         "<li><a href='?page=3' class='btn'>3</a></li>"\
                         "<li><a href='?page=4' class='btn'>4</a></li>"\
                         "<li><a href='?page=5' class='btn'>5</a></li>", result)


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
        self.assertEqual(0, self.test.starting_record_in_group, "starting_record_in_group not as expected")
        self.assertEqual(26, self.test.remaining_number_of_records, "remaining_number_of_records not as expected")
        self.assertEqual(6, self.test.remaining_number_of_pages, "remaining_number_of_pages not as expected")
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>"\
                         "<li><a href='?page=2' class='btn'>2</a></li>"\
                         "<li><a href='?page=3' class='btn'>3</a></li>"\
                         "<li><a href='?page=4' class='btn'>4</a></li>"\
                         "<li><a href='?page=5' class='btn'>5</a></li>"\
                         "<li><a href='?page=6' class='btn'>&rarr;</a></li>", result)


    def test_show_pages_6_with_previous_for_26_records(self):
        # set up
        self.test = Pager(page = 6, page_size = 5, pager_size = 5, data = [
            # group 1
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            # group 2
            "Neptunium (Np)",])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(25, self.test.starting_record_in_group, "starting_record_in_group not as expected")
        self.assertEqual(1, self.test.remaining_number_of_records, "remaining_number_of_records not as expected")
        self.assertEqual(1, self.test.remaining_number_of_pages, "remaining_number_of_pages not as expected")
        self.assertEqual("<li><a href='?page=5' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=6' class='btn btn-primary'>6</a></li>", result)


    def test_show_page_6_with_previous_and_next_for_60_records(self):
        # set up
        self.test = Pager(page = 6, page_size = 5, pager_size = 5, data = [
            # group 1
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            # group 2
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Tantalium (Ta)", "Antimony (Sb)",  "Niobium (Nb)",     "Neon (Ne)",        "Gallium (Ga)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            # group 3
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Tantalium (Ta)", "Antimony (Sb)",  "Niobium (Nb)",     "Neon (Ne)",        "Gallium (Ga)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(25, self.test.starting_record_in_group, "starting_record_in_group not as expected")
        self.assertEqual(35, self.test.remaining_number_of_records, "remaining_number_of_records not as expected")
        self.assertEqual(7, self.test.remaining_number_of_pages, "remaining_number_of_pages not as expected")
        self.assertEqual("<li><a href='?page=5' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=6' class='btn btn-primary'>6</a></li>"\
                         "<li><a href='?page=7' class='btn'>7</a></li>"\
                         "<li><a href='?page=8' class='btn'>8</a></li>"\
                         "<li><a href='?page=9' class='btn'>9</a></li>"\
                         "<li><a href='?page=10' class='btn'>10</a></li>"\
                         "<li><a href='?page=11' class='btn'>&rarr;</a></li>", result)


    def test_show_page_12_with_previous_for_55_records(self):
        # set up
        self.test = Pager(page = 12, page_size = 5, pager_size = 5, data = [
            # group 1
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            # group 2
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Tantalium (Ta)", "Antimony (Sb)",  "Niobium (Nb)",     "Gallium (Ga)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            # group 3
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Tantalium (Ta)", "Antimony (Sb)",  "Niobium (Nb)",     "Neon (Ne)",        "Gallium (Ga)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(50, self.test.starting_record_in_group, "starting_record_in_group not as expected")
        self.assertEqual(10, self.test.remaining_number_of_records, "remaining_number_of_records not as expected")
        self.assertEqual(2, self.test.remaining_number_of_pages, "remaining_number_of_pages not as expected")
        self.assertEqual("<li><a href='?page=10' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=11' class='btn'>11</a></li>"\
                         "<li><a href='?page=12' class='btn btn-primary'>12</a></li>", result)


