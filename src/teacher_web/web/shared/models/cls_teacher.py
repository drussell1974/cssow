from django.db import models
from django.contrib.auth.models import User
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.basemodel import BaseModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE


class TeacherModel(BaseModel):

    def __init__(self, id, name, department, is_authorised=False, created=None, created_by_id=None, created_by_name=None, published=1, is_from_db=False, ctx=None):
        
        TeacherModel.depreciation_notice("use TeacherPermissionModel")

        super().__init__(id, name, created=None, created_by_id=None, created_by_name=None, published=1, is_from_db=is_from_db, ctx=ctx)
        self.id = id
        self.name = name
        self.department = department

        
    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate name
        self._validate_required_string("name", self.name, 1, 70)

        self.on_after_validate()


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)


    def get_name(self):
        return self.name


    @staticmethod
    def get_model(db, teacher_id, ctx):
        model = TeacherModel(0, "", department=DepartmentModel(0, "", institute=InstituteModel(0, "", is_from_db=False), is_from_db=False), is_authorised=False, is_from_db=False)
        
        rows = TeacherDataAccess.get_model(db, teacher_id, ctx.department_id, ctx.institute_id)
        
        for row in rows:
            model = TeacherModel(row[0], row[1], department=DepartmentModel(row[2], row[3], institute=InstituteModel(row[4], name=row[5], is_from_db=False), is_from_db=True), is_authorised=row[6], is_from_db=True)
        return model

class TeacherDataAccess:

    @staticmethod
    def get_model(db, teacher_id, department_id, institute_id):
        execHelper = ExecHelper()

        str_select = "teacher__get"
        params = (teacher_id, department_id, institute_id)
        
        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows
            
        except Exception as e:
            raise Exception("Error getting teacher model", e)


'''
    @staticmethod
    def save(db, model, teacher_id, auth_user):
        """ save model """
        if model.published == STATE.DELETE
            data = DepartmentDataAccess._delete(db, model, auth_user)
        elif model.is_valid == True:
            if model.is_new():
                data = TeacherDataAccess._insert(db, model, teacher_id, auth_user)
                model.id = data[0]
            else:
                data = TeacherDataAccess._update(db, model, teacher_id, auth_user)

        return model
'''