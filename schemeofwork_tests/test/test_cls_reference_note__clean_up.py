import sys
sys.path.append('../../schemeofwork/modules')
from cls_reference_note import ReferenceNoteModel

from unittest import TestCase

class test_cls_reference__clean_up(TestCase):

    def setUp(self):
        self.test = ReferenceNoteModel(1, reference_id=1, learning_episode_id = 6, page_note = "")


    def test_page_note__trim_whitespace(self):

        self.test.page_note = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.page_note)


    def test_page_uri__trim_whitespace(self):

        self.test.page_uri = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.page_uri)


    def test_task_icon__trim_whitespace(self):

        self.test.task_icon = " x, y, z "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x, y, z", self.test.task_icon)
