# -*- coding: utf-8 -*-
from django.db import models
from .core.basemodel import BaseModel, BaseDataAccess, try_int
from .core.db_helper import ExecHelper, sql_safe, to_db_null
from shared.models.core.log import handle_log_info


class SchemeOfWorkListModel(models.Model):
    schemesofwork = []
    def __init__(self, data):
        
        # TODO: remove __dict__ . The object should be serialised to json further up the stack
        self.schemesofwork = get_all(None, 11, None).__dict__


class SchemeOfWorkModel(BaseModel):

    name = ""
    description = ""
    
    def __init__(self, id_, name="", description="", exam_board_id=0, exam_board_name="", key_stage_id=0, key_stage_name="", created="", created_by_id=0, created_by_name="", is_recent = False, published = 1, is_from_db=False):
        #231: implement across all classes
        super().__init__(id_, name, created, created_by_id, created_by_name, published, is_from_db)
        self.name = name
        self.description = description
        self.exam_board_id = try_int(exam_board_id)
        self.exam_board_name = exam_board_name
        self.key_stage_id = try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.is_recent = is_recent
        self.url = '/schemeofwork/{}/lessons'.format(self.id)


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # Validate name
        self._validate_required_string("name", self.name, 1, 40)
        # Validate description
        self._validate_required_string("description", self.description, 1, 1500)
        # Validate exam board
        self._validate_optional_integer("exam_board_id", self.exam_board_id, 1, 9999)
        # Validate key stage
        self._validate_required_integer("key_stage_id", self.key_stage_id, 1, 9999)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        if self.name is not None:
            self.name = sql_safe(self.name)

        if self.description is not None:
            self.description = sql_safe(self.description)

        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.exam_board_name is not None:
            self.exam_board_name = sql_safe(self.exam_board_name)

   
    @staticmethod
    def get_all(db, auth_user, key_stage_id=0):
        rows = SchemeOfWorkDataAccess.get_all(db, auth_user, key_stage_id)
        data = []
        for row in rows:
            model = SchemeOfWorkModel(id_=row[0],
                                    name=row[1],
                                    description=row[2],
                                    exam_board_id=row[3],
                                    exam_board_name=row[4],
                                    key_stage_id=row[5],
                                    key_stage_name=row[6],
                                    created=row[7],
                                    created_by_id=row[8],
                                    created_by_name=row[9],
                                    published=row[10])
            model.set_is_recent()
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


    @staticmethod
    def get_model(db, id, auth_user):
        rows = SchemeOfWorkDataAccess.get_model(db, id, auth_user)
        model = SchemeOfWorkModel(0)
        for row in rows:
            model = SchemeOfWorkModel(id_=row[0],
                                    name=row[1],
                                    description=row[2],
                                    exam_board_id=row[3],
                                    exam_board_name=row[4],
                                    key_stage_id=row[5],
                                    key_stage_name=row[6],
                                    created=row[7],
                                    created_by_id=row[8],
                                    created_by_name=row[9],
                                    published=row[10])
            model.on_fetched_from_db()

        return model


    @staticmethod
    def get_options(db, auth_user):
        rows = SchemeOfWorkDataAccess.get_options(db, auth_user)
        data = []

        for row in rows:
            model = SchemeOfWorkModel(id_ = row[0], name = row[1], key_stage_name = row[2])
            data.append(model)

        return data


    @staticmethod
    def get_latest_schemes_of_work(db, top, auth_user):
        rows = SchemeOfWorkDataAccess.get_latest_schemes_of_work(db, top, auth_user)
        data = []
        for row in rows:
            model = SchemeOfWorkModel(id_=row[0],
                                    name=row[1],
                                    description=row[2],
                                    exam_board_id=row[3],
                                    exam_board_name=row[4],
                                    key_stage_id=row[5],
                                    key_stage_name=row[6],
                                    created=row[7],
                                    created_by_id=row[8],
                                    created_by_name=row[9],
                                    published=row[10])
            data.append(model)
        return data


    @staticmethod
    def get_schemeofwork_name_only(db, scheme_of_work_id):
        rows = SchemeOfWorkDataAccess.get_schemeofwork_name_only(db, scheme_of_work_id)
        scheme_of_work_name = ""
        for row in rows:
            scheme_of_work_name = row[0]

        return scheme_of_work_name


    @staticmethod
    def get_key_stage_id_only(db, scheme_of_work_id):
        rows = SchemeOfWorkDataAccess.get_key_stage_id_only(db, scheme_of_work_id)
        key_stage_id = 0
        for row in rows:
            key_stage_id = row[0]
        return key_stage_id


    @staticmethod
    def save(db, model, published=1):
        if try_int(published) == 2:
            model = SchemeOfWorkDataAccess._delete(db, model)
        else:
            if model.is_new() == True:
                model = SchemeOfWorkDataAccess._insert(db, model, published)
            else:
                model = SchemeOfWorkDataAccess._update(db, model, published)

        return model


    @staticmethod
    def delete_unpublished(db, auth_user):
        rows = SchemeOfWorkDataAccess.delete_unpublished(db, auth_user)
        return len(rows)


    @staticmethod
    def publish_by_id(db, id, auth_user):
        return SchemeOfWorkDataAccess.publish(db, auth_user, id)        


