from tests.model_test._unittest import TestCase
from shared.models.cls_resource import ResourceModel


class test_cls_resource_validate__title(TestCase):

    test = None

    def setUp(self):
        self.test = ResourceModel(1, scheme_of_work_id = 0, lesson_id = 1002, type_id = 3, type_name = "Video", title = "title here!", publisher="YouTube", page_note="Watch this!")


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


class test_cls_resource_validate__page_note(TestCase):

    test = None

    def setUp(self):
        self.test = ResourceModel(1, scheme_of_work_id = 0, lesson_id = 12, type_id = 3, type_name = "Video", title = "title here!", publisher="YouTube", page_note="Read this!")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.page_note = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_note" in self.test.validation_errors, "page_note should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.page_note = " "

        # test
        self.test.validate()

        # assert
        self.assertTrue("page_note" in self.test.validation_errors, "page_note should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.page_note, "")
        self.assertFalse(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
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

        self.test.page_note = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sed sollicitudin orci. In hac habitasse platea dictumst. Sed finibus interdum bibendum. Nunc pharetra enim a vehicula porttitor. Duis ac pulvinar dolor. Integer vehicula, risus vel congue lacinia, odio lorem maximus felis, non laoreet nunc nunc sed ex. Curabitur venenatis, diam non sollicitudin congue, orci magna vulputate lectus, at imperdiet orci est sed sapien. Etiam vitae luctus elit. Suspendisse tempor orci in ex interdum ornare. Nulla sollicitudin maximus felis eget consequat. Integer justo tellus, ornare id sagittis et, tempus eu quam. Suspendisse ut mattis erat. Pellentesque semper justo at semper ornare. Sed tempor efficitur ante vitae vulputate. Vestibulum quis eleifend tortor, eget fringilla magna." \
            "Aenean odio elit, luctus nec turpis sodales, porttitor gravida neque. Morbi vitae faucibus purus. Maecenas eros ex, tempor sed tortor quis, malesuada scelerisque est. Cras quis tincidunt sem. Nunc in nisl tortor. Nunc pellentesque erat justo, a dapibus massa porta ornare. Donec et iaculis augue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sed enim sed mauris sollicitudin accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam et justo auctor, congue nulla quis, sollicitudin lacus. Donec pretium non urna at tincidunt. Fusce efficitur enim vel neque suscipit, nec hendrerit felis vulputate." \
            "Quisque elementum, mauris vitae rhoncus porttitor, dolor felis laoreet justo, ut porttitor ante ex at tortor. Maecenas mollis lacus augue, id ornare tortor pretium ut. Quisque libero ante, lacinia ut eros sed, egestas tristique leo. Suspendisse nunc metus, volutpat sed lobortis ac, ultrices ullamcorper ex. Pellentesque vitae mi eu eros consequat sagittis. Integer eget blandit sem. Aenean ligula ligula, suscipit et ultricies et, cursus ac lacus. Nam ut consectetur dolor. Proin eu erat rhoncus, gravida orci dapibus, mollis metus. Cras mollis faucibus erat." \
            "Nam finibus lacini dictum. Sed volutpat odio dolor, non mattis odio egestas id. Nam sed viverra lacus, ac pellentesque quam. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed interdum tempor mi, vitae consequat orci pellentesque nec. Mauris lacus libero, luctus eu arcu nec, posuere laoreet metus. Sed massa lorem, feugiat sed orci sit amet, lobortis facilisis lectus. Etiam erat ante, consequat at metus luctus, porttitor mollis turpis. Etiam aliquam tempor neque. Nullam orci."
        # length 2500 characters            

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True %s" % self.test.validation_errors)
        self.assertFalse("page_note" in self.test.validation_errors, "page_note should not have validation error %s" % self.test.validation_errors)
        

    def test_max__invalid_extreme(self):
        # set up

        self.test.page_note = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sed sollicitudin orci. In hac habitasse platea dictumst. Sed finibus interdum bibendum. Nunc pharetra enim a vehicula porttitor. Duis ac pulvinar dolor. Integer vehicula, risus vel congue lacinia, odio lorem maximus felis, non laoreet nunc nunc sed ex. Curabitur venenatis, diam non sollicitudin congue, orci magna vulputate lectus, at imperdiet orci est sed sapien. Etiam vitae luctus elit. Suspendisse tempor orci in ex interdum ornare. Nulla sollicitudin maximus felis eget consequat. Integer justo tellus, ornare id sagittis et, tempus eu quam. Suspendisse ut mattis erat. Pellentesque semper justo at semper ornare. Sed tempor efficitur ante vitae vulputate. Vestibulum quis eleifend tortor, eget fringilla magna." \
            "Aenean odio elit, luctus nec turpis sodales, porttitor gravida neque. Morbi vitae faucibus purus. Maecenas eros ex, tempor sed tortor quis, malesuada scelerisque est. Cras quis tincidunt sem. Nunc in nisl tortor. Nunc pellentesque erat justo, a dapibus massa porta ornare. Donec et iaculis augue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sed enim sed mauris sollicitudin accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam et justo auctor, congue nulla quis, sollicitudin lacus. Donec pretium non urna at tincidunt. Fusce efficitur enim vel neque suscipit, nec hendrerit felis vulputate." \
            "Quisque elementum, mauris vitae rhoncus porttitor, dolor felis laoreet justo, ut porttitor ante ex at tortor. Maecenas mollis lacus augue, id ornare tortor pretium ut. Quisque libero ante, lacinia ut eros sed, egestas tristique leo. Suspendisse nunc metus, volutpat sed lobortis ac, ultrices ullamcorper ex. Pellentesque vitae mi eu eros consequat sagittis. Integer eget blandit sem. Aenean ligula ligula, suscipit et ultricies et, cursus ac lacus. Nam ut consectetur dolor. Proin eu erat rhoncus, gravida orci dapibus, mollis metus. Cras mollis faucibus erat." \
            "Nam finibus lacinia dictum. Sed volutpat odio dolor, non mattis odio egestas id. Nam sed viverra lacus, ac pellentesque quam. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed interdum tempor mi, vitae consequat orci pellentesque nec. Mauris lacus libero, luctus eu arcu nec, posuere laoreet metus. Sed massa lorem, feugiat sed orci sit amet, lobortis facilisis lectus. Etiam erat ante, consequat at metus luctus, porttitor mollis turpis. Etiam aliquam tempor neque. Nullam orci.x"
        # length 2501 characters            
 
        # test

        self.test.validate()

        # assert
        self.assertTrue("page_note" in self.test.validation_errors, "page_note should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_resource_validate__page_uri(TestCase):

    test = None

    def setUp(self):
        self.test = ResourceModel(1, lesson_id = 101, type_id = 2, type_name = "Website", title = "title here!", publisher = "Medium.com", page_note="Visit this website", scheme_of_work_id = 0)


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

        self.test.page_uri = " "

        # test
        self.test.validate()

        # assert
        self.assertFalse("page_uri" in self.test.validation_errors, "page_uri should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.page_uri, "")
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

        self.test.uri = "https://psum-dolor.sit/ametx/consectetur/adipiscing/elity/Aenean/a.html"

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("uri" in self.test.validation_errors, "uri should not have validation error %s" % self.test.validation_errors)


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
        self.assertFalse(self.test.is_valid, "is_valid should be True")
        self.assertTrue("page_uri" in self.test.validation_errors, "page_uri should not have validation error %s" % self.test.validation_errors)


class test_cls_resource_validate__publisher(TestCase):

    test = None

    def setUp(self):
        self.test = ResourceModel(1, lesson_id = 301, type_id = 6, type_name = "Book", title = "title here!", publisher = "penguin", page_note="Read this", scheme_of_work_id = 0)


    def tearDown(self):
        pass


    def test_valid_mid(self):
        # set up

        self.test.publisher = "penguin"

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("publisher" in self.test.validation_errors, "publisher should not have validation error %s" % self.test.validation_errors)


    def test_min__valid_extreme(self):
        # set up

        self.test.publisher = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vehicula imperdiet quam. Curabitur lectus augue, vehicula \
            nec mollis imperdiet, pellentesque et tellus. Integer ullamcorper commodo risus et varius. Nam ultrices finibus nisl eu eleifend. Nunc eget felis \
            lectus. Phasellus ultricies semper urna. Fusce mollis imperdiet scelerisque. Duis condimentum velit vitae porttitor lobortis. Nulla quis sem sed tortor \
            pretium volutpat et eget orci. Sed ali."
        # 500 characters

        if len(self.test.publisher) != 500:
            raise Exception("self.test.publisher is ", len(self.test.publisher), "characters long")

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("publisher" in self.test.validation_errors, "publisher should not have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        self.test.publisher = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "should not be is_valid")
        self.assertTrue("publisher" in self.test.validation_errors, "publisher should not have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme_when_None(self):
        # setup
        self.test.publisher = None

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be True")
        self.assertTrue("publisher" in self.test.validation_errors, "publisher should not have validation error %s" % self.test.validation_errors)


    def test_max__valid_extreme(self):
        #setup

        self.test.publisher = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vehicula imperdiet quam. Curabitur lectus augue, vehicula \
            nec mollis imperdiet, pellentesque et tellus. Integer ullamcorper commodo risus et varius. Nam ultrices finibus nisl eu eleifend. Nunc eget felis \
            lectus. Phasellus ultricies semper urna. Fusce mollis imperdiet scelerisque. Duis condimentum velit vitae porttitor lobortis. Nulla quis sem sed tortor \
            pretium volutpat et eget orci. Sed ali."
        # 500 characters
        
        if len(self.test.publisher) != 500:
            raise Exception("self.test.publisher is ", len(self.test.publisher), "characters long")

        # testself.test.publ
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("publisher" in self.test.validation_errors, "publisher should not have validation error %s" % self.test.validation_errors)
        

    def test_max__invalid_extreme(self):
        # setup

        self.test.publisher = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vehicula imperdiet quam. Curabitur lectus augue, vehicula \
            nec mollis imperdiet, pellentesque et tellus. Integer ullamcorper commodo risus et varius. Nam ultrices finibus nisl eu eleifend. Nunc eget felis \
            lectus. Phasellus ultricies semper urna. Fusce mollis imperdiet scelerisque. Duis condimentum velit vitae porttitor lobortis. Nulla quis sem sed tortor \
            pretium volutpat et eget orci. Sed aliquet, dui non tempus porta, justo utx."
        # 501 characters
         
        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be False")
        self.assertTrue("publisher" in self.test.validation_errors, "publisher should have validation error %s" % self.test.validation_errors)


class test_cls_resource_validate__type_id(TestCase):

    test = None

    def setUp(self):
        self.test = ResourceModel(1, scheme_of_work_id = 0, lesson_id = 21, type_id = 6, type_name = "Website", title = "title here!", publisher = "penguin", page_note="A great website")


    def tearDown(self):
        pass


    def test_valid_mid(self):
        # set up

        self.test.type_id = 7

        # test
        self.test.validate()

        # assert
        self.assertFalse("type_id" in self.test.validation_errors, "type_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # set up

        self.test.type_id = 1

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("type_id" in self.test.validation_errors, "type_id should not have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        self.test.type_id = 0

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "should not be is_valid")
        self.assertTrue("type_id" in self.test.validation_errors, "type_id should have validation error %s" % self.test.validation_errors)


    def test_min__invalid_extreme_when_None(self):
        # setup
        self.test.type_id = None

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be True")
        self.assertTrue("type_id" in self.test.validation_errors, "type_id should not have validation error %s" % self.test.validation_errors)


    def test_max__valid_extreme(self):
        #setup
        self.test.type_id = 15

        # test
        self.test.validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertFalse("type_id" in self.test.validation_errors, "type_id should not have validation error %s" % self.test.validation_errors)


    def test_max__invalid_extreme(self):
        # setup
        self.test.type_id = 16 # too far out of possible range

        # test
        self.test.validate()

        # assert
        self.assertFalse(self.test.is_valid, "is_valid should be False")
        self.assertTrue("type_id" in self.test.validation_errors, "type_id should have validation error %s" % self.test.validation_errors)


class test_cls_resource_validate__md_document_name(TestCase):

    test = None

    def setUp(self):
        self.test = ResourceModel(1, scheme_of_work_id = 0, lesson_id = 1002, type_id = 3, type_name = "Video", title = "title here!", publisher="YouTube", page_note="Watch this!")


    def tearDown(self):
        pass


    def test_min__valid_extreme_when_type_is_markdown_document(self):
        # set up

        self.test.md_document_name = "A"
        self.test.type_id = 10
        
        # test
        self.test.validate()

        # assert
        self.assertFalse("md_document_name" in self.test.validation_errors, "md_document_name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_when_type_is_NOT_markdown_document(self):
        # set up

        self.test.md_document_name = "A"
        self.test.type_id = 1
        
        # test
        self.test.validate()

        # assert
        self.assertFalse("md_document_name" in self.test.validation_errors, "md_document_name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.md_document_name = " x "
        self.test.type_id = 10
        
        # test
        self.test.validate()

        # assert
        self.assertFalse("md_document_name" in self.test.validation_errors, "md_document_name should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.md_document_name, "x")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme_when_type_is_markdown_document(self):
        # set up

        self.test.md_document_name = ""
        self.test.type_id = 10

        # test
        self.test.validate()

        # assert
        self.assertTrue("md_document_name" in self.test.validation_errors, "md_document_name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_type_is_NOT_markdown_document(self):
        # set up

        self.test.md_document_name = ""
        self.test.type_id = 1

        # test
        self.test.validate()

        # assert
        self.assertFalse("md_document_name" in self.test.validation_errors, "md_document_name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should be is_valid")


    def test_min__invalid_extreme_when_None_and_type_is_markdown_document(self):
        # set up

        self.test.md_document_name = None
        self.test.type_id = 10

        # test
        self.test.validate()

        # assert
        self.assertTrue("md_document_name" in self.test.validation_errors, "md_document_name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_min__invalid_extreme_when_None_and_type_is_NOT_markdown_document(self):
        # set up

        self.test.md_document_name = None
        self.test.type_id = 1

        # test
        self.test.validate()

        # assert
        self.assertFalse("md_document_name" in self.test.validation_errors, "md_document_name should NOT have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__valid_extreme_when_type_is_markdown_document(self):
        # set up

        self.test.md_document_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id lig." # length 200 characters
        self.test.type_id = 10
        
        # test
        self.test.validate()

        # assert
        self.assertFalse("md_document_name" in self.test.validation_errors, "md_document_name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme_when_type_is_markdown_document(self):
        # set up

        self.test.md_document_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id ligula tempor pellentesque at at neque. Ut sed viverra mauris. " \
                          "Fusce commodo, nisi in pellentesque yamet." # length 201 characters
        self.test.type_id = 10
        
        # test
        self.test.validate()

        # assert
        self.assertTrue("md_document_name" in self.test.validation_errors, "md_document_name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")

