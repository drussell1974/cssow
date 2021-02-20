from unittest import skip
from unittest.mock import MagicMock, Mock
from datetime import datetime
from unittest import TestCase
from shared.models.core.context import AuthCtx

class test_core_context_authctx_constructor(TestCase):

    test = None
    created_now = datetime.now()

    def setUp(self):

        self.mock_request = MagicMock()
        self.mock_request.user = MagicMock(id=6079)
        self.mock_request.session = {}


        self.mock_db = Mock()
        self.mock_db.cursor = MagicMock()
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # act
        test = AuthCtx(self.mock_db, self.mock_request, 1276711, 67)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(6079, test.auth_user_id)


    def test_constructor_with_scheme_of_work_id___as_param(self):

        # act
        test = AuthCtx(self.mock_db, self.mock_request, 1276711, 67, scheme_of_work_id=11)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(11, test.scheme_of_work_id)

        

    def test_constructor_with_scheme_of_work_id___as_kwargs(self):
        # arrange

        fake_kw_args = {"scheme_of_work_id":13}

        # act
        test = AuthCtx(self.mock_db, self.mock_request, 1276711, 67, **fake_kw_args)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(13, test.scheme_of_work_id)


        

    def test_constructor_with_multiple_args(self):
        # arrange

        fake_kw_args = {"scheme_of_work_id":13, "institute_id":1276711, "department_id":67 }

        # act
        test = AuthCtx(self.mock_db, self.mock_request, **fake_kw_args)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(13, test.scheme_of_work_id)
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)