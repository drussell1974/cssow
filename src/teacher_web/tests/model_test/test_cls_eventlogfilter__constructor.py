from datetime import datetime, timedelta
from unittest import TestCase
from shared.models.cls_eventlog import EventLogFilter


class fake_settings:
    PAGER = {
        "default":{
            "page": 1,
            "pagesize": 20,
            "pagesize_options": [ 3, 5, 10, 25, 50, 100 ]
        },
        "notifications":{
            "page": 1,
            "pagesize": 100,
            "pagesize_options": [100,]
        },
        "schedule":{
            "page": 1,
            "pagesize": 7,
            "pagesize_options": { 0:"all", 1:"today", 2:"2 days", 7:"1 week", 14:"2 weeks", 28:"28 days" }
        }
    },
    ISOFORMAT = "%Y-%m-%dT%H:%M"


class test_cls_eventlogfilter__constructor(TestCase):

    def setUp(self):
        self.fake_settings = fake_settings()
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = EventLogFilter([ 3, 5, 10, 25, 50, 100 ], 1, 20)
        self.test.date_from = datetime(2020, 7, 23, 7, 9, 20)
        self.test.date_to = datetime(2020, 8, 23, 7, 9, 20)
        

        # assert
        self.assertEqual(datetime(2020, 7, 23, 7, 9, 20), self.test.date_from)
        self.assertEqual(datetime(2020, 8, 23, 7, 9, 20), self.test.date_to)
        self.assertEqual(1, self.test.event_type)
        self.assertEqual("", self.test.category)
        self.assertEqual("", self.test.subcategory)
        self.assertTrue(self.test.is_valid)
        self.assertEqual({}, self.test.validation_errors)


    def test_constructor_valid(self):

        # self.test
        self.test = EventLogFilter( 
            self.fake_settings,
            page=0,
            pagesize=0,
            date_from="23-07-2020 02:31:23",
            date_to="23-08-2020 02:31:23",
            event_type="NONE",
            category="",
            subcategory=""
        )

        # assert
        self.assertEqual("23-07-2020 02:31:23", self.test.date_from)
        self.assertEqual("23-08-2020 02:31:23", self.test.date_to)
        self.assertEqual("NONE", self.test.event_type)
        self.assertEqual("", self.test.category)
        self.assertEqual("", self.test.subcategory)
        self.assertTrue(self.test.is_valid)
        self.assertEqual({}, self.test.validation_errors)


    def test_constructor_date_range_invalid(self):

        # self.test
        self.test = EventLogFilter(
            self.fake_settings.PAGER,
            page=99,
            pagesize=100,
            date_from="23-08-2020 02:31:24",
            date_to="23-08-2020 02:31:23",
            event_type="NONE",
            category="",
            subcategory=""
        )

        # assert
        self.assertEqual("23-08-2020 02:31:24", self.test.date_from)
        self.assertEqual("23-08-2020 02:31:23", self.test.date_to)
        self.assertEqual("NONE", self.test.event_type)
        self.assertEqual("", self.test.category)
        self.assertEqual("", self.test.subcategory)
        self.assertFalse(self.test.is_valid)
        self.assertEqual({'date_from':'date range invalid'}, self.test.validation_errors)