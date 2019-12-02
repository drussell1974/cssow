from _unittest import TestCase
from cls_reference_note import ReferenceNoteModel


class test_cls_reference_note_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = ReferenceNoteModel(0, reference_id = 0, learning_episode_id = 0, page_note="Note here!")

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual(0, self.test.reference_id)
        self.assertEqual("Note here!", self.test.page_note, "page_note should be ''")
        self.assertEqual("", self.test.page_uri, "uri should be ''")
        self.assertEqual(0, self.test.learning_episode_id, "learning_episode_id should be 0")
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # setup

        self.test = ReferenceNoteModel(6,
                                 reference_id = 1,
                                 page_note="Note here!",
                                 page_uri="http://jazzthecat.co.uk",
                                 learning_episode_id = 1)

        # self.test
        self.test.validate()

        # assert
        self.assertEqual(6, self.test.id)
        self.assertEqual(1, self.test.reference_id)
        self.assertEqual("Note here!", self.test.page_note)
        self.assertEqual("http://jazzthecat.co.uk", self.test.page_uri)
        self.assertEqual(1, self.test.learning_episode_id)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
