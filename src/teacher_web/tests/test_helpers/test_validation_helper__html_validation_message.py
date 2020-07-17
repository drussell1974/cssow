from unittest import TestCase
from shared.models.core.validation_helper import html_validation_message

class test_validation_helper__html_validation_message(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__none_if_there_are_no_messages(self):
        result = html_validation_message("")
        self.assertEqual(None, result)

    def test__show_single_validation_message(self):
        result = html_validation_message({"field":"is invalid"})
        self.assertEqual("<b>field</b> is invalid<br>", result)

    def test__show_multiple_validation_messages(self):
        result = html_validation_message({"field1":"is invalid", "field2":"is invalid", "field3":"is invalid", "field4":"is invalid", "field5":"is invalid", "field6":"is invalid", "field7":"is invalid", "field8":"is invalid", "field9":"is invalid", "field10":"is invalid"})
        self.assertTrue("<b>field1</b> is invalid<br>" in result)
        self.assertTrue("<b>field2</b> is invalid<br>" in result)
        self.assertTrue("<b>field3</b> is invalid<br>" in result)
        self.assertTrue("<b>field4</b> is invalid<br>" in result)
        self.assertTrue("<b>field5</b> is invalid<br>" in result)
        self.assertTrue("<b>field6</b> is invalid<br>" in result)
        self.assertTrue("<b>field7</b> is invalid<br>" in result)
        self.assertTrue("<b>field8</b> is invalid<br>" in result)
        self.assertTrue("<b>field9</b> is invalid<br>" in result)
        self.assertTrue("<b>field10</b> is invalid<br>" in result)

