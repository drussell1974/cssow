from datetime import datetime
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
            self.test = fake_lesson_schedule(id=0, title="", start_date="2021-06-09T17:20", class_name="", class_code="", lesson_id=12, scheme_of_work_id=34, auth_ctx=mock_auth_user)

            # assert
            self.assertEqual(0, self.test.id)
            self.assertEqual("", self.test.title)
            self.assertEqual("", self.test.class_name)
            self.assertEqual("", self.test.class_code)
            self.assertEqual("2021-06-09T17:20", self.test.start_date)
            self.assertEqual("2021-06-09", self.test.start_date_ui_date)
            self.assertEqual("17:20", self.test.start_date_ui_time)
            self.assertEqual("", self.test.whiteboard_url)
            self.assertEqual("", self.test.edit_url)
            self.assertEqual(12, self.test.lesson_id)
            self.assertEqual(34, self.test.scheme_of_work_id)
            self.assertEqual(mock_auth_user.department_id, self.test.department_id)
            self.assertEqual(mock_auth_user.institute_id, self.test.institute_id)
            self.assertFalse(self.test.is_valid)
            self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        def fake_resolve_schedule_urls(sch):
            return {
                "lesson_schedule.whiteboard_view":f"http://localhost/.../schemesofwork/{sch.scheme_of_work_id}/lessons/{sch.lesson_id}/whiteboard", 
                "lesson_schedule.edit":f"http://localhost/.../schemesofwork/{sch.scheme_of_work_id}/lessons/{sch.lesson_id}/edit"
            }

        # arrange

        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:            
            self.test = fake_lesson_schedule(id=0, title="Vivamus at porta orci", start_date=datetime(year=2021, month=6, day=9, hour=17, minute=20, second=30), class_name="7x", class_code="ABCDEF", lesson_id=12, scheme_of_work_id=34, auth_ctx=mock_auth_user, fn_resolve_url=fake_resolve_schedule_urls)

            self.maxDiff = None
            # assert
            self.assertEqual(0, self.test.id)
            self.assertEqual("ABCDEF", self.test.class_code)
            self.assertEqual("Vivamus at porta orci", self.test.title)
            self.assertEqual("7x", self.test.class_name)
            self.assertEqual(datetime(2021, 6, 9, 17, 20, 30), self.test.start_date)
            self.assertEqual("2021-06-09", self.test.start_date_ui_date)
            self.assertEqual("17:20", self.test.start_date_ui_time)
            self.assertEqual("http://localhost/.../schemesofwork/34/lessons/12/whiteboard", self.test.whiteboard_url)
            self.assertEqual("http://localhost/.../schemesofwork/34/lessons/12/edit", self.test.edit_url)
            self.assertEqual(12, self.test.lesson_id)
            self.assertEqual(34, self.test.scheme_of_work_id)
            self.assertEqual(mock_auth_user.department_id, self.test.department_id)
            self.assertEqual(mock_auth_user.institute_id, self.test.institute_id)
            self.assertFalse(self.test.is_valid)
            self.assertTrue(self.test.is_new())