class SchemeOfWorkDataAccess:
    
    @staticmethod
    def get_model(db, id_, auth_user):
        execHelper = ExecHelper()

        select_sql = "SELECT "\
                    " sow.id as id, "\
                    " sow.name as name, "\
                    " sow.description as description, "\
                    " sow.exam_board_id as exam_board_id, "\
                    " exam.name as exam_board_name, "\
                    " sow.key_stage_id as key_stage_id, "\
                    " kys.name as key_stage_name, "\
                    " sow.created as created, "\
                    " sow.created_by as created_by_id, "\
                    " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, "\
                    " sow.published as published"\
                    " FROM sow_scheme_of_work as sow "\
                    " LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id "\
                    " INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id "\
                    " INNER JOIN auth_user as user ON user.id = sow.created_by "\
                    "  WHERE sow.id = {scheme_of_work_id} AND (sow.published = 1 OR sow.created_by = {auth_user});"

        select_sql = select_sql.format(scheme_of_work_id=id_, auth_user=to_db_null(auth_user))

        rows = []
        rows = execHelper.execSql(db, select_sql, rows)
        return rows


    @staticmethod
    def get_all(db, auth_user, key_stage_id=0):

        execHelper = ExecHelper()

        select_sql = "SELECT "\
                    "  sow.id as id, "\
                    "  sow.name as name, "\
                    "  sow.description as description, "\
                    "  sow.exam_board_id as exam_board_id, "\
                    "  exam.name as exam_board_name, "\
                    "  sow.key_stage_id as key_stage_id, "\
                    "  kys.name as key_stage_name, "\
                    "  sow.created as created, "\
                    "  sow.created_by as created_by_id,"\
                    "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, "\
                    "  sow.published as published"\
                    " FROM sow_scheme_of_work as sow "\
                    "  LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id "\
                    "  INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id "\
                    "  LEFT JOIN auth_user as user ON user.id = sow.created_by "\
                    " WHERE (sow.key_stage_id = {key_stage_id} or {key_stage_id} = 0) AND (sow.published = 1 OR sow.created_by = {auth_user})" \
                    " ORDER BY sow.key_stage_id;"
        select_sql = select_sql.format(key_stage_id=int(key_stage_id), auth_user=to_db_null(auth_user))

        rows = []
        rows = execHelper.execSql(db, select_sql, rows)
        return rows


    @staticmethod
    def get_latest_schemes_of_work(db, top = 5, auth_user = 0):
        """
        Gets the latest schemes of work with learning objectives
        :param db: the database context
        :param top: number of records to return
        :return: list of schemes of work models
        """
        
        execHelper = ExecHelper()
        
        select_sql = "SELECT DISTINCT "\
                    " sow.id as id," \
                    " sow.name as name," \
                    " sow.description as description," \
                    " sow.exam_board_id as exam_board_id," \
                    " exam.name as exam_board_name," \
                    " sow.key_stage_id as key_stage_id," \
                    " kys.name as key_stage_name," \
                    " sow.created as created," \
                    " sow.created_by as created_by_id," \
                    " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name," \
                    " sow.published as published"\
                    " FROM sow_scheme_of_work as sow" \
                    " LEFT JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id"\
                    " LEFT JOIN sow_learning_objective__has__lesson as lo_le ON lo_le.lesson_id = le.id"\
                    " LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id" \
                    " LEFT JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id "\
                    " LEFT JOIN auth_user as user ON user.id = sow.created_by" \
                    " WHERE sow.published = 1 OR sow.created_by = {auth_user}"\
                    " ORDER BY sow.created DESC LIMIT {top};"
        select_sql = select_sql.format(auth_user=to_db_null(auth_user), top=top)

        rows = []
        rows = execHelper.execSql(db, select_sql, rows)
        return rows
        

    @staticmethod
    def _update(db, model, published):
        execHelper = ExecHelper()

        str_update = "UPDATE sow_scheme_of_work SET name = '{name}', description = '{description}', exam_board_id = {exam_board_id}, key_stage_id = {key_stage_id}, published = {published} WHERE id =  {scheme_of_work_id};"
        str_update = str_update.format(
            name=to_db_null(model.name),
            description = to_db_null(model.description),
            exam_board_id = to_db_null(model.exam_board_id),
            key_stage_id=to_db_null(model.key_stage_id),
            scheme_of_work_id = to_db_null(model.id),
            published=published)

        execHelper.execCRUDSql(db, str_update, log_info=handle_log_info)

        return model


    @staticmethod
    def _insert(db, model, published):
        execHelper = ExecHelper()
        
        str_insert = "INSERT INTO sow_scheme_of_work (name, description, exam_board_id, key_stage_id, created, created_by, published) VALUES ('{name}', '{description}', {exam_board_id}, {key_stage_id}, '{created}', {created_by}, {published});SELECT LAST_INSERT_ID();"
        str_insert = str_insert.format(
            name=to_db_null(model.name),
            description=to_db_null(model.description),
            exam_board_id=to_db_null(model.exam_board_id),
            key_stage_id=to_db_null(model.key_stage_id),
            created=to_db_null(model.created),
            created_by=to_db_null(model.created_by_id),
            published=published)

        # get last inserted row id
        rows = []
        
        (result, new_id) = execHelper.execCRUDSql(db, str_insert, rows, handle_log_info)
        
        model.id = new_id

        return model


    @staticmethod
    def _delete(db, model):
        
        execHelper = ExecHelper()
        rval = []
        str_delete = "DELETE FROM sow_scheme_of_work WHERE id = {scheme_of_work_id} and published NOT IN (1);"
        str_delete = str_delete.format(scheme_of_work_id=model.id)
        
        rval = execHelper.execCRUDSql(db, str_delete, rval, log_info=handle_log_info)

        model.published = 2        
        return model


    @staticmethod
    def get_key_stage_id_only(db, scheme_of_work_id):

        execHelper = ExecHelper()
        
        select_sql = ("SELECT "\
                    "  sow.key_stage_id as key_stage_id "\
                    " FROM sow_scheme_of_work as sow "\
                    " LEFT JOIN auth_user as user ON user.id = sow.created_by "\
                    " WHERE sow.id = {scheme_of_work_id};".format(scheme_of_work_id=scheme_of_work_id))
        rows = []
        rows = execHelper.execSql(db, select_sql, rows)
        return rows


    @staticmethod
    def delete_unpublished(db, auth_user_id):
        """ Delete all unpublished schemes of work """

        execHelper = ExecHelper()
        
        """ Delete all unpublished learning objectives """
        str_delete = "DELETE FROM sow_scheme_of_work WHERE published IN (0,2);"
            
        rows = []
        rows = execHelper.execSql(db, str_delete, rows, handle_log_info)
        return rows

    @staticmethod
    def publish(db, auth_user_id, id_):
        
        model = SchemeOfWorkModel(id_)
        model.publish = True

        execHelper = ExecHelper()
        
        str_update = "UPDATE sow_scheme_of_work SET published = {published} WHERE id = {scheme_of_work_id};"
        str_update = str_update.format(published=1 if model.published else 0, scheme_of_work_id=model.id)

        rval = []
        execHelper.execCRUDSql(db, str_update, rval, handle_log_info)

        return rval

    @staticmethod
    def get_options(db, auth_user = 0):

        execHelper = ExecHelper()
        
        str_select = "SELECT sow.id, sow.name, ks.name as key_stage_name FROM sow_scheme_of_work as sow LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id WHERE sow.published = 1 OR sow.created_by = {auth_user} ORDER BY sow.key_stage_id;"
        str_select = str_select.format(auth_user=to_db_null(auth_user))
        rows = []
        rows = execHelper.execSql(db, str_select, rows)
        return rows


    @staticmethod
    def get_schemeofwork_name_only(db, scheme_of_work_id):
        
        execHelper = ExecHelper()
        
        select_sql = "SELECT "\
                    "  sow.name as name "\
                    " FROM sow_scheme_of_work as sow "\
                    " LEFT JOIN auth_user as user ON user.id = sow.created_by "\
                    " WHERE sow.id = {scheme_of_work_id};"
        select_sql = select_sql.format(scheme_of_work_id=scheme_of_work_id)

        rows = []
        rows = execHelper.execSql(db, select_sql, rows)
        return rows

