from unittest import TestCase
from unittest.mock import patch
from shared.models.cls_lesson_schedule import LessonScheduleModel
from tests.test_helpers.mocks import fake_ctx_model, fake_lesson_schedule

class test_cls_lesson_schedule__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrange
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:    
            self.test = fake_lesson_schedule(id=0, title="", start_date=None, class_name="", class_code="", lesson_id=12, scheme_of_work_id=34, auth_ctx=mock_auth_user)

            # assert
            self.assertEqual(0, self.test.id)
            self.assertEqual("", self.test.title)
            self.assertEqual("", self.test.class_name)
            self.assertEqual("", self.test.class_code)
            self.assertEqual(12, self.test.lesson_id)
            self.assertEqual(34, self.test.scheme_of_work_id)
            self.assertEqual(mock_auth_user.department_id, self.test.department_id)
            self.assertEqual(mock_auth_user.institute_id, self.test.institute_id)
            self.assertFalse(self.test.is_valid)
            self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):


        # arrange

        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:            
            self.test = fake_lesson_schedule(id=0, title="Vivamus at porta orci", start_date=None, class_name="7x", class_code="ABCDEF", lesson_id=12, scheme_of_work_id=34, auth_ctx=mock_auth_user)

            # assert
            self.assertEqual(0, self.test.id)
            self.assertEqual("ABCDEF", self.test.class_code)
            self.assertEqual("Vivamus at porta orci", self.test.title)
            self.assertEqual("7x", self.test.class_name)
            self.assertEqual(12, self.test.lesson_id)
            self.assertEqual(34, self.test.scheme_of_work_id)
            self.assertEqual(mock_auth_user.department_id, self.test.department_id)
            self.assertEqual(mock_auth_user.institute_id, self.test.institute_id)
            self.assertFalse(self.test.is_valid)
            self.assertTrue(self.test.is_new())