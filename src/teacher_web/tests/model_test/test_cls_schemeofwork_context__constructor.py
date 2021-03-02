from unittest import TestCase
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.enums.publlished import STATE

class test_cls_department_context__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrangee

        self.test = SchemeOfWorkContextModel(0, "Lorem ipsum")

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("Lorem ipsum", self.test.name)
        self.assertEqual("Lorem ipsum", self.test.display_name)
        #self.assertEqual(None, self.test.parent_id)
        self.assertEqual(0, self.test.created_by_id)
        self.assertEqual(int(STATE.PUBLISH), self.test.published)
        self.assertEqual("published", self.test.published_state)


    def test_constructor_set_valid_values(self):

        # arrange

        self.test = SchemeOfWorkContextModel(7, "Curabitur", description="Sed erat ultricies dapibus.")

        # assert
        self.assertEqual(7, self.test.id)
        self.assertEqual("Curabitur", self.test.name)
        self.assertEqual("Curabitur", self.test.display_name)
        #self.assertEqual(None, self.test.parent_id)
        self.assertEqual(0, self.test.created_by_id)
        self.assertEqual(int(STATE.PUBLISH), self.test.published)
        self.assertEqual("published", self.test.published_state)
