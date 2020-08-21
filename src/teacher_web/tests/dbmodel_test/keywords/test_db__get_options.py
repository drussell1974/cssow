from shared.models.cls_keyword import KeywordModel
from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper


class test_db_keyword__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        KeywordModel.handle_log_info = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                KeywordModel.get_options(self.fake_db)


    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeywordModel.get_options(self.fake_db, 6079)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_options'
                , (6079,)
                , [])
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self):
        # arrange
        expected_result = [(123, "Binary", "Donec porta efficitur metus, eget consequat ligula maximus eget. Nunc imperdiet sapien sit amet arcu fermentum maximus.")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeywordModel.get_options(self.fake_db, 6079)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_options'
                , (6079,)
                , [])
            self.assertEqual(1, len(rows))
            self.assertEqual("Binary", rows[0].term)


    def test__should_call_select__return_multiple_item(self):
        # arrange
        expected_result = [
            (1, "Binary", "Phasellus vitae pretium neque, ut mattis mi.")
            ,(2,"Decimal", "Donec porta efficitur metus, eget consequat ligula maximus eget. Nunc imperdiet sapien sit amet arcu fermentum maximus.")
            ,(3, "Hexadecimal", "Phasellus mauris lacus, accumsan non viverra non, sagittis nec lorem. Vestibulum tristique laoreet nisi non congue.")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeywordModel.get_options(self.fake_db, 6079)
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_options'
                , (6079,)
                , [])
            self.assertEqual(3, len(rows))

            self.assertEqual("Binary", rows[0].term)
            self.assertEqual("Hexadecimal", rows[2].term)
