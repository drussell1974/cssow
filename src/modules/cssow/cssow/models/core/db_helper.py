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

def execCRUDSql(db, sql, result=None):
    ''' run the sql statement without results '''
    if db != None:
        cur = _execSql(db, sql)
        for tup in cur:
            result.append(tup)
        db.commit()    
        _closeSqlConn(db, None)

def execSql(db, sql, result, enable_logging=False):
    ''' run the sql statement '''
    if db != None:
        cur = _execSql(db, sql)
        for tup in cur:
            result.append(tup)
        _closeSqlConn(db, None)


def to_db_null(val):
    return "NULL" if val is None else sql_safe(val)


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