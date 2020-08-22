from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_schemeofwork import SchemeOfWorkModel

get_schemeofwork_name_only = SchemeOfWorkModel.get_schemeofwork_name_only


class test_db__get_schemeofwork_name_only(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_schemeofwork_name_only(self.fake_db, 101)


    def test__should_call__select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = get_schemeofwork_name_only(self.fake_db, 101, 99)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_schemeofwork_name_only"
                , (101, 99)
                , [])

            self.assertEqual("", actual_result)


    def test__should_call__select__return_single_item(self):
        # arrange
        expected_result = [("ipsum dolor sit amet.",)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_result = get_schemeofwork_name_only(self.fake_db, 6, 99)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_schemeofwork_name_only"
                , (6, 99)
                , [])
            self.assertEqual("ipsum dolor sit amet.", actual_result)



