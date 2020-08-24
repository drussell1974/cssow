from unittest import TestCase
from shared.models.cls_eventlog import EventLogModel


class test_cls_eventlog__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = EventLogModel(0, 
            created="23-08-2020 02:31:23",
            event_type="NONE",
            message="Mauris dignissim mi at lorem varius condimentum.",
            details="Quisque ut magna eleifend, blandit lorem vitae, molestie magna. Maecenas suscipit, leo vitae pretium lobortis, felis augue euismod ex, nec maximus ex orci eu libero. Nullam fringilla mauris tellus, at consectetur est convallis nec. Curabitur in massa sed nisi egestas efficitur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nibh eros, imperdiet vel pharetra id, finibus id diam. Sed nibh libero, faucibus eget tristique ac, sollicitudin a ante. Mauris nulla felis, cursus eu nibh et, lobortis imperdiet leo. Morbi eu justo et turpis elementum mattis. Cras et magna sit amet leo vehicula posuere tempor eget ante. Phasellus in dui sed lectus consectetur tempor.",
            category="",
            subcategory=""
        )

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("23-08-2020 02:31:23", self.test.created)
        self.assertEqual("NONE", self.test.event_type)
        self.assertEqual("Mauris dignissim mi at lorem varius condimentum.", self.test.message)
        self.assertEqual("Quisque ut magna eleifend, blandit lorem vitae, molestie magna. Maecenas suscipit, leo vitae pretium lobortis, felis augue euismod ex, nec maximus ex orci eu libero. Nullam fringilla mauris tellus, at consectetur est convallis nec. Curabitur in massa sed nisi egestas efficitur. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent nibh eros, imperdiet vel pharetra id, finibus id diam. Sed nibh libero, faucibus eget tristique ac, sollicitudin a ante. Mauris nulla felis, cursus eu nibh et, lobortis imperdiet leo. Morbi eu justo et turpis elementum mattis. Cras et magna sit amet leo vehicula posuere tempor eget ante. Phasellus in dui sed lectus consectetur tempor.", self.test.details)
        self.assertEqual("", self.test.category)
        self.assertEqual("", self.test.subcategory)
