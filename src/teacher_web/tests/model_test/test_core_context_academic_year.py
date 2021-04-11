from unittest import skip
from unittest.mock import MagicMock, Mock,patch
from datetime import datetime
from unittest import TestCase
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_institute import InstituteContextModel
from shared.models.core.context import AcademicYearCtx


@skip("needs implementing")
class test_core_context_academic_year(TestCase):

    def setUp(self):
        self.mock_request = Mock()
        self.mock_request.session = {
            "academic_year.start_date": datetime(year=2020, month=9, day=1),
            "academic_year.end_date": datetime(year=2021, month=7, day=15),
            "academic_year.periods": { 1: "09:00", 2:"10:00 "}
        }

    def tearDown(self):
        pass


    def test_academic_year__default(self):

        # act
        test = AcademicYearCtx(self.mock_request)

        self.assertEqual(datetime(2020, 9, 1), test.start_date)
        self.assertEqual(datetime(2021, 7, 15), test.end_date)
