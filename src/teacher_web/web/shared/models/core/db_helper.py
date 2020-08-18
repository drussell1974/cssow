# -*- coding: utf-8 -*-
"""
helper routines for retrieving and saving values in the database
"""
import mysql.connector
from .log_type import LOG_TYPE

class ExecHelper:
    #############################
    # TODO: create as singleton #
    #############################
    #last_sql = ()
    #def _log_it(self, db, sql, enable_logging):
    #    l = log.Log();
    #    l.is_enabled = enable_logging
    #   l.write(db, sql)

    def _execSql(self, db, sql, params=None):

        with db.cursor() as cur:
            cur.execute(sql, params)
            result = cur.fetchall()
        return result


    def _closeSqlConn(self, db, cursor):
            db.close()


    def execCRUDSql(self, db, sql_statement, result=[], log_info=None):
        ''' run the sql statement without results '''
        
        last_insert_id = 0
        if db != None:

            if log_info != None:
                log_info(db, "execCRUDSql", "executing:{}".format(sql_statement), LOG_TYPE.Verbose)

            cur = self._execSql(db, sql_statement)
            for tup in cur:
                result.append(tup)

            cur_li = self._execSql(db, "SELECT LAST_INSERT_ID();")
        
            last_insert_id = int(cur_li[0][0])


            db.commit()    
            self._closeSqlConn(db, None)

            if log_info != None:
                log_info(db, "execCRUDSql", "result:{}".format(result), LOG_TYPE.Verbose)
        
        return (result, last_insert_id)


    def execSql(self, db, sql, result, log_info=None):
        ''' run the sql statement '''
        if db != None:

            if log_info != None:
                log_info(db, "execSql", "executing:{}".format(sql), LOG_TYPE.Verbose)
            
            cur = self._execSql(db, sql)
            for tup in cur:
                result.append(tup)
            self._closeSqlConn(db, None)

            if log_info != None:
                log_info(db, "execSql", "results:{}".format(result), LOG_TYPE.Verbose)

        # returns appended result
        return result


    def select(self, db, sql, params, result, log_info=None):
    
        ''' run the sql statement '''
        if db != None:
            try:
                if log_info != None:
                    log_info(db, "select using callproc", "executing:{}".format(sql), LOG_TYPE.Verbose)
                
                cur = db.cursor()
                cur.callproc(sql, params)
                result = cur.fetchall()

                cur.close()

                self._closeSqlConn(db, None)

                if log_info != None:
                    log_info(db, "select using callproc", "fetchall returned :{}".format(result), LOG_TYPE.Verbose)
            
            except Exception as e:
                log_info(db, "ExecHelper.select", "An error occurred selecting data '%s'" % sql, log_type=LOG_TYPE.Error)    
                raise e
            
        return result


    def insert(self, db, sql, params, log_info=None):
        ''' run the sql statement '''

        result = []
        try:
            if db != None:

                if log_info is not None:
                    log_info(db, "insert using callproc", "executing:{}".format(sql), LOG_TYPE.Verbose)
                
                cur = db.cursor()
                cur.callproc(sql, params)
                result = cur.fetchone()
            
                cur.close()
            
                self._closeSqlConn(db, None)

                if log_info is not None:
                    log_info(db, "insert using callproc", "new_id = {}".format(result), LOG_TYPE.Verbose)

        except Exception as e:
            if log_info is not None:
                log_info(db, "ExecHelper.insert", "An error occurred inserting data '{}'".format(sql), LOG_TYPE.Error)    
            raise e

        return result


    def update(self, db, sql, params, log_info=None):
        ''' run the sql statement '''
        result = []

        try:
            if db != None:
                
                cur = db.cursor()
                cur.callproc(sql, params)
                result = cur.rowcount
            
                cur.close()
            
                self._closeSqlConn(db, None)

                if log_info != None:
                    log_info(db, "update", "executed:{}, with results: number of records affected = {}".format(sql, result), LOG_TYPE.Verbose)

        except Exception as e:
            log_info(db, "ExecHelper.update", "An error occurred updating data '%s'" % sql, log_type=LOG_TYPE.Error)    
            raise e

        return result


    def delete(self, db, sql, params, log_info=None):
        ''' run the sql statement '''

        result = []
        try:
            if db != None:

                if log_info != None:
                    log_info(db, "delete", "executing:{}".format(sql), LOG_TYPE.Verbose)
                
                cur = db.cursor()
                cur.callproc(sql, params)
                result = cur.rowcount

                cur.close()

                self._closeSqlConn(db, None)

                if log_info != None:
                    log_info(db, "delete", "results: number of records affected = {}".format(result), LOG_TYPE.Verbose)
                    
        except Exception as e:
            log_info(db, "ExecHelper.delete", "An error occurred deleting data '%s'" % sql, log_type=LOG_TYPE.Error)    
            raise e

        return result


def to_db_null(val, as_null = None):
    return "NULL" if val is None or val is as_null else sql_safe(val)


def to_empty(val):
    return "" if val is None else val


def to_db_bool(val):
    return 1 if val == True else 0


def from_db_bool(val):
    return True if val == 1 else False


def sql_safe(string):
    return str(string)\
        .strip(' ')\
        .replace("'", "\"")\
        .replace(";", "\;")