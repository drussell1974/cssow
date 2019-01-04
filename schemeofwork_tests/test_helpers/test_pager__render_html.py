from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from pager import Pager

class test_pager__render_html(TestCase):


    def setUp(self):
        pass #self.test = Pager(page_size = 10)


    def test_show_0_pages__for_ZERO_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, data = [])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(0, self.test.start_page, "start_page not as expected")
        self.assertEqual(0, self.test.end_page, "end_page not as expected")
        self.assertFalse(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(0, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(5, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("", result)
        #self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>", result)


    def test_1_page_group_for_1_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, data = ["Chlorine (Cl)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(0, self.test.start_page, "start_page not as expected")
        self.assertEqual(1, self.test.end_page, "end_page not as expected")
        self.assertFalse(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(0, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(5, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>", result)


    def test_1_page_group_for_5_records(self):
        # set up
        self.test = Pager(page = 1, page_size = 5,data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",     "Mercury (Pb)"])

        # test
        result = self.test.render_html()

        # assert
        #self.fail("implement offset for new page group")
        self.assertEqual(0, self.test.start_page, "start_page not as expected")
        self.assertEqual(1, self.test.end_page, "end_page not as expected")
        self.assertFalse(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(0, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(5, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>", result)


    def test_1_page_group_for_6_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",     "Tin (Sn)",        "Mercury (Pb)",
            "Niobium (Nb)"])

        # test
        result = self.test.render_html()

        # assert
        #self.fail("implement offset for new page group")
        self.assertEqual(0, self.test.start_page, "start_page not as expected")
        self.assertEqual(2, self.test.end_page, "end_page not as expected")
        self.assertFalse(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(0, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(5, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li><li><a href='?page=2' class='btn'>2</a></li>", result)


    def test_1_page_groups_for_35_record(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, data = [
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Carbon (C)",   "Fluorine (F)",     "Iron (Fe)",       "Neon (Ne)",        "Indium (In)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(0, self.test.start_page, "start_page not as expected")
        self.assertEqual(7, self.test.end_page, "end_page not as expected")
        self.assertFalse(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(0, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(5, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>"\
                         "<li><a href='?page=2' class='btn'>2</a></li>"\
                         "<li><a href='?page=3' class='btn'>3</a></li>"\
                         "<li><a href='?page=4' class='btn'>4</a></li>"\
                         "<li><a href='?page=5' class='btn'>5</a></li>"\
                         "<li><a href='?page=6' class='btn'>6</a></li>"\
                         "<li><a href='?page=7' class='btn'>7</a></li>", result)


    def test_2_page_groups_with_next_for_36_records(self):
        # set up
        self.test = Pager(page = 1, page_size = 5, data = [
            # group 1
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Carbon (C)",   "Fluorine (F)",     "Iron (Fe)",       "Neon (Ne)",        "Indium (In)",
            # group 2
            "Neptunium (Np)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(0, self.test.start_page, "start_page not as expected")
        self.assertEqual(7, self.test.end_page, "end_page not as expected")
        self.assertFalse(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertTrue(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(0, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(5, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=1' class='btn btn-primary'>1</a></li>"\
                         "<li><a href='?page=2' class='btn'>2</a></li>"\
                         "<li><a href='?page=3' class='btn'>3</a></li>"\
                         "<li><a href='?page=4' class='btn'>4</a></li>"\
                         "<li><a href='?page=5' class='btn'>5</a></li>"\
                         "<li><a href='?page=6' class='btn'>6</a></li>"\
                         "<li><a href='?page=7' class='btn'>7</a></li>"\
                         "<li><a href='?page=8' class='btn'>&rarr;</a></li>", result)


    def test_2_page_groups_with_previous_for_36_records(self):
        # set up
        self.test = Pager(page = 8, page_size = 5, data = [
            # group 1
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Carbon (C)",   "Fluorine (F)",     "Iron (Fe)",       "Neon (Ne)",        "Indium (In)",
            # group 2
            "Neptunium (Np)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(7, self.test.start_page, "start_page not as expected")
        self.assertEqual(8, self.test.end_page, "end_page not as expected")
        self.assertTrue(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(35, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(40, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=7' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=8' class='btn btn-primary'>8</a></li>", result)


    def test_3_page_groups_with_previous_and_next_for_66_records(self):
        # set up
        self.test = Pager(page = 8, page_size = 5, data = [
            # group 1
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Carbon (C)",   "Fluorine (F)",     "Iron (Fe)",       "Neon (Ne)",        "Indium (In)",
            # group 2
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            # group 3
            "Arsenic (As)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(7, self.test.start_page, "start_page not as expected")
        self.assertEqual(14, self.test.end_page, "end_page not as expected")
        self.assertTrue(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertTrue(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(35, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(40, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=7' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=8' class='btn btn-primary'>8</a></li>"\
                         "<li><a href='?page=9' class='btn'>9</a></li>"\
                         "<li><a href='?page=10' class='btn'>10</a></li>"\
                         "<li><a href='?page=11' class='btn'>11</a></li>"\
                         "<li><a href='?page=12' class='btn'>12</a></li>"\
                         "<li><a href='?page=13' class='btn'>13</a></li>"\
                         "<li><a href='?page=14' class='btn'>14</a></li>"\
                         "<li><a href='?page=15' class='btn'>&rarr;</a></li>", result)


    def test_3_page_groups_with_previous_for_71_records(self):
        # set up
        self.test = Pager(page = 15, page_size = 5, data = [
            # group 1
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Carbon (C)",   "Fluorine (F)",     "Iron (Fe)",       "Neon (Ne)",        "Indium (In)",
            # group 2
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            # group 3
            "Tantalium (Ta)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(14, self.test.start_page, "start_page not as expected")
        self.assertEqual(15, self.test.end_page, "end_page not as expected")
        self.assertTrue(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(70, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(75, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=14' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=15' class='btn btn-primary'>15</a></li>", result)


    def test_3_page_groups_with_previous_for_75_records(self):
        # set up
        self.test = Pager(page = 15, page_size = 5, data = [
            # group 1
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Carbon (C)",   "Fluorine (F)",     "Iron (Fe)",       "Neon (Ne)",        "Indium (In)",
            # group 2
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            # group 3
            "Tantalium (Ta)", "Antimony (Sb)",  "Niobium (Nb)",     "Gallium (Ga)",      "Oxygen (O)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(14, self.test.start_page, "start_page not as expected")
        self.assertEqual(15, self.test.end_page, "end_page not as expected")
        self.assertTrue(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(70, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(75, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=14' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=15' class='btn btn-primary'>15</a></li>", result)


    def test_3_page_groups_with_previous_for_76_records(self):
        # set up
        self.test = Pager(page = 15, page_size = 5, data = [
            # group 1
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Neon (Ne)",        "Hydroen (H)",
            "Carbon (C)",   "Fluorine (F)",     "Iron (Fe)",       "Neon (Ne)",        "Indium (In)",
            # group 2
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Nitrogen (N)", "Fluorine (F)",     "Nickel (Ni)",      "Phospherus (P)",   "Magnesium (Mg)",
            "Iron (Fe)",    "Gold (Au)",        "Carbon (C)",       "Hydroen (H)",      "Oxygen (O)",
            "Arsenic (As)", "Vanadium (V)",     "Indium (In)",      "Sodium (Na)",      "Beryllium (Be)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            "Helium (He)",  "Selenium (Se)",    "Niobium (Nb)",     "Francium (Fr)",    "Chromium (Cr)",
            "Cobalt (Co)",  "Chlorine (Cl)",    "Potassium (K)",    "Tin (Sn)",         "Mercury (Pb)",
            # group 3
            "Tantalium (Ta)", "Antimony (Sb)",  "Niobium (Nb)",     "Gallium (Ga)",      "Oxygen (O)",
            "Arsenic (As)"])

        # test
        result = self.test.render_html()

        # assert
        self.assertEqual(14, self.test.start_page, "start_page not as expected")
        self.assertEqual(16, self.test.end_page, "end_page not as expected")
        self.assertTrue(self.test.show_previous_pages, "show_previous_pages not as expected")
        self.assertFalse(self.test.show_more_pages, "show_more_pages not as expected")
        self.assertEqual(70, self.test.display_records_start, "display_records_start not as expected")
        self.assertEqual(75, self.test.display_records_end, "display_records_end not as expected")
        self.assertEqual("<li><a href='?page=14' class='btn'>&larr;</a></li>"\
                         "<li><a href='?page=15' class='btn btn-primary'>15</a></li>"\
                         "<li><a href='?page=16' class='btn'>16</a></li>", result)
