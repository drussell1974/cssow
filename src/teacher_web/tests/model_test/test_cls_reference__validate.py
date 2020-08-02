from unittest import TestCase, skip
from shared.models.cls_reference import ReferenceModel


@skip("Deprecated. No longer used")
class test_cls_reference_validate__title(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceModel(1, reference_type_id = 6, reference_type_name = "Website", title = "title here!", publisher = "penguin", year_published = 2016, scheme_of_work_id = 0)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.title = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("title" in self.test.validation_errors, "title should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.title = " x "

        # test
        self.test.validate()

        # assert
        self.assertFalse("title" in self.test.validation_errors, "title should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.title, "x")
        self.assertTrue(self.test.is_valid, "is_valid should be True")

    def test_min__invalid_extreme(self):
        # set up

        self.test.title = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("title" in self.test.validation_errors, "title should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.title = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("title" in self.test.validation_errors, "title should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.title = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id ligula tempor pellentesque at at neque. Ut sed viverra mauris. " \
                          "Fusce commodo, nisi in pellentesque amet." # length 300 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("title" in self.test.validation_errors, "title should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.title = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id ligula tempor pellentesque at at neque. Ut sed viverra mauris. " \
                          "Fusce commodo, nisi in pellentesque yamet." # length 301 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("title" in self.test.validation_errors, "title should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


@skip("Deprecated. No longer used")
class test_cls_reference_validate__authors(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceModel(1, reference_type_id = 6, reference_type_name = "Website", title = "title here!", publisher = "penguin", year_published = 2016, scheme_of_work_id = 0)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.authors = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("authors" in self.test.validation_errors, "authors should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.authors = " "

        # test
        self.test.validate()

        # assert
        self.assertFalse("authors" in self.test.validation_errors, "authors should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.authors, "")
        self.assertTrue(self.test.is_valid, "is_valid should be True")

    def test_min__valid_extreme(self):
        # set up

        self.test.authors = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("authors" in self.test.validation_errors, "authors should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.authors = None

        # test
        self.test.validate()

        # assert
        self.assertFalse("authors" in self.test.validation_errors, "authors should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.authors = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis metus urna, at tempor felis sollicitudin at. " \
                            "In nisi nisl, faucibus at tortor et, cursus aliquet ante. Lorem ipsum dolor sit amet." # length 200 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("authors" in self.test.validation_errors, "authors should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.authors = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis metus urna, at tempor felis sollicitudin at. " \
                            "In nisi nisl, faucibus at tortor et, cursus aliquet ante. Lorem ipsum dolor sit yamet." # length 201 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("authors" in self.test.validation_errors, "authors should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


@skip("Deprecated. No longer used")
class test_cls_reference_validate__uri(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceModel(1, reference_type_id = 6, reference_type_name = "Website", title = "title here!", publisher = "penguin", year_published = 2016, scheme_of_work_id = 0)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.uri = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("uri" in self.test.validation_errors, "uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.uri = " "

        # test
        self.test.validate()

        # assert
        self.assertFalse("uri" in self.test.validation_errors, "uri should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.uri, "")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # set up

        self.test.uri = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("uri" in self.test.validation_errors, "uri should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.uri = None

        # test
        self.test.validate()

        # assert
        self.assertFalse("uri" in self.test.validation_errors, "uri should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.uri = "http://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a/consequat/diamy/Class/aptent/taciti/sociosqu/ad/litora/torquent/per/conubia/nostrax/per/inceptos/"\
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
        self.assertFalse("uri" in self.test.validation_errors, "uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.uri = "http://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a/consequat/diamy/Class/aptent/taciti/sociosqu/ad/litora/torquent/per/conubia/nostrax/per/inceptos/"\
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
        self.assertTrue("uri" in self.test.validation_errors, "uri should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_valid__starting_https(self):
        # set up

        self.test.uri = "https://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertFalse("uri" in self.test.validation_errors, "uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_valid__starting_http(self):
        # set up

        self.test.uri = "http://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertFalse("uri" in self.test.validation_errors, "uri should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_valid__http_spelt_incorrectly(self):
        # set up

        self.test.uri = "htps://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertTrue("uri" in self.test.validation_errors, "uri should not have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be True")


    def test_valid__missing_forward_slash(self):
        # set up

        self.test.uri = "https:psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertTrue("uri" in self.test.validation_errors, "uri should not have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be True")


@skip("Deprecated. No longer used")
class test_cls_reference_validate__year_published(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceModel(1, reference_type_id = 6, reference_type_name = "Website", title = "title here!", publisher = "penguin", year_published = 2016, scheme_of_work_id = 0)


    def tearDown(self):
        pass


    def test_valid_mid(self):
        # set up

        self.test.year_published = 2016

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("year_published" in self.test.validation_errors, "year_published should not have validation error %s" % self.test.validation_errors)


    def test_min__valid_extreme(self):
        # set up

        self.test.year_published = 1100

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("year_published" in self.test.validation_errors, "year_published should not have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        self.test.year_published = 1099

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "should not be is_valid")
        self.assertTrue("year_published" in self.test.validation_errors, "year_published should not have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme_when_None(self):
        # setup
        self.test.year_published = None

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be True")
        self.assertTrue("year_published" in self.test.validation_errors, "year_published should not have validation error %s" % self.test.validation_errors)


    def test_max__valid_extreme(self):
        #setup
        self.test.year_published = 2100

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("year_published" in self.test.validation_errors, "year_published should not have validation error %s" % self.test.validation_errors)


    def test_max__invalid_extreme(self):
        # setup
        self.test.year_published = 2101 # too far out of possible range

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be False")
        self.assertTrue("year_published" in self.test.validation_errors, "year_published should have validation error %s" % self.test.validation_errors)


@skip("Deprecated. No longer used")
class test_cls_reference_validate__reference_type_id(TestCase):

    test = None

    def setUp(self):
        self.test = ReferenceModel(1, reference_type_id = 6, reference_type_name = "Website", title = "title here!", publisher = "penguin", year_published = 2016, scheme_of_work_id = 0)


    def tearDown(self):
        pass


    def test_valid_mid(self):
        # set up

        self.test.reference_type_id = 7

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("reference_type_id" in self.test.validation_errors, "reference_type_id should not have validation error %s" % self.test.validation_errors)


    def test_min__valid_extreme(self):
        # set up

        self.test.reference_type_id = 15

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("reference_type_id" in self.test.validation_errors, "reference_type_id should not have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        self.test.reference_type_id = 0

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "should not be is_valid")
        self.assertTrue("reference_type_id" in self.test.validation_errors, "reference_type_id should not have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme_when_None(self):
        # setup
        self.test.reference_type_id = None

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be True")
        self.assertTrue("reference_type_id" in self.test.validation_errors, "reference_type_id should not have validation error %s" % self.test.validation_errors)


    def test_max__valid_extreme(self):
        #setup
        self.test.reference_type_id = 15

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("reference_type_id" in self.test.validation_errors, "reference_type_id should not have validation error %s" % self.test.validation_errors)


    def test_max__invalid_extreme(self):
        # setup
        self.test.reference_type_id = 16 # too far out of possible range

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be False")
        self.assertTrue("reference_type_id" in self.test.validation_errors, "reference_type_id should have validation error %s" % self.test.validation_errors)
