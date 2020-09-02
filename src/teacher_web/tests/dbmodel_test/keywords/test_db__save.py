from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
import shared.models.cls_keyword as test_context

# create test context

Model = test_context.KeywordModel
save = test_context.KeywordModel.save
handle_log_info = test_context.handle_log_info


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

        model = Model(0, term="", definition="Mauris ac velit ultricies, vestibulum.")
        model.is_new = Mock(return_value=True)

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save(self.fake_db, model, 1, 6079)


    def test_should_call___update___updatewith_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, term="", definition="Mauris ac velit ultricies, vestibulum.")
        model.is_new = Mock(return_value=False)
        
        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                
                save(self.fake_db, model, 1, 6079)


    def test_should_call__update_with__is_new__false(self):
         # arrange

        model = Model(1, term="Lorem Ipsum", definition="Mauris ac velit ultricies, vestibulum.", scheme_of_work_id=13)
        model.is_new = MagicMock(return_value=False)
        model.is_valid = MagicMock(return_value=True)
        model.published = 1

        #test_context._update_lesson_lessonobjectives = Mock()

        expected_result = model.id

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, 1, 6079)
            
            # assert
            
            ExecHelper.update.assert_called_with(self.fake_db, 
                'keyword__update'
                , (1, 'Lorem Ipsum', 'Mauris ac velit ultricies, vestibulum.', 13, 1, 6079)
                ,  handle_log_info)

            self.assertEqual(expected_result, actual_result.id)


    def test_should_call__insert__when__is_new__true(self):
        # arrange

        model = Model(0, term="Mauris", definition="Mauris ac velit ultricies, vestibulum.", scheme_of_work_id=13)
        
        model.is_new = MagicMock(return_value=True)
        model.is_valid = MagicMock(return_value=True)
        
        expected_result = ([], "100")

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = save(self.fake_db, model, 1, 6079)

            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db,
                'keyword__insert'
                , (0, 'Mauris', 'Mauris ac velit ultricies, vestibulum.', 13, 6079, 1)
                , handle_log_info)
                
            self.assertNotEqual(0, actual_result.id)

