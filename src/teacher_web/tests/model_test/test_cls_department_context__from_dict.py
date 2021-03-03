from unittest import TestCase
from shared.models.cls_department import DepartmentContextModel
from shared.models.enums.publlished import STATE

class test_cls_department_context__from_dict(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_should_be_dictionary(self):

        # arrangee

        non_dict_obj = DepartmentContextModel(0, "Lorem ipsum")

        # act
        with self.assertRaises(TypeError):
            self.test = DepartmentContextModel.empty()
            self.test.from_dict(non_dict_obj)


    def test_should_give_object_from_constructor_default(self):

        # arrange

        dict_obj = DepartmentContextModel(0, "Lorem ipsum").__dict__

        # act
        
        self.test = DepartmentContextModel.empty()
        
        self.test.from_dict(dict_obj)

        # assert

        self.assertEqual(0, self.test.id)
        self.assertEqual("Lorem ipsum", self.test.name)
        self.assertEqual("Lorem ipsum", self.test.display_name)
        #self.assertEqual(None, self.test.parent_id)
        self.assertEqual(0, self.test.created_by_id)
        self.assertEqual(int(STATE.PUBLISH), self.test.published)
        self.assertEqual("published", self.test.published_state)
        self.assertFalse(self.test.is_from_db)


    def test_should_give_object_from_constructor_set_valid_values(self):

        # arrange

        dict_obj = DepartmentContextModel(1, "Sor shurem", description="Curabitur vulputate leo sed erat ultricies dapibus.", published=STATE.DRAFT, is_from_db=True).__dict__

        # act
        
        self.test = DepartmentContextModel.empty()
        
        self.test.from_dict(dict_obj)

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("Sor shurem", self.test.name)
        self.assertEqual("Sor shurem", self.test.display_name)
        #self.assertEqual(None, self.test.parent_id)
        self.assertEqual(0, self.test.created_by_id)
        self.assertEqual(STATE.DRAFT, self.test.published)
        self.assertEqual("unpublished", self.test.published_state)
        self.assertTrue(self.test.is_from_db)
