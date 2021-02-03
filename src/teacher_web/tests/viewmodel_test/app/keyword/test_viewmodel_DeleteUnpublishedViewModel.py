import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.keywords.viewmodels import KeywordDeleteUnpublishedViewModel  as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_delete__with_exception(self):
        
        # arrange        
        with patch.object(Model, "delete_unpublished", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, scheme_of_work_id=45, auth_user=99)
                

    def test_init_called_delete__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=29, auth_user=99)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            self.assertIsNone(self.viewmodel.model)
            

    def test_init_called_delete__return_item(self):
        
        # arrange
        
        data_to_return = Model(912, "How to save the world in a day")
        data_to_return.published = 2

        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=29, auth_user=99)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            self.assertEqual(912, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.term)
            self.assertEqual(2, self.viewmodel.model.published)
