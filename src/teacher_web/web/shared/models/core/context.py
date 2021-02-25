from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.enums.publlished import STATE

class Ctx:
    
    def __init__(self, institute_id, department_id, **view_params):
        self.institute_id = institute_id
        self.department_id = department_id
        self.scheme_of_work_id = view_params.get("scheme_of_work_id",0)
        self.auth_user_id = view_params.get("auth_user_id",0)
        # public member
        self.can_view = STATE.PUBLISH


class AuthCtx(Ctx):
    
    def __init__(self, db, request, institute_id, department_id, **view_params):
        super().__init__(institute_id=institute_id, department_id=department_id, **view_params)
        
        self.request = request
        self.auth_user_id = request.user.id

        if request.user.id is not None:
            self.user_name = request.user.first_name
            # logged in member can view internal and public published
            self.can_view = STATE.PUBLISH_INTERNAL
        
        # NOTE: get department then institute to promote can_view

        self.department = self.session_cache(db, "department", DepartmentContextModel.get_context_model, self.institute_id, self.department_id, self.auth_user_id)
        # TODO: #329 check ownership and set can_view
        # TODO: #329 fix dictionary error when getting properties
        #if self.department.created_by_id == self.auth_user_id:
            # can view draft
        #    self.can_view = STATE.DRAFT

        self.institute = self.session_cache(db, "institute", InstituteContextModel.get_context_model, self.institute_id, self.auth_user_id)
        # TODO: #329 check ownership and set can_view
        # TODO: #329 fix dictionary error when getting properties
        #if self.institute.created_by_id == self.auth_user_id:
            # can view everything
        #    self.can_view = STATE.DELETE


    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}"


    def session_cache(self, db, name, fnc, *lookup_args):
        
        key = str((name, lookup_args)) # create unique key from name and lookup_id
        
        # TODO: ensure value is stored in cache to prevent calling scalar_fnc each time

        #if key not in self.request.session:
        self.request.session[key] = fnc(db, *lookup_args).__dict__
        return self.request.session[key]

        