from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from api.lessons.viewmodels import LessonGetModelViewModel as ViewModel
from shared.models.cls_lesson import LessonDataAccess as DataAccess, LessonModel as Model
from shared.models.cls_keyword import KeywordModel


class test_viewmodel_LessonGetModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__with_exception(self):
        
        # arrange        
        with patch.object(DataAccess, "get_model", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, 99, auth_user=99)


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(DataAccess, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 123, auth_user=99)

            # assert functions was called
            DataAccess.get_model.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_fetch__return_item(self):
        
        # arrange
        
        data_to_return = Model(99)
        
        with patch.object(DataAccess, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, 456, auth_user=99)

            # assert functions was called
            DataAccess.get_model.assert_called()
            self.assertEqual(99, self.viewmodel.model["id"])
            self.assertEqual("", self.viewmodel.model["title"])
            self.assertEqual(0, len(self.viewmodel.model["key_words"]))


    def test_init_called_fetch__return_item__with__key_words(self):
        
        # arrange

        data_to_return = Model(99, "Lorem Ipsum")
        data_to_return.key_words = [
                KeywordModel(34, "CPU"),
                KeywordModel(45, "Fetch Decode Execute"),
                KeywordModel(106, "RAM"),
            ]

        with patch.object(DataAccess, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 69, auth_user=99)

            # assert functions was called
            DataAccess.get_model.assert_called()

            self.assertEqual(99, self.viewmodel.model["id"])
            self.assertEqual("Lorem Ipsum", self.viewmodel.model["title"])
            self.assertEqual(3, len(self.viewmodel.model["key_words"]))
            self.assertEqual("CPU", self.viewmodel.model["key_words"][0]["term"])
            self.assertEqual("RAM", self.viewmodel.model["key_words"][2]["term"])
