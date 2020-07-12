from tests.model_test._unittest import TestCase
from web.shared.models.cls_schemeofwork import SchemeOfWorkModel

from datetime import datetime

class Test_SchemeOfWork__IsRecent(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_is_recent__for_default_instance_returns_false(self):

        test = SchemeOfWorkModel(0)

        self.assertFalse(test.is_recent)



    def test_is_recent__for_old_instance_returns_true(self):

        test = SchemeOfWorkModel(0, is_recent = True)

        self.assertTrue(test.is_recent)
