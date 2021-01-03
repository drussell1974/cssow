from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from django import forms
from shared.models.cls_registereduser import RegisteredUserModel


@skip("TODO: 206 inherit RegisteredUserForm from UserCreationForm -cls_registereduser.RegisterUserModel may not be required")
class test_cls_registereduser_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    
    def test_constructor_default(self):

        # self.test
        self.test = RegisteredUserModel()

        # assert
        self.assertEqual(0, self.test.id)
        self.assertTrue(self.test.is_new())


    @skip("need to mock dango.forms")
    def test_constructor_set_valid_values(self):

        # arrange
        
        mock_form = MagicMock()

        #mock_form.CharField = MagicMock(max_length=30, required=False, help_text='Optional.', returns_value = "xxx")
        #mock_form.CharField = MagicMock(max_length=30, required=False, help_text='Optional.')
        #mock_form.EmailField = MagicMock(max_length=254, help_text='Required. Inform a valid email address.')
        #mock_form.BooleanField = MagicMock(required=True, help_text="Check if this is a staff member. You must also set permissions.")
        
        # act
        self.test = RegisteredUserModel(1, {"first_name":"Lorem", "last_name":"Ipsum", "email":"lorem@ipsum.com", "is_staff":False, "is_active":False})

    
        # assert
        #self.assertEqual(1, self.test.id)
        #self.assertEqual("Lorem", self.test.first_name)
        #self.assertEqual("Ipsum", self.test.last_name)
        #self.assertFalse(self.test.is_staff)
        #self.assertFalse(self.test.is_active)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())


