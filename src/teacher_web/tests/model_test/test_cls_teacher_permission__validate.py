from unittest import TestCase
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON


class test_cls_teacher_permission_validate__department_permission(TestCase):

    test = None

    def setUp(self):
        self.test = Model(teacher_id=2, teacher_name="", scheme_of_work=SchemeOfWorkModel(11))

    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.department_permission = DEPARTMENT.NONE

        # test
        self.test.validate()

        # assert
        self.assertFalse("department_permission" in self.test.validation_errors, "department_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid)


    def test_min__invalid_extreme(self):
        # set up

        self.test.department_permission = DEPARTMENT.NONE - 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("department_permission" in self.test.validation_errors, "department_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.department_permission = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("department_permission" in self.test.validation_errors, "department_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_min__invalid_its_just_not_in_the_list(self):
        # set up

        self.test.department_permission = DEPARTMENT.TEACHER + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("department_permission" in self.test.validation_errors, "department_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__valid_mid_range(self):
        # set up

        self.test.department_permission = DEPARTMENT.TEACHER

        # test
        self.test.validate()

        # s
        self.assertFalse("department_permission" in self.test.validation_errors, "department_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid)


    def test_max__valid_extreme(self):
        # set up

        self.test.department_permission = DEPARTMENT.ADMIN

        # test
        self.test.validate()

        # assert
        self.assertFalse("department_permission" in self.test.validation_errors, "department_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.department_permission = DEPARTMENT.ADMIN + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("department_permission" in self.test.validation_errors, "department_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_teacher_permission_validate__scheme_of_work_permission(TestCase):

    test = None

    def setUp(self):
        self.test = Model(teacher_id=2, teacher_name="", scheme_of_work=SchemeOfWorkModel(11))

    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.scheme_of_work_permission = SCHEMEOFWORK.NONE

        # test
        self.test.validate()

        # assert
        self.assertFalse("scheme_of_work_permission" in self.test.validation_errors, "scheme_of_work_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid)


    def test_min__invalid_extreme(self):
        # set up

        self.test.scheme_of_work_permission = SCHEMEOFWORK.NONE - 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("scheme_of_work_permission" in self.test.validation_errors, "scheme_of_work_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")



    def test_min__invalid_its_just_not_in_the_list(self):
        # set up

        self.test.scheme_of_work_permission = SCHEMEOFWORK.VIEWER + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("scheme_of_work_permission" in self.test.validation_errors, "scheme_of_work_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__valid_mid_range(self):
        # set up

        self.test.scheme_of_work_permission = SCHEMEOFWORK.EDITOR

        # test
        self.test.validate()

        # assert
        self.assertFalse("scheme_of_work_permission" in self.test.validation_errors, "scheme_of_work_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid)


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.scheme_of_work_permission = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("scheme_of_work_permission" in self.test.validation_errors, "scheme_of_work_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")



    def test_max__valid_extreme(self):
        # set up

        self.test.scheme_of_work_permission = SCHEMEOFWORK.OWNER

        # test
        self.test.validate()

        # assert
        self.assertFalse("scheme_of_work_permission" in self.test.validation_errors, "scheme_of_work_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.scheme_of_work_permission = SCHEMEOFWORK.OWNER + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("scheme_of_work_permission" in self.test.validation_errors, "scheme_of_work_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_teacher_permission_validate__lesson_permission(TestCase):

    test = None

    def setUp(self):
        self.test = Model(teacher_id=2, teacher_name="", scheme_of_work=SchemeOfWorkModel(11))

    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.lesson_permission = LESSON.NONE

        # test
        self.test.validate()

        # assert
        self.assertFalse("lesson_permission" in self.test.validation_errors, "lesson_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid)


    def test_min__invalid_extreme(self):
        # set up

        self.test.lesson_permission = LESSON.NONE - 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("lesson_permission" in self.test.validation_errors, "lesson_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.lesson_permission = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("lesson_permission" in self.test.validation_errors, "lesson_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_min__invalid_its_just_not_in_the_list(self):
        # set up

        self.test.lesson_permission = LESSON.VIEWER + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("lesson_permission" in self.test.validation_errors, "lesson_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__valid_mid_range(self):
        # set up

        self.test.lesson_permission = LESSON.VIEWER

        # test
        self.test.validate()

        # s
        self.assertFalse("lesson_permission" in self.test.validation_errors, "lesson_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid)


    def test_max__valid_extreme(self):
        # set up

        self.test.lesson_permission = LESSON.OWNER

        # test
        self.test.validate()

        # assert
        self.assertFalse("lesson_permission" in self.test.validation_errors, "lesson_permission should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.lesson_permission = LESSON.OWNER + 1

        # test
        self.test.validate()

        # assert
        self.assertTrue("lesson_permission" in self.test.validation_errors, "lesson_permission should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")

