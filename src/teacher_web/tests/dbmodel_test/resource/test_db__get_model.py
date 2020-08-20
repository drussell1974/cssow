from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_resource import ResourceModel, handle_log_info

# test context

get_model = ResourceModel.get_model

class test_db__get_model(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_model(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = get_model(self.fake_db, 99, lesson_id=34, scheme_of_work_id=874, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_resource__get'
                , (99, 6079)
                , []
                , handle_log_info)

            self.assertIsNone(actual_results)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        """expected_result = [(
            321,"Understanding numbering systems",1,5,"Computer Science",
            2,"Denary",3,"Data representation",38,11,"Understand common numbering systems","2020-07-16 01:04:59",
            1,"test_user",0,"Denary,Binary,Hexadecimal",4,"learning_objectives",23,343
        )]"""
        expected_result = [(
            321,
            "Understanding numbering systems",
            "Craig and Dave",
            10,
            "Markdown",
            "fa-book",
            "how_to_add_in_binary.md",
            "How to add in binary",
            "",
            76,
            "2020-06-21 08:10:58",
            99,
            "test_user",
            1
        )]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 321, lesson_id=34, scheme_of_work_id=874, auth_user=6079)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson_resource__get"
                , (321, 6079)
                , []
                , handle_log_info)
            

            self.assertEqual(321, actual_results.id)
            self.assertEqual("Understanding numbering systems", actual_results.title)
            self.assertEqual("Craig and Dave", actual_results.publisher)
            self.assertEqual("Markdown", actual_results.type_name)
            self.assertEqual("fa-book", actual_results.type_icon)
            self.assertTrue(actual_results.is_from_db)




