from unittest import TestCase
from shared.models.cls_institute import InstituteContextModel
from shared.models.enums.publlished import STATE

class test_cls_department_context__from_dict(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_should_be_dictionary(self):

        # arrangee

        non_dict_obj = InstituteContextModel(0, "Ultricies")

        # act
        with self.assertRaises(TypeError):
            self.test = InstituteContextModel.empty()
            self.test.from_dict(non_dict_obj)


    def test_should_give_object_from_constructor_default(self):

        # arrange

        dict_obj = InstituteContextModel(0, "Ultricies").__dict__

        # act

        self.test = InstituteContextModel.empty()
        
        self.test.from_dict(dict_obj)

        # assert
        
        self.assertEqual(0, self.test.id)
        self.assertEqual("Ultricies", self.test.name)
        self.assertEqual("Ultricies", self.test.display_name)
        #self.assertEqual(None, self.test.parent_id)
        self.assertEqual(0, self.test.created_by_id)
        self.assertEqual(int(STATE.PUBLISH), self.test.published)
        self.assertEqual("published", self.test.published_state)


    def test_should_give_object_from_constructor_set_valid_values(self):

        # arrange

        dict_obj = InstituteContextModel(7, "Curabitur", description="Sed erat ultricies dapibus.", published=STATE.DRAFT).__dict__

        # act

        self.test = InstituteContextModel.empty()
        
        self.test.from_dict(dict_obj)

        # assert

        self.assertEqual(7, self.test.id)
        self.assertEqual("Curabitur", self.test.name)
        self.assertEqual("Curabitur", self.test.display_name)
        #self.assertEqual(None, self.test.parent_id)
        self.assertEqual(0, self.test.created_by_id)
        self.assertEqual(STATE.DRAFT, self.test.published)
        self.assertEqual("unpublished", self.test.published_state)
