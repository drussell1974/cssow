from datetime import datetime
from unittest import TestCase
from shared.models.cls_academic_year import AcademicYearModel

class test_cls_academic_year__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrangee

            
        start_date = datetime(year=2020, month=9, day=1)
        end_date = datetime(year=2021, month=8, day=30)

        self.test = AcademicYearModel(start_date, end_date, is_from_db=False)

        # assert
        self.assertEqual("2020-09-01T00:00", self.test.start)
        self.assertEqual("2021-08-30T00:00", self.test.end)
        self.assertEqual("2020/2021", self.test.display)
        self.assertFalse(self.test.is_valid)
        self.assertFalse(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # arrange

        start_date = datetime(year=2020, month=9, day=1)
        end_date = datetime(year=2021, month=8, day=30)

        self.test = AcademicYearModel(start_date, end_date, is_from_db=False)

        # self.test
        self.test.validate()

        # assert
        self.assertEqual("2020-09-01T00:00", self.test.start)
        self.assertEqual("2021-08-30T00:00", self.test.end)
        self.assertEqual("2020/2021", self.test.display)
        self.assertEqual({}, self.test.validation_errors)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
