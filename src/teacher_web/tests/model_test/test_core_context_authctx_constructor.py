from unittest import skip
from unittest.mock import MagicMock, Mock,patch
from datetime import datetime
from unittest import TestCase
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_institute import InstituteContextModel
from shared.models.core.context import AuthCtx
from tests.test_helpers.mocks import *

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

    @patch.object(AcademicYearModel, "get_model", return_value = fake_academic_year())
    @patch.object(AcademicYearModel, "get_all", return_value = fake_academic_years())
    @patch.object(AcademicYearPeriodModel, "get_all", return_value = fake_academic_year_periods())
    def test_constructor_default(self, mock_institute, mock_department, mock_AYear, mock_AYears, mock_AYearPeriods):

        # actd
        test = AuthCtx(self.mock_db, self.mock_request, 1276711, 67)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(6079, test.auth_user_id)
        self.assertEqual('2020-09-01T00:00', test.academic_year.start)
        self.assertEqual('2021-07-30T00:00', test.academic_year.end)


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


    @patch.object(AcademicYearModel, "get_model", return_value = None)
    @patch.object(AcademicYearModel, "get_all", return_value = [])
    @patch.object(AcademicYearPeriodModel, "get_all", return_value = [])
    def test_constructor_with_multiple_args___when_academic_year_does_not_exist(self, mock_institute, mock_department, mock_AYear, mock_AYears, mock_AYearPeriods):
        # arrange

        fake_kw_args = {"scheme_of_work_id":0, "institute_id":1276711, "department_id":0, "auth_user_id":6078 }

        # act
        test = AuthCtx(self.mock_db, self.mock_request, **fake_kw_args)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(0, test.scheme_of_work_id)
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(0, test.department_id)
        self.assertEqual(6079, test.auth_user_id)
        self.assertEqual(2021, test.selected_year) # current year
        self.assertEqual('2020-09-01T00:00', test.academic_year.start)
        self.assertEqual('2021-07-30T00:00', test.academic_year.end)


    @patch.object(AcademicYearModel, "get_model", return_value = fake_academic_year(year=1802))
    @patch.object(AcademicYearModel, "get_all", return_value = [fake_academic_year(year=1801),fake_academic_year(year=1802),fake_academic_year(year=1803)])
    @patch.object(AcademicYearPeriodModel, "get_all", return_value = [])
    def test_constructor_with_multiple_args___when_academic_year_in_the_past(self, mock_institute, mock_department, mock_AYear, mock_AYears, mock_AYearPeriods):
        # arrange

        fake_kw_args = {"scheme_of_work_id":0, "institute_id":1276711, "department_id":0, "auth_user_id":6078 }

        # act
        test = AuthCtx(self.mock_db, self.mock_request, **fake_kw_args)

        # assert
        self.assertEqual(1802, test.selected_year)
        self.assertEqual('1801-09-01T00:00', test.academic_year.start)
        self.assertEqual('1802-07-30T00:00', test.academic_year.end)


    @patch.object(AcademicYearModel, "get_model", return_value = None)
    @patch.object(AcademicYearModel, "get_all", return_value = [fake_academic_year(year=2120), fake_academic_year(year=2121)])
    @patch.object(AcademicYearPeriodModel, "get_all", return_value = [])
    def test_constructor_with_multiple_args___when_academic_year_in_the_future(self, mock_institute, mock_department, mock_AYear, mock_AYears, mock_AYearPeriods):
        # arrange

        fake_kw_args = {"scheme_of_work_id":0, "institute_id":1276711, "department_id":0, "auth_user_id":6078 }

        # act
        test = AuthCtx(self.mock_db, self.mock_request, **fake_kw_args)

        # assert
        self.assertEqual(2120, test.selected_year)
        self.assertEqual('2119-09-01T00:00', test.academic_year.start)
        self.assertEqual('2120-07-30T00:00', test.academic_year.end)


    @patch.object(AcademicYearModel, "get_model", return_value = fake_academic_year(year=2017))
    @patch.object(AcademicYearModel, "get_all", return_value = [fake_academic_year(year=1801),fake_academic_year(year=1802),fake_academic_year(year=2103)])
    @patch.object(AcademicYearPeriodModel, "get_all", return_value = [])
    def test_constructor_with_multiple_args___when_always_get_selected_year(self, mock_institute, mock_department, mock_AYear, mock_AYears, mock_AYearPeriods):
        # arrange

        fake_kw_args = {"scheme_of_work_id":0, "institute_id":1276711, "department_id":0, "auth_user_id":6078 }
        
        # get the selected year from get_model

        self.mock_request.session = { "academic_year__selected_id": 2017 }

        # act
        test = AuthCtx(self.mock_db, self.mock_request, **fake_kw_args)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(0, test.scheme_of_work_id)
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(0, test.department_id)
        self.assertEqual(6079, test.auth_user_id)
        self.assertEqual(2017, test.selected_year)
        self.assertEqual('2016-09-01T00:00', test.academic_year.start)
        self.assertEqual('2017-07-30T00:00', test.academic_year.end)
