from unittest import skip
from datetime import datetime
from unittest import TestCase
from shared.models.core.context import Ctx

class test_core_context_ctx_constructor(TestCase):

    test = None
    created_now = datetime.now()

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # act
        test = Ctx(1276711, 67)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)


    def test_constructor_with_scheme_of_work_id___as_param(self):

        # act
        test = Ctx(1276711, 67, scheme_of_work_id=11, auth_user_id=6079)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(11, test.scheme_of_work_id)


    def test_constructor_with_auth_user_id___as_param(self):

        # act
        test = Ctx(1276711, 67, auth_user_id=6079)

        # assert
        self.assertEqual(1276711, test.institute_id)
        self.assertEqual(67, test.department_id)
        self.assertEqual(6079, test.auth_user_id)