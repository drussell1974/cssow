from unittest import TestCase
from shared.models.enums.publlished import STATE

class test__parse_enum__state(TestCase):

    def setUp(self):
        pass


    def test_FOOBAR_should_raise_error(self):

        # act
        with self.assertRaises(KeyError):
            STATE.parse("FOOBAR")
        

    def test_PUBLISH_should_be__enum__STATE_PUBLISH(self):

        # act
        act_result = STATE.parse("PUBLISH")
        
        # assert
        self.assertEqual(STATE.PUBLISH, act_result)


    def test_DRAFT_should_be__enum__STATE_DRAFT(self):

        # act
        act_result = STATE.parse("DRAFT")
        
        # assert
        self.assertEqual(STATE.DRAFT, act_result)


    def test_DELETE_should_be__enum__STATE_DELETE(self):

        # act
        act_result = STATE.parse("DELETE")
        
        # assert
        self.assertEqual(STATE.DELETE, act_result)
