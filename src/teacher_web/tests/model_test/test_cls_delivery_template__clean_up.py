from unittest import TestCase
from shared.models.cls_delivery_template import DeliveryTemplateModel


class test_cls_delivery_template__clean_up(TestCase):

    def setUp(self):
        self.test = DeliveryTemplateModel(1, "")


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)

