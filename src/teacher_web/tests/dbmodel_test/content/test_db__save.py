from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_content import ContentModel as Model, ContentDataAccess, handle_log_info

save = Model.save

class test_db__save(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                save(self.fake_db, model, 99)


    def test_should_call__update_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, "")
    
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                
                save(self.fake_db, model)


    def test_should_call__update_with__is_new__false(self):
         # arrange
        model = Model(1, "CPU and RAM")

        expected_result = model.id

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=6079, published=1)
            
            # assert
            
            ExecHelper.update.assert_called_with(self.fake_db, 
                 'content__update'
                , (1, 'CPU and RAM', '', 0, None, 1, 6079)
                , handle_log_info)

            self.assertEqual(1, actual_result)


    def test_should_call__insert_insert__when__is_new__true(self):
        # arrange

        model = Model(0, description="", key_stage_id=20)

        expected_result = (876,)

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=6079, published = 1)
            
            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db,
                'content__insert'
                , (0, '', '', 20, None, 1, 6079)
                , handle_log_info)
            
            self.assertEqual(876, actual_result[0])


    def test_should_call__delete__when__is_new__false__and__published_is_2(self):
        # arrange

        model = Model(23, "")
        
        expected_result = model.id

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, auth_user=6079, published=2)

            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                "content__delete"
                , (23, None, 6079)
                , handle_log_info)

            # check subsequent functions where called

            self.assertEqual(23, actual_result.id)
            self.assertEqual(2, actual_result.published)