from unittest import TestCase, skip
from shared.models.cls_reference_note import ReferenceNoteModel

@skip("Deprecated. No longer used")
class test_cls_reference_validate__page_note(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceNoteModel(1, reference_id = 1, lesson_id = 6, page_note = "")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.page_note = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_note" in self.test.validation_errors, "page_note should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.page_note = " x "

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_note" in self.test.validation_errors, "page_note should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.page_note, "x")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.page_note = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("page_note" in self.test.validation_errors, "page_note should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.page_note = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("page_note" in self.test.validation_errors, "page_note should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.page_note = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id ligula tempor pellentesque at at neque. Ut sed viverr. " # length 250 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_note" in self.test.validation_errors, "page_note should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.page_note = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id ligula tempor pellentesque at at neque. Ut sed viverra. " # length 251 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("page_note" in self.test.validation_errors, "page_note should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


@skip("Deprecated. No longer used")
class test_cls_reference_validate__page_uri(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceNoteModel(1, reference_id = 1, lesson_id = 6, page_note = "Test note")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.page_uri = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.page_uri = " "

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.page_uri, "")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # set up

        self.test.page_uri = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.page_uri = None

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.page_uri = "http://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a/consequat/diamy/Class/aptent/taciti/sociosqu/ad/litora/torquent/per/conubia/nostrax/per/inceptos/"\
                        "himenaeosy/Ut/sit/amet/ipsum/non/ante/luctus/gravida/vel/et/metusy/Nunc/iaculis/dolor/non/arcu/condimentumx/sed/posuere/lacus/porttitory/In/est/estx/dapibus/ac/mi/"\
                        "vulputatex/cursus/dapibus/auguey/Mauris/et/nunc/urnay/Integer/orci/urnax/porta/eget/velit/atx/aliquam/maximus/quamy/Integer/varius/sit/amet/nulla/nec/sempery/"\
                        "Pellentesque/non/ante/feugiatx/semper/mauris/sit/ametx/imperdiet/justoy/In/maximus/egestas/elitx/nec/viverra/nisi/aliquam/euy/Vestibulum/vitae/luctus/duiy/Nulla/"\
                        "facilisiy/Aenean/lacinia/leo/in/elit/imperdietx/non/ullamcorper/lorem/commodoy/In/tempus/sem/felisx/nec/vehicula/diam/sagittis/acy/Suspendisse/nisi/quamx/malesuada/non/"\
                        "nisl/utx/consectetur/iaculis/tortory/Nullam/pretium/lectus/ut/eleifend/feugiaty/Sed/tristique/arcu/felisy/Etiam/tempor/risus/vitae/fringilla/commodoy/Praesent/sit/amet/"\
                        "molestie/nequex/sit/amet/suscipit/auguey/Sed/gravida/dictum/ipsum/et/conguey/Praesent/fermentum/congue/turpisx/a/iaculis/elit/convallis/necy/Nam/pretium/erat/ut/ante/"\
                        "pretium/dictumy/Ut/malesuada/iaculis/sem/at/eleifendy/Vivamus/ut/ante/consecteturx/lacinia/ex/vitaex/eleifend/nullay/Nunc/volutpat/ligula/ut/nisl/accumsan/placeraty/"\
                        "Maecenas/erat/nislx/elementum/vel/turpis/egetx/interdum/iaculis/risusy/Duis/ultrices/est/id/lorem/aliquetx/eu/imperdiet/elit/fringillay/Nunc/bibendum/sapien/at/egestas/"\
                        "blandity/Nunc/arcu/magnax/feugiat/at/lectus/gravidax/tempor/consequat/exy/Maecenas/eu/pellentesque/diamy/Integer/congue/semper/rutrumy/Aliquam/suscipit/metus/non/lacus/"\
                        "laoreetx/sed/interdum/dolor/venenatisy/Sed/justo/loremx/mattis/ac/aliquet/sedx/egestas/nec/odioy/Donec/mauris/nibhx/tristique/ut/neque/utx/volutpat/aliquam/antey/"\
                        "Vestibulum/leo/nibhx/tristique/posuere/metus/idx/dictum/pharetra/enimy/Fusce/sed/tellus/viverrax/"\
                        "posuere/enim/etx/dignissim/antey/Interdum/et/malesuada/fames/ac/ante/ipsum/primis/in/faucibusy/Nulla/justo/massax/posuere/vel/rutrum/necx/"\
                        "lus/ac/purusy/Duis/sit/amet/cra/a.html" # length 2083 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.page_uri = "http://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a/consequat/diamy/Class/aptent/taciti/sociosqu/ad/litora/torquent/per/conubia/nostrax/per/inceptos/"\
                        "himenaeosy/Ut/sit/amet/ipsum/non/ante/luctus/gravida/vel/et/metusy/Nunc/iaculis/dolor/non/arcu/condimentumx/sed/posuere/lacus/porttitory/In/est/estx/dapibus/ac/mi/"\
                        "vulputatex/cursus/dapibus/auguey/Mauris/et/nunc/urnay/Integer/orci/urnax/porta/eget/velit/atx/aliquam/maximus/quamy/Integer/varius/sit/amet/nulla/nec/sempery/"\
                        "Pellentesque/non/ante/feugiatx/semper/mauris/sit/ametx/imperdiet/justoy/In/maximus/egestas/elitx/nec/viverra/nisi/aliquam/euy/Vestibulum/vitae/luctus/duiy/Nulla/"\
                        "facilisiy/Aenean/lacinia/leo/in/elit/imperdietx/non/ullamcorper/lorem/commodoy/In/tempus/sem/felisx/nec/vehicula/diam/sagittis/acy/Suspendisse/nisi/quamx/malesuada/non/"\
                        "nisl/utx/consectetur/iaculis/tortory/Nullam/pretium/lectus/ut/eleifend/feugiaty/Sed/tristique/arcu/felisy/Etiam/tempor/risus/vitae/fringilla/commodoy/Praesent/sit/amet/"\
                        "molestie/nequex/sit/amet/suscipit/auguey/Sed/gravida/dictum/ipsum/et/conguey/Praesent/fermentum/congue/turpisx/a/iaculis/elit/convallis/necy/Nam/pretium/erat/ut/ante/"\
                        "pretium/dictumy/Ut/malesuada/iaculis/sem/at/eleifendy/Vivamus/ut/ante/consecteturx/lacinia/ex/vitaex/eleifend/nullay/Nunc/volutpat/ligula/ut/nisl/accumsan/placeraty/"\
                        "Maecenas/erat/nislx/elementum/vel/turpis/egetx/interdum/iaculis/risusy/Duis/ultrices/est/id/lorem/aliquetx/eu/imperdiet/elit/fringillay/Nunc/bibendum/sapien/at/egestas/"\
                        "blandity/Nunc/arcu/magnax/feugiat/at/lectus/gravidax/tempor/consequat/exy/Maecenas/eu/pellentesque/diamy/Integer/congue/semper/rutrumy/Aliquam/suscipit/metus/non/lacus/"\
                        "laoreetx/sed/interdum/dolor/venenatisy/Sed/justo/loremx/mattis/ac/aliquet/sedx/egestas/nec/odioy/Donec/mauris/nibhx/tristique/ut/neque/utx/volutpat/aliquam/antey/"\
                        "Vestibulum/leo/nibhx/tristique/posuere/metus/idx/dictum/pharetra/enimy/Fusce/sed/tellus/viverrax/"\
                        "posuere/enim/etx/dignissim/antey/Interdum/et/malesuada/fames/ac/ante/ipsum/primis/in/faucibusy/Nulla/justo/massax/posuere/vel/rutrum/necx/"\
                        "lus/ac/purusy/Duis/sit/amet/crasam.html" # length 2084 characters
        # test
        self.test.validate()

        # assert
        self.assertTrue("page_uri" in self.test.validation_errors, "page_uri should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_valid__starting_https(self):
        # set up

        self.test.page_uri = "https://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_valid__starting_http(self):
        # set up

        self.test.page_uri = "http://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_valid__http_spelt_incorrectly(self):
        # set up

        self.test.page_uri = "htps://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertTrue("page_uri" in self.test.validation_errors, "page_uri should not have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be True")


    def test_valid__missing_forward_slash(self):
        # set up

        self.test.page_uri = "https:psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertTrue("page_uri" in self.test.validation_errors, "page_uri should not have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be True")


@skip("Deprecated. No longer used")
class test_cls_reference_validate__task_icon(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceNoteModel(1, reference_id = 1, lesson_id = 6, page_note = "Test note", task_icon = "fa-icon")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.task_icon = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.task_icon = " "

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.task_icon, "")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # set up

        self.test.task_icon = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.task_icon = None

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.task_icon = "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89, " \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon, faz" # length 500 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("task_icon" in self.test.validation_errors, "task_icon should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.task_icon = "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89, " \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon1, fa-icon2, fa-icon3, fa-icon4, fa-icon5, fa-icon6, fa-icon7, fa-iconic89" \
                              "fa-icon, fa-1" # length 501 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("task_icon" in self.test.validation_errors, "task_icon should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")
