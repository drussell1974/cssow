# -*- coding: utf-8 -*-
"""
helper routines for retrieving and saving values in the database
"""
import mysql.connector

last_sql = ()
def _log_it(db, sql, enable_logging):
    l = log.Log();
    l.is_enabled = enable_logging
    l.write(db, sql)

def _execSql(db, sql):

    with db.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()
    return result


def _closeSqlConn(db, cursor):
        #cursor.close()
        db.close()

def execCRUDSql(db, sql, result=[], log_info=None):
    ''' run the sql statement without results '''
    if db != None:

        if log_info != None:
            log_info(db, "executing:{}".format(sql))

        cur = _execSql(db, sql)
        for tup in cur:
            result.append(tup)
        
        cur_li = _execSql(db, "SELECT LAST_INSERT_ID();")
        for tup in cur_li:
            result.append(tup)

        db.commit()    
        _closeSqlConn(db, None)

        if log_info != None:
            log_info(db, "result:{}".format(result))


def execSql(db, sql, result, log_info=None):
    ''' run the sql statement '''
    if db != None:

        if log_info != None:
            log_info(db, "executing:{}".format(sql))
        
        cur = _execSql(db, sql)
        for tup in cur:
            result.append(tup)
        _closeSqlConn(db, None)

        if log_info != None:
            log_info(db, "results:{}".format(result))


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