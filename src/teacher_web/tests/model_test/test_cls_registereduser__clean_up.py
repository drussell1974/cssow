from unittest import TestCase, skip
from shared.models.cls_registereduser import RegisteredUserModel

from unittest import TestCase

@skip("TODO: 206 inherit RegisteredUserForm from UserCreationForm -cls_registereduser.RegisterUserModel may not be required")
class test_cls_resource__clean_up(TestCase):

    def setUp(self):
        self.test = RegisteredUserModel()


    # first_name

    def test_first_name__trim_whitespace(self):

        self.test.first_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.first_name)


    # last_name

    def test_last_name__trim_whitespace(self):

        self.test.last_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.last_name)


    # email

    def test_email__trim_whitespace(self):

        self.test.email = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.email)
