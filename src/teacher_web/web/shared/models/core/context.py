from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel

class Ctx:
    
    def __init__(self, institute_id, department_id, **view_params):
        self.institute_id = institute_id
        self.department_id = department_id
        self.scheme_of_work_id = view_params.get("scheme_of_work_id",0)
        

class AuthCtx(Ctx):
    
    def __init__(self, db, request, institute_id, department_id, **view_params):
        super().__init__(institute_id=institute_id, department_id=department_id, **view_params)
        
        self.request = request
        self.auth_user_id = request.user.id

        if request.user.id is not None:
            self.user_name = request.user.first_name

        self.institute_name = self.session_cache(db, "institute_name", InstituteModel.get_context_name, self.institute_id, self.auth_user_id)
        self.department_name = self.session_cache(db, "department_name", DepartmentModel.get_context_name, self.institute_id, self.department_id, self.auth_user_id)


    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}"


    def session_cache(self, db, name, scalar_fnc, *lookup_args):
        
        key = str((name, lookup_args)) # create unique key from name and lookup_id
        
        #if key not in self.request.session:
        self.request.session[key] = scalar_fnc(db, *lookup_args)
        return self.request.session[key]