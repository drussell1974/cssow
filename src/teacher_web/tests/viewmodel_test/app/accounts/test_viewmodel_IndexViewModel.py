from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.teampermissions.viewmodels import TeamPermissionIndexViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from tests.test_helpers.mocks import fake_ctx_model


class test_viewmodel_TeamPermissionsIndexViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(TeacherPermissionModel, "get_team_permissions", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            fake_request = Mock()
            
            # act
            viewmodel = ViewModel(db=db, request=fake_request, auth_user=6079)
            actual_result = viewmodel.view()
            
            # assert functions was called
            TeacherPermissionModel.get_team_permissions.assert_called()
            self.assertEqual(4, len(actual_result.content))
            

    def test_init_called_fetch__single_item(self):
        
        # arrange
        data_to_return = [
            TeacherPermissionModel(
                teacher_id=24,
                teacher_name="Jane Doe", #DepartmentModel(15, "Computer Science")), 
                scheme_of_work=MagicMock(id = 69, name="GCSE Computer Science"), 
                published=1,
                department_permission=DEPARTMENT.TEACHER, 
                scheme_of_work_permission=SCHEMEOFWORK.EDITOR, 
                lesson_permission=LESSON.EDITOR,
                ctx=fake_ctx_model()
            )
        ]
        
        with patch.object(TeacherPermissionModel, "get_team_permissions", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            fake_request = Mock()
            
            # act
            viewmodel = ViewModel(db=db, request=fake_request, auth_user=6079)
            actual_result = viewmodel.view()
            
            # assert functions was called
            TeacherPermissionModel.get_team_permissions.assert_called()

            self.assertEqual(1, len(actual_result.content["content"]["data"]["my_team_permissions"]))        
            


    def test_init_called_fetch__multiples_items(self):
        
        # arrange

        #data_to_return = [DepartmentModel(34, "Computer Science"), DepartmentModel(35, "Information Technology"), DepartmentModel(36, "Electronics")]
        data_to_return = [
            TeacherPermissionModel(
                teacher_id=1, 
                teacher_name="Mr Russell", #DepartmentModel(15, "Computer Science")), 
                scheme_of_work=MagicMock(id = 67, name="GCSE Computer Science"), 
                published=1,
                department_permission=int(DEPARTMENT.HEAD), 
                scheme_of_work_permission=int(SCHEMEOFWORK.OWNER),
                lesson_permission=int(LESSON.OWNER),
                ctx=fake_ctx_model()    
            ), 
            TeacherPermissionModel(
                teacher_id=2, 
                teacher_name="Jane Doe", #DepartmentModel(15, "Computer Science")), 
                scheme_of_work=MagicMock(id = 68, name="A-Level Computer Science"), 
                published=1,
                department_permission=int(DEPARTMENT.TEACHER), 
                scheme_of_work_permission=int(SCHEMEOFWORK.EDITOR), 
                lesson_permission=int(LESSON.EDITOR),
                ctx=fake_ctx_model()
            ), 
            TeacherPermissionModel(
                teacher_id=3, 
                teacher_name="Miss Doe", #DepartmentModel(15, "Computer Science")), 
                scheme_of_work=MagicMock(id = 69, name="Games design"), 
                published=1,
                department_permission=int(DEPARTMENT.STUDENT), 
                scheme_of_work_permission=int(SCHEMEOFWORK.VIEWER), 
                lesson_permission=int(LESSON.VIEWER),
                ctx=fake_ctx_model()
            )
        ]

        with patch.object(TeacherPermissionModel, "get_team_permissions", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            fake_request = Mock()
            
            # act
            viewmodel = ViewModel(db=db, request=fake_request, auth_user=6079)
            actual_result = viewmodel.view()
            
            # assert

            TeacherPermissionModel.get_team_permissions.assert_called()
            
            self.assertEqual(3, len(actual_result.content["content"]["data"]["my_team_permissions"]))              
