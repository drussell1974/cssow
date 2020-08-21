from unittest import TestCase

class ViewModelTestCase(TestCase):

    def assertViewModelContent(self, viewmodel, exp_page_prefix, exp_main_heading, exp_subheading, exp_validationerrors):

        actual = viewmodel.view().content

        self.assertEqual(exp_page_prefix, "", "page_prefix not as expected")
        self.assertEqual(exp_main_heading, actual["content"]["main_heading"], "main_heading not as expected")
        self.assertEqual(exp_subheading, actual["content"]["sub_heading"], "sub_heading not as expected")
        self.assertEqual(exp_validationerrors, {}, "validationerrors not as expected")
