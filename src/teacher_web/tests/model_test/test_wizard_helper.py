from unittest import TestCase
from unittest.mock import Mock
from shared.wizard_helper import WizardHelper

class test_wizard_helper(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrangee

        self.test = WizardHelper(default_url="/")

        # assert
        self.assertIsNone(self.test.next_url)
        self.assertIsNone(self.test.add_another_url)
        self.assertEqual("/", self.test.default_url)


    def test_constructor_set_valid_values(self):

        # arrange

        self.test = WizardHelper(next_url="/this-url-is-the-next_url", add_another_url="/this-url-is-the-add_another_url", default_url="/this-url-is-the-default_url")

        # assert
        self.assertEqual("/this-url-is-the-next_url", self.test.next_url)
        self.assertEqual("/this-url-is-the-add_another_url", self.test.add_another_url)
        self.assertEqual("/this-url-is-the-default_url", self.test.default_url)


    def test_get_redirect_url__should_use_default_url__when__request__is_none(self):

        # arrange

        self.test = WizardHelper(default_url="/this-url-is-the-default_url")
        
        # act
        
        act_result = self.test.get_redirect_url(None)
        
        # assert
        self.assertEqual("/this-url-is-the-default_url", act_result)


    def test_get_redirect_url__should_use_default_url___when__wizard_mode__is_none(self):

        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
            "wizard_mode": None
        }

        self.test = WizardHelper(default_url="/this-url-is-the-default_url")

        # act
        
        act_result = self.test.get_redirect_url(mock_request)
        
        # assert
        self.assertEqual("/this-url-is-the-default_url", act_result)
