from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.basemodel import BaseModel, BaseContextModel
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy

class InstituteContextModel(BaseContextModel):
    
    def __init__(self, id_, name, description="", created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, display_name=name, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=ctx)
        self.id = id_
        self.name = name


    @classmethod
    def empty(cls, published=STATE.PUBLISH, ctx=None):
        model = cls(id_=0, name="", published=published, ctx=ctx)
        return model


    @classmethod
    def get_context_model(cls, db, institute_id, auth_user_id):
        
        def set_attributes(model, row):
            model.id = row[0]
            model.name = row[1]
            #model.parent_id = row[2] # TODO: create @property setter
            model.created_by_id = row[3]
            model.published = row[4]

        empty_model = cls.empty()

        result = BaseContextModel.get_context_model(db, empty_model, set_attributes, "institute__get_context_model",  handle_log_info, institute_id)
        result.institute_id = institute_id
        
        return result if result is not None else None


    @classmethod
    def cached(cls, request, db, institute_id, auth_user_id):
        
        institute = cls.empty()
        
        cache_obj = CacheProxy.session_cache(request, db, "institute", cls.get_context_model, institute_id, auth_user_id)
        
        if cache_obj is not None:
            institute.from_dict(cache_obj)

        return institute

class InstituteModel(InstituteContextModel):

    # default values for api
    name = ""
    description = ""
    number_of_departments = 0
    
    def __init__(self, id_, name, description="", created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, name=name, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=None)
        #self.id = id_
        self.name = name
        self.description = description
        self.number_of_departments = 0
        self.departments = []
        

    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate name
        self._validate_required_string("name", self.name, 1, 70)
        self._validate_optional_string("description", self.description, 5000)

        self.on_after_validate()


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)

        # description
        if self.description is not None:
            self.description = sql_safe(self.description)


    @staticmethod
    def empty():
        model = InstituteModel(0, "")
        return model


    @staticmethod
    def get_all(db, auth_user):
        
        rows = InstituteDataAccess.get_all(db, show_published_state=auth_user.can_view, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows: 
            model = InstituteModel(id_=row[0],
                                    name=row[1],
                                    created=row[2],                                                                                                                                                                                                                         
                                    created_by_id=row[3],
                                    created_by_name=row[4],
                                    published=row[5])
            
            model.number_of_departments = InstituteModel.get_number_of_departments(db, model.id, auth_user)
            
            data.append(model)
        return data


    @staticmethod
    def get_model(db, id, auth_user):   
        rows = InstituteDataAccess.get_model(db, id, auth_user_id=auth_user.auth_user_id)
        # TODO: start as none None
        model = InstituteModel(0, "")
        for row in rows:
            model = InstituteModel(id_=row[0],
                                    name=row[1],
                                    created=row[2],
                                    created_by_id=row[3],
                                    created_by_name=row[4],
                                    published=row[5])

            model.number_of_departments = InstituteModel.get_number_of_departments(db, id, auth_user)

            model.on_fetched_from_db()         
        return model


    @staticmethod
    def get_my(db, auth_user):
        
        rows = InstituteDataAccess.get_my(db, show_published_state=auth_user.can_view, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows: 
            model = InstituteModel(id_=row[0],
                                    name=row[1],
                                    created=row[2],                                                                                                                                                                                                                         
                                    created_by_id=row[3],
                                    created_by_name=row[4],
                                    published=row[5])
            
            model.number_of_departments = InstituteModel.get_number_of_departments(db, model.id, auth_user)
            
            data.append(model)
        return data


    @staticmethod
    def get_options(db, auth_user):
        rows = InstituteDataAccess.get_options(db, auth_user_id=auth_user.auth_user_id)
        data = []
        
        for row in rows:
            model = InstituteModel(row[0], row[1])
            data.append(model)
        return data


    @staticmethod
    def get_number_of_departments(db, institute_id, auth_user):
        result = InstituteDataAccess.get_number_of_departments(db, institute_id, auth_user.auth_user_id)
        return result
        

    @staticmethod
    def save(db, model, teacher_id, auth_user):
        """ save model """
        if model.published == STATE.DELETE:
            data = InstituteDataAccess._delete(db, model, auth_user.auth_user_id)
        elif model.is_valid == True:
            if model.is_new():
                data = InstituteDataAccess._insert(db, model, teacher_id, auth_user_id=auth_user.auth_user_id)
                model.id = data[0]
            else:
                data = InstituteDataAccess._update(db, model, teacher_id, auth_user_id=auth_user.auth_user_id)

        return model


    @staticmethod
    def delete_unpublished(db, auth_user):
        rows = InstituteDataAccess.delete_unpublished(db, auth_user_id=auth_user.auth_user_id)
        return rows


    @staticmethod
    def publish_by_id(db, id, auth_user):
        return InstituteDataAccess.publish(db=db, auth_user_id=auth_user.auth_user_id, id_=id)        


class InstituteDataAccess:
    

    @staticmethod
    def get_model(db, id_, auth_user_id):
        """
        get institution

        :param db: database context
        :param id_: institution identifier
        :param auth_user_id: the user executing the command
        """

        execHelper = ExecHelper()

        select_sql = "institute__get"
        params = (id_, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_all(db, show_published_state, auth_user_id):
        """
        get all inistutions
        """
        
        execHelper = ExecHelper()
        
        select_sql = "institute__get_all" 
        params = (int(show_published_state), auth_user_id,)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_my(db, show_published_state, auth_user_id):
        """
        get my inistutions
        """
        
        execHelper = ExecHelper()
        
        select_sql = "institute__get_my" 
        params = (int(show_published_state), auth_user_id,)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_options(db, auth_user_id):
        
        execHelper = ExecHelper()

        str_select = "institute__get_options"
        params = (auth_user_id,)

        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting institutes", e)

    
    @staticmethod
    def get_number_of_departments(db, institute_id, auth_user_id):
        execHelper = ExecHelper()
        execHelper.begin(db)
        
        select_sql = "institute__get_number_of_departments"
        params = (institute_id, auth_user_id)

        result = []
        result = execHelper.scalar(db, select_sql, result, handle_log_info, params)

        if result is not None and len(result) > 0:
            result = result[0]
        return result


    @staticmethod
    def _insert(db, model, teacher_id, auth_user_id):
        """ inserts the sow_insitute """
        execHelper = ExecHelper()

        sql_insert_statement = "institute__insert"
        params = (
            model.id,
            model.name,
            teacher_id,
            auth_user_id,
            int(model.published)
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, teacher_id, auth_user_id):
        """ updates the sow_institute """
        
        execHelper = ExecHelper()
        
        str_update = "institute__update"
        params = (
            model.id,
            model.name,
            teacher_id,
            int(model.published),
            auth_user_id
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, model, auth_user_id):

        execHelper = ExecHelper()

        sql = "institute__delete"
        params = (model.id, auth_user_id)
    
        #271 Stored procedure
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows


    @staticmethod
    def delete_unpublished(db, auth_user_id):
        """ Delete all unpublished schemes of work """

        execHelper = ExecHelper()
        
        #271 Create StoredProcedure
        str_delete = "institute__delete_unpublished"
        params = (int(STATE.DRAFT),auth_user_id)
            
        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval


    @staticmethod
    def publish(db, auth_user_id, id_):
        
        model = InstituteModel(id_, "")
        model.publish = True

        execHelper = ExecHelper()
        #271 Create StoredProcedure
        str_update = "institute__publish"
        params = (model.id, model.published, auth_user_id)

        rval = []
        rval = execHelper.update(db, str_update, params, handle_log_info)

        return rval