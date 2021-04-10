from unittest import skip
from unittest.mock import MagicMock, Mock,patch
from datetime import datetime
from unittest import TestCase
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_institute import InstituteContextModel
from shared.models.core.context import AuthCtx

@patch.object(InstituteContextModel, "get_context_model", return_value = InstituteContextModel(127671276711, name="Lorum Ipsum"))
@patch.object(DepartmentContextModel, "get_context_model", return_value = DepartmentContextModel(67, name="Computer Science", is_from_db=True))
class test_core_context_authctx_constructor(TestCase):

    test = None
    created_now = datetime.now()

    def setUp(self):

        self.mock_request = MagicMock()
        self.mock_request.user = MagicMock(id=6079)
        self.mock_request.session = {
            "academic_year.start_date": datetime(year=2020, month=9, day=1),
            "academic_year.end_date": datetime(year=2021, month=7, day=15)
        }

        self.mock_db = Mock()
        self.mock_db.cursor = MagicMock()
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self, mock_institute, mock_department):

        # act
        test = AuthCtx(self.mock_db, self.mock_request, 1276711, 67)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(6079, test.auth_user_id)
        #self.assertIsNotNone(test.academic_year.start)
        #self.assertIsNotNone(test.academic_year.end)


    def test_constructor_with_scheme_of_work_id___as_param(self, mock_institute, mock_department):

        # act
        test = AuthCtx(self.mock_db, self.mock_request, 1276711, 67, scheme_of_work_id=11)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(11, test.scheme_of_work_id)
        

    def test_constructor_with_scheme_of_work_id___as_kwargs(self, mock_institute, mock_department):
        # arrange

        fake_kw_args = {"scheme_of_work_id":13}

        # act
        test = AuthCtx(self.mock_db, self.mock_request, 1276711, 67, **fake_kw_args)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(13, test.scheme_of_work_id)


    def test_constructor_with_multiple_args(self, mock_institute, mock_department):
        # arrange

        fake_kw_args = {"scheme_of_work_id":13, "institute_id":1276711, "department_id":67, "auth_user_id":6078 }

        # act
        test = AuthCtx(self.mock_db, self.mock_request, **fake_kw_args)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(13, test.scheme_of_work_id)
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(6079, test.auth_user_id)
