from django.http import Http404
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel


def on_not_found(self, model, *identifers):
    str_msg = "The item is currently unavailable or you do not have permission."
    raise Http404(str_msg)
