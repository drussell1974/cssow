from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from django.http import Http404
from api.lessons.viewmodels import LessonGetModelViewModel as ViewModel
from shared.models.core.context import Ctx
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_keyword import KeywordModel
from tests.test_helpers.mocks import fake_ctx_model


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_LessonGetModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__with_exception(self, mock_ctx_model):
        
        # arrange        
        with patch.object(Model, "get_model", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, 99, scheme_of_work_id=22, auth_user=99)
            #TODO: #233 remove self.assertRaises
             
            # assert
            #TODO: #233 assert error_message
            #self.assertEqual("ERROR MESSAGE HERE!!!", self.viewmodel.error_message)


    def test_init_called_fetch__no_return(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            with self.assertRaises(Http404):
                self.viewmodel = ViewModel(db, 123, scheme_of_work_id=22, auth_user=99)

                # assert functions was called
                Model.get_model.assert_called()
                self.assertIsNone(self.viewmodel.model)


    def test_init_called_fetch__return_item(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = Model(99, is_from_db=True)
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, 456, scheme_of_work_id=22, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(99, self.viewmodel.model["id"])
            self.assertEqual("", self.viewmodel.model["title"])
            self.assertEqual(0, len(self.viewmodel.model["key_words"]))


    def test_init_called_fetch__return_item__with__key_words(self, mock_ctx_model):
        
        # arrange

        data_to_return = Model(99, "Lorem Ipsum", is_from_db=True)
        data_to_return.key_words = [
                KeywordModel(34, "CPU"),
                KeywordModel(45, "Fetch Decode Execute"),
                KeywordModel(106, "RAM"),
            ]

        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 69, scheme_of_work_id=22, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()

            self.assertEqual(99, self.viewmodel.model["id"])
            self.assertEqual("Lorem Ipsum", self.viewmodel.model["title"])
            self.assertEqual(3, len(self.viewmodel.model["key_words"]))
            self.assertEqual("CPU", self.viewmodel.model["key_words"][0]["term"])
            self.assertEqual("RAM", self.viewmodel.model["key_words"][2]["term"])
