from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.learningobjectives.viewmodels import LearningObjectiveIndexViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model
from shared.models.cls_solotaxonomy import SoloTaxonomyModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_viewmodel_IndexViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = []

        with patch.object(LessonModel, "get_model", return_value=LessonModel(12)):
            with patch.object(Model, "get_all", return_value=data_to_return):

                db = MagicMock()
                db.cursor = MagicMock()

                # act
                self.viewmodel = ViewModel(db=db, lesson_id = 78, scheme_of_work_id = 92, auth_user=mock_auth_user)

                # assert functions was called
                Model.get_all.assert_called()
                self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(56, solo_taxonomy_id=2).__dict__]
        
        with patch.object(SoloTaxonomyModel,  "get_options", return_value=[SoloTaxonomyModel(1, name="unistructural", lvl=1),SoloTaxonomyModel(2, name="abstract", lvl=2)]):
            with patch.object(LessonModel, "get_model", return_value=LessonModel(12)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    # act
                    self.viewmodel = ViewModel(db=db, lesson_id=19, scheme_of_work_id=84, auth_user=mock_auth_user)

                    # assert functions was called
                    Model.get_all.assert_called()
                    self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = [
            Model(56, solo_taxonomy_id=1).__dict__,
            Model(57, solo_taxonomy_id=2).__dict__,
            Model(58, solo_taxonomy_id=2).__dict__
        ]

        with patch.object(SoloTaxonomyModel,  "get_options", return_value=[SoloTaxonomyModel(1, name="unistructural", lvl=1),SoloTaxonomyModel(2, name="abstract", lvl=2)]):
            with patch.object(LessonModel, "get_model", return_value=LessonModel(12)):
                with patch.object(Model, "get_all", return_value=data_to_return):

                    db = MagicMock()
                    db.cursor = MagicMock()

                    self.mock_model = Mock()

                    # act
                    self.viewmodel = ViewModel(db=db, lesson_id=12, scheme_of_work_id=2, auth_user=mock_auth_user)

                    # assert functions was called
                    Model.get_all.assert_called()
                    self.assertEqual(3, len(self.viewmodel.model))
