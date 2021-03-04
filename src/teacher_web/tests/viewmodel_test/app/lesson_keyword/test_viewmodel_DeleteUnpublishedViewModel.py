import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.lesson_keywords.viewmodels import LessonKeywordDeleteUnpublishedViewModel  as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_delete__with_exception(self, mock_auth_user):
        
        # arrange        
        with patch.object(Model, "delete_unpublished", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, scheme_of_work_id=45, lesson_id=101, auth_user=mock_auth_user)
                

    def test_init_called_delete__no_return_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=29, lesson_id=101, auth_user=mock_auth_user)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_delete__return_item(self, mock_auth_user):
        
        # arrange
        
        data_to_return = Model(912, "How to save the world in a day")
        data_to_return.published = STATE.DELETE

        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=29, lesson_id=101, auth_user=mock_auth_user)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            self.assertEqual(912, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.term)
            self.assertEqual(STATE.DELETE, self.viewmodel.model.published)

