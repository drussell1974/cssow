from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.learningobjectives.viewmodels import LearningObjectiveEditViewModel as ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model
from shared.models.cls_teacher_permission import TeacherPermissionModel

class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_called_save__add_model_to_data(self, check_permission):
        
        # arrange

        mock_model = Model(0, "Proin id massa metus. Aliqua tincidunt.")
        mock_model.solo_taxonomy_id = 1
        mock_model.lesson_id = 134

        on_save__data_to_return = Model(99, "Proin id massa metus. Aliqua tincidunt.")
        
        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(db=self.mock_db, scheme_of_work_id=13, model=mock_model, auth_user=99)
            test_context.execute(published=1)
                            
            # assert functions was called
            
            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.description)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_called_save__add_model_to_data__return_invalid(self, check_permission):
         
        # arrange

        mock_model = Model(99, "Proin id massa metus. Aliqua tincidunt.")
        mock_model.solo_taxonomy_id = 1
        mock_model.lesson_id = 0 # invalid value


        with patch.object(Model, "save", return_value=None):
                
            # act
            
            test_context = ViewModel(db=self.mock_db, scheme_of_work_id=13, model=mock_model, auth_user=99)
            test_context.execute(1)
                            
            # assert save functions was not called
            Model.save.assert_not_called()

            # return the invalid object
            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.description)
            self.assertEqual(0, test_context.model.lesson_id)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual(1, len(test_context.model.validation_errors)) 
            self.assertEqual({'lesson_id': '0 is not a valid range'}, test_context.model.validation_errors) 


    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_should_raise_PermissionError(self, check_permission):
        # arrange 
        mock_model = Model(99, "Proin id massa metus. Aliqua tincidunt.")

        # assert
        with self.assertRaises(PermissionError):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            ViewModel(db=self.mock_db, scheme_of_work_id=13, model=mock_model, auth_user=99)