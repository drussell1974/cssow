class Ctx:
    
    def __init__(self, **view_params):
        self.institute_id = view_params.get("institute_id", 0)
        self.department_id = view_params.get("department_id", 0)
        self.scheme_of_work_id = view_params.get("scheme_of_work_id",0 )
    

    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}, scheme_of_work_id={self.scheme_of_work_id}"
