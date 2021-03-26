from unittest import TestCase
from shared.models.cls_schemeofwork import SchemeOfWorkModel

from datetime import datetime

class Test_SchemeOfWork__IsRecent(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_is_recent__for_default_instance_returns_false(self):

        test = SchemeOfWorkModel(0, name="KS3 Computing", study_duration=3, start_study_in_year=7)

        self.assertFalse(test.is_recent)



    def test_is_recent__for_old_instance_returns_true(self):

        test = SchemeOfWorkModel(0, name="KS3 Computing", study_duration=3, start_study_in_year=7, is_recent = True)

        self.assertTrue(test.is_recent)
