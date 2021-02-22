from unittest import TestCase, skip
from tests.model_test.learningobjective_testcase import LearningObjective_TestCase
from shared.models.cls_institute import InstituteModel


class test_institute_validate__name(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.name = "A"

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.name = " x "

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.name, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.name = ""

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.name = None

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")
        
        test.name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse e" # length 70 characters

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse el"  # length 71 characters

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_institute_validate__description(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.description = "A"

        # act
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.description = " x "

        # act
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.description, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.description = ""

        # act
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "should be is_valid")


    def test_min__valid_extreme_when_None(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.description = None

        # act
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__valid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")
        
        test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vulputate leo sed erat ultricies dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nec molestie quam, vel rutrum tellus. Aenean aliquam volutpat tortor, sit amet pulvinar elit sollicitudin et. Aliquam et feugiat orci. Nam semper egestas condimentum. Fusce sollicitudin, leo quis mollis condimentum, nulla mauris laoreet nulla, vel tincidunt purus nisi sit amet nisi. Vestibulum quis ullamcorper nisi, at rutrum leo. Curabitur sed orci volutpat, rutrum justo vel, commodo arcu."\
            "Pellentesque ornare vel nisl vitae tincidunt. Fusce eros ipsum, vulputate vel orci nec, malesuada consectetur dolor. Donec diam velit, cursus vel erat a, rutrum feugiat tortor. Nam hendrerit, tortor eu blandit vestibulum, est lacus imperdiet lorem, quis iaculis est neque nec neque. Sed luctus leo et odio hendrerit auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris maximus interdum rhoncus. Vivamus porta dui in eros varius accumsan. In porta pharetra rhoncus. Vivamus in malesuada libero, a commodo quam. Sed vel commodo neque, eu convallis turpis. Praesent tempor orci ornare, efficitur lorem non, commodo enim."\
            "Etiam lobortis bibendum felis. Nam nec pulvinar lectus. Maecenas molestie ligula eget molestie dapibus. Mauris vel laoreet elit, ut ultrices lorem. Nam mattis quis nulla ut imperdiet. Fusce elementum mi a nibh tincidunt finibus. Morbi ac sem ac massa cursus sodales. Etiam in condimentum nulla. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Nulla quis porta justo, nec ornare risus. Nulla venenatis odio eu turpis vehicula, a iaculis risus tincidunt. Cras at bibendum mi. Proin mi lorem, tincidunt non sagittis id, semper non sem. Proin imperdiet lorem nunc, vel ultrices turpis tincidunt in."\
            "In sagittis consectetur arcu, vel viverra justo bibendum et. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse finibus, lacus quis hendrerit accumsan, neque metus aliquam mauris, sed tincidunt enim elit et elit. Quisque sed ante in magna blandit maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer at dolor laoreet, ornare nisi ut, pharetra urna. Etiam volutpat nec enim in pulvinar. Etiam non vestibulum tellus. Nulla tincidunt lorem nec lectus mollis, et auctor ante porttitor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse at magna pulvinar, mattis lectus eu, volutpat nisl. Nulla id feugiat libero."\
            "In purus urna, commodo sed purus a, molestie interdum dui. Aliquam vulputate elit neque, vulputate lobortis urna sodales in. Donec sagittis suscipit metus, et facilisis ipsum maximus nec. Fusce arcu metus, imperdiet ut augue id, hendrerit tincidunt velit. Ut in nisl dictum, semper tellus at, suscipit nisl. Vivamus sodales tortor quis metus bibendum accumsan. Phasellus quis risus nec urna mattis scelerisque. Mauris posuere cursus augue, et rutrum ex varius a."\
            "Phasellus rutrum tellus in posuere mattis. Sed auctor tempus odio, a tempus diam sollicitudin in. Sed diam nulla, hendrerit sed aliquet eget, varius ut purus. Curabitur laoreet, erat at elementum dictum, leo felis aliquam orci, ut faucibus velit leo et odio. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam blandit arcu quam, eu pretium eros tincidunt vel. Integer fringilla efficitur ipsum a suscipit. Donec aliquet diam ac mauris semper consequat. Nunc lacus sem, consequat ac imperdiet ac, tempor et mi. Donec arcu urna, ornare sed sagittis non, aliquet id neque. Praesent eros metus, tincidunt a feugiat vel, efficitur eget lorem. Nulla tincidunt efficitur elementum. Donec eu cursus sem. In ultricies sit amet risus eu convallis."\
            "Suspendisse dui felis, fringilla sed erat id, tincidunt ultrices nibh. Cras consectetur nibh nec ligula egestas sollicitudin. Nullam ut lectus eget massa lacinia mattis eu sed ligula. Nullam lectus magna, efficitur vel orci ac, luctus condimentum magna. Cras condimentum nisi quis enim ultrices egestas. Morbi vel vehicula urna. Nam posuere, ipsum in commodo fermentum, ante nisi blandit nunc, dapibus hendrerit nisi erat vel quam. Donec sit amet nulla semper, feugiat nulla a, convallis lacus. Fusce sagittis urna et leo porta, eu convallis orci placerat. Vestibulum vitae sagittis orci, et volutpat leo. Quisque nisi lacus, egestas vitae nibh ut, mollis blandit felis. Integer tincidunt neque dui. Integer ullamcorper iaculis ipsum, eget gravida nisl pellentesque vel. Aenean efficitur cursus neque. Ut velit turpis, dapibus vitae suscipit vitae, auctor sed erat. Aliquam tempor, eros eget porttitor mollis, urna erat lobortis nibh, eu vulputate nisl lorem vel dui."\
            "Praesent imperdiet sodales vehicula. Nunc eget tellus odio. Donec magna mi, rhoncus in dignissim sit amet, molestie in elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur dapibus nam." 
            # length 5000 characters

        # act
        test.validate()

        # assert
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = InstituteModel(1, "Lorem ipsum")

        test.description = "XLorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vulputate leo sed erat ultricies dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nec molestie quam, vel rutrum tellus. Aenean aliquam volutpat tortor, sit amet pulvinar elit sollicitudin et. Aliquam et feugiat orci. Nam semper egestas condimentum. Fusce sollicitudin, leo quis mollis condimentum, nulla mauris laoreet nulla, vel tincidunt purus nisi sit amet nisi. Vestibulum quis ullamcorper nisi, at rutrum leo. Curabitur sed orci volutpat, rutrum justo vel, commodo arcu."\
            "Pellentesque ornare vel nisl vitae tincidunt. Fusce eros ipsum, vulputate vel orci nec, malesuada consectetur dolor. Donec diam velit, cursus vel erat a, rutrum feugiat tortor. Nam hendrerit, tortor eu blandit vestibulum, est lacus imperdiet lorem, quis iaculis est neque nec neque. Sed luctus leo et odio hendrerit auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris maximus interdum rhoncus. Vivamus porta dui in eros varius accumsan. In porta pharetra rhoncus. Vivamus in malesuada libero, a commodo quam. Sed vel commodo neque, eu convallis turpis. Praesent tempor orci ornare, efficitur lorem non, commodo enim."\
            "Etiam lobortis bibendum felis. Nam nec pulvinar lectus. Maecenas molestie ligula eget molestie dapibus. Mauris vel laoreet elit, ut ultrices lorem. Nam mattis quis nulla ut imperdiet. Fusce elementum mi a nibh tincidunt finibus. Morbi ac sem ac massa cursus sodales. Etiam in condimentum nulla. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Nulla quis porta justo, nec ornare risus. Nulla venenatis odio eu turpis vehicula, a iaculis risus tincidunt. Cras at bibendum mi. Proin mi lorem, tincidunt non sagittis id, semper non sem. Proin imperdiet lorem nunc, vel ultrices turpis tincidunt in."\
            "In sagittis consectetur arcu, vel viverra justo bibendum et. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse finibus, lacus quis hendrerit accumsan, neque metus aliquam mauris, sed tincidunt enim elit et elit. Quisque sed ante in magna blandit maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer at dolor laoreet, ornare nisi ut, pharetra urna. Etiam volutpat nec enim in pulvinar. Etiam non vestibulum tellus. Nulla tincidunt lorem nec lectus mollis, et auctor ante porttitor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse at magna pulvinar, mattis lectus eu, volutpat nisl. Nulla id feugiat libero."\
            "In purus urna, commodo sed purus a, molestie interdum dui. Aliquam vulputate elit neque, vulputate lobortis urna sodales in. Donec sagittis suscipit metus, et facilisis ipsum maximus nec. Fusce arcu metus, imperdiet ut augue id, hendrerit tincidunt velit. Ut in nisl dictum, semper tellus at, suscipit nisl. Vivamus sodales tortor quis metus bibendum accumsan. Phasellus quis risus nec urna mattis scelerisque. Mauris posuere cursus augue, et rutrum ex varius a."\
            "Phasellus rutrum tellus in posuere mattis. Sed auctor tempus odio, a tempus diam sollicitudin in. Sed diam nulla, hendrerit sed aliquet eget, varius ut purus. Curabitur laoreet, erat at elementum dictum, leo felis aliquam orci, ut faucibus velit leo et odio. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam blandit arcu quam, eu pretium eros tincidunt vel. Integer fringilla efficitur ipsum a suscipit. Donec aliquet diam ac mauris semper consequat. Nunc lacus sem, consequat ac imperdiet ac, tempor et mi. Donec arcu urna, ornare sed sagittis non, aliquet id neque. Praesent eros metus, tincidunt a feugiat vel, efficitur eget lorem. Nulla tincidunt efficitur elementum. Donec eu cursus sem. In ultricies sit amet risus eu convallis."\
            "Suspendisse dui felis, fringilla sed erat id, tincidunt ultrices nibh. Cras consectetur nibh nec ligula egestas sollicitudin. Nullam ut lectus eget massa lacinia mattis eu sed ligula. Nullam lectus magna, efficitur vel orci ac, luctus condimentum magna. Cras condimentum nisi quis enim ultrices egestas. Morbi vel vehicula urna. Nam posuere, ipsum in commodo fermentum, ante nisi blandit nunc, dapibus hendrerit nisi erat vel quam. Donec sit amet nulla semper, feugiat nulla a, convallis lacus. Fusce sagittis urna et leo porta, eu convallis orci placerat. Vestibulum vitae sagittis orci, et volutpat leo. Quisque nisi lacus, egestas vitae nibh ut, mollis blandit felis. Integer tincidunt neque dui. Integer ullamcorper iaculis ipsum, eget gravida nisl pellentesque vel. Aenean efficitur cursus neque. Ut velit turpis, dapibus vitae suscipit vitae, auctor sed erat. Aliquam tempor, eros eget porttitor mollis, urna erat lobortis nibh, eu vulputate nisl lorem vel dui."\
            "Praesent imperdiet sodales vehicula. Nunc eget tellus odio. Donec magna mi, rhoncus in dignissim sit amet, molestie in elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur dapibus nam." 
            # length 5001 characters

        # act
        test.validate()

        # assert
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
