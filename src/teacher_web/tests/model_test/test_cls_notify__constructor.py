from unittest import TestCase
from shared.models.cls_notification import NotifyModel

class test_cls_notify__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrangee
        self.test = NotifyModel(0, message="", notify_message="", action="", reminder=None, event_type=4, event_log_id=0, auth_user_id=0)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.notify_message)
        self.assertEqual("", self.test.action)
        self.assertEqual(None, self.test.reminder)
        self.assertEqual(0, self.test.event_log_id)
        self.assertEqual(0, self.test.auth_user_id)


    def test_constructor_set_valid_values(self):

        # arrange
        self.test = NotifyModel(1, 
            message="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris commodo magna sem. Suspendisse laoreet varius odio eu varius. Phasellus eu tincidunt risus. Mauris gravida urna at ligula molestie eros.", 
            notify_message="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris commodo magna sem. Suspendisse laoreet varius odio eu varius. Phasellus eu tincidunt risus. Mauris gravida urna at ligula molestie eros.", 
            action="http://localhost/dosomething/1", 
            reminder=None, 
            event_type=1,
            event_log_id=99,
            auth_user_id=21)

        # assert
        self.maxDiff = None

        self.assertEqual(1, self.test.id)
        # trim to 145 characters
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris commodo magna sem. Suspendisse laoreet varius odio eu varius. Phasellus eu tincid", self.test.notify_message)
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris commodo magna sem. Suspendisse laoreet varius odio eu varius. Phasellus eu tincidunt risus. Mauris gravida urna at ligula molestie eros.", self.test.message)
        self.assertEqual("http://localhost/dosomething/1", self.test.action)
        self.assertEqual(None, self.test.reminder)
        self.assertEqual(99, self.test.event_log_id)
        self.assertEqual(21, self.test.auth_user_id)
