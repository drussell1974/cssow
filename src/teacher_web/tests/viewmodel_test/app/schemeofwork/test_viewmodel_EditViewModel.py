from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.schemesofwork.viewmodels import SchemeOfWorkEditViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from tests.test_helpers.mocks import fake_ctx_model

class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    
    def test_execute_called_save__add_model_to_data(self):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Proin id massa metus. Aliqua tincidunt.",
                    "description": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur",
                    "exam_board_id": 56,
                    "institute_id": 49,
                    "department_id": 68,
                    "lesson_id": 230,
                    "key_stage_id": 2,
                    "study_duration": 1
                }

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        on_save__scheme_of_work_data_to_return = Model(99, name="Proin id massa metus. Aliqua tincidunt.", study_duration=2, start_study_in_year=10)
        
        with patch.object(Model, "save", return_value=on_save__scheme_of_work_data_to_return):

            # act

            test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=fake_ctx_model())
            test_context.model.key_words.clear()
            
            # assert 
            self.assertEqual(0, test_context.model.key_stage_id)
                    
            self.assertEqual("", test_context.error_message)
            self.assertTrue(test_context.saved)
            
            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.name)
            self.assertEqual([], test_context.model.key_words)


    
    def test_execute_called_save__add_model_to_data__with_keywords(self):
        
        # arrange
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Proin id massa metus. Aliqua tinciduntx.",
                    "description": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur",
                    "exam_board_id": 56,
                    "lesson_id": 230,
                    "key_stage_id": 2,
                    "study_duration": 1
                }


        on_save__scheme_of_work_data_to_return = Model(99, name="Proin id massa metus. Aliqua tinciduntx.", study_duration=2, start_study_in_year=10, auth_user=fake_ctx_model())
        
        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=on_save__scheme_of_work_data_to_return):


                return_keyword_model = KeywordModel(123, "RAM")
                return_keyword_model.is_valid = True

                # act
                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                mock_db = MagicMock()
                mock_db.cursor = MagicMock()

                test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=fake_ctx_model())
                
                # assert 
                self.assertEqual(0, test_context.model.key_stage_id)
                
                self.assertEqual("", test_context.error_message)
                self.assertEqual({}, test_context.model.validation_errors)

                Model.save.assert_called()

                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Proin id massa metus. Aliqua tinciduntx.", test_context.model.name)


    
    def test_execute_called_save__add_model_to_data__return_invalid(self):
         
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Suspendisse nisi dui, lobortis ut",
                    "description": "unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.",
                    "exam_board_id": 0,
                    "lesson_id": 0,
                    "department_id": 56,
                    "institute_id": 49,
                    "key_stage_id": 2,
                    "study_duration": 1
                }

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=None):
                    
                # act
                
                return_keyword_model = KeywordModel(4, term="Four")
                return_keyword_model.is_valid = True

                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                mock_db = MagicMock()
                mock_db.cursor = MagicMock()

                test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=fake_ctx_model())

                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertEqual("validation errors {'exam_board_id': '0 is not a valid range'}", test_context.alert_message)
                self.assertFalse(test_context.saved)

                Model.save.assert_not_called()

                # return the invalid objectwith patch.object(Model, "save", return_value=None):
                    
                # act
                
                return_keyword_model = KeywordModel(4, term="Four")
                return_keyword_model.is_valid = True

                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                mock_db = MagicMock()
                mock_db.cursor = MagicMock()

                test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=fake_ctx_model())

                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertEqual("validation errors {'exam_board_id': '0 is not a valid range'}", test_context.alert_message)
                self.assertFalse(test_context.saved)

                Model.save.assert_not_called()

                # return the invalid object
                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Suspendisse nisi dui, lobortis ut", test_context.model.name)
                self.assertEqual(2, test_context.model.key_stage_id)
                self.assertFalse(test_context.model.is_valid)
                self.assertEqual(1, len(test_context.model.validation_errors)) 
                self.assertEqual({'exam_board_id': '0 is not a valid range'}, test_context.model.validation_errors) 

                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Suspendisse nisi dui, lobortis ut", test_context.model.name)
                self.assertEqual(2, test_context.model.key_stage_id)
                self.assertFalse(test_context.model.is_valid)
                self.assertEqual(1, len(test_context.model.validation_errors)) 
                self.assertEqual({'exam_board_id': '0 is not a valid range'}, test_context.model.validation_errors) 


    def test_execute_called_save__add_model_to_data__invalid_study_duration(self):
         
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Suspendisse nisi dui, lobortis ut",
                    "description": "unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.",
                    "exam_board_id": 2,
                    "lesson_id": 0,
                    "department_id": 56,
                    "institute_id": 49,
                    "key_stage_id": 2,
                    "study_duration": 0 # invalid study
                }

        
        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=None):
                    
                # act
                
                return_keyword_model = KeywordModel(4, term="Four")
                return_keyword_model.is_valid = True

                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                mock_db = MagicMock()
                mock_db.cursor = MagicMock()

                test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=fake_ctx_model())

                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertEqual("validation errors {'study_duration': '0 is not a valid range'}", test_context.alert_message)
                self.assertFalse(test_context.saved)

                Model.save.assert_not_called()

                # return the invalid object
                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Suspendisse nisi dui, lobortis ut", test_context.model.name)
                self.assertEqual(2, test_context.model.key_stage_id)
                self.assertFalse(test_context.model.is_valid)
                self.assertEqual(1, len(test_context.model.validation_errors)) 
                self.assertEqual({'study_duration': '0 is not a valid range'}, test_context.model.validation_errors) 
