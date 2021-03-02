from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy

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
        
        # NOTE: get department then get institute to promote can_view

        self.department = DepartmentContextModel.cached(request, db, self.institute_id, self.department_id, self.auth_user_id)
        # TODO: #323 check ownership and set can_view

        self.institute = InstituteContextModel.cached(request, db, self.institute_id, self.auth_user_id)        
        # TODO: #323 check ownership and set can_view
        
        if self.scheme_of_work_id > 0:
            self.scheme_of_work = SchemeOfWorkContextModel.cached(request, db, self.scheme_of_work_id, self.auth_user_id)        

    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}"
