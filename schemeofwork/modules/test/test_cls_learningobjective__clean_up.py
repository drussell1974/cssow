from unittest import TestCase

import sys
sys.path.insert(0, '../')

from cls_schemeofwork import SchemeOfWorkModel
from schemeofwork_testcase import SchemeOfWork_TestCase

"""
description DONE
solo_taxonomy_id DONE
topic_id = DONE
parent_topic_id = DOING
parent_topic_name = ""
content_id = DONE
content_description = ""
exam_board_id = DONE
exam_board_name = ""
learning_episode_id = DONE
learning_episode_name = ""
key_stage_id = DONE
key_stage_name = ""
parent_id = DONE

"""
class test_SchemeOfWork_clean_up__key_stage_name(SchemeOfWork_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")

class test_SchemeOfWork_clean_up__exam_board_name(SchemeOfWork_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.exam_board_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.exam_board_name, "x")
