class Ctx:
    
    def __init__(self, institute_id, department_id, scheme_of_work_id):
        self.institute_id = institute_id
        self.department_id = department_id
        self.scheme_of_work_id = scheme_of_work_id
    

    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}, scheme_of_work_id={self.scheme_of_work_id}"
