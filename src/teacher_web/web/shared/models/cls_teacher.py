from django.db import models
from django.contrib.auth.models import User
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.basemodel import BaseModel
from shared.models.cls_department import DepartmentModel

class TeacherModel(BaseModel):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, null=True)

    def __init__(self, id, name, department, is_authorised=False, created=None, created_by_id=None, created_by_name=None, published=1, is_from_db=False):
        super().__init__(id, name, created=None, created_by_id=None, created_by_name=None, published=1, is_from_db=is_from_db)
        self.id = id
        self.name = name
        self.department = department
        self.is_authorised = is_authorised


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
    def get_model(db, teacher_id, department_id, institute_id = 0):
        model = TeacherModel(0, "", department=DepartmentModel(0, "", is_from_db=False), is_authorised=False, is_from_db=False)
        
        rows = TeacherDataAccess.get_model(db, teacher_id, department_id, institute_id)
        
        for row in rows:
            model = TeacherModel(row[0], row[1], department=DepartmentModel(row[2], row[3], is_from_db=True), is_authorised=row[4], is_from_db=True)
        return model

class TeacherDataAccess:

    @staticmethod
    def get_model(db, teacher_id, department_id = 0, institute_id = 0):
        execHelper = ExecHelper()

        str_select = "teacher__get"
        params = (teacher_id, department_id, institute_id)

        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows
            
        except Exception as e:
            raise Exception("Error getting departments", e)


'''
    @staticmethod
    def save(db, model, teacher_id, auth_user):
        """ save model """
        if model.published == 2:
            data = DepartmentDataAccess._delete(db, model, auth_user)
        elif model.is_valid == True:
            if model.is_new():
                data = TeacherDataAccess._insert(db, model, teacher_id, auth_user)
                model.id = data[0]
            else:
                data = TeacherDataAccess._update(db, model, teacher_id, auth_user)

        return model
'''