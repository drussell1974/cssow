# -*- coding: utf-8 -*-
"""
helper routines for retrieving and saving values in the database
"""
import mysql.connector

last_sql = ()

def _execSql(db, sql):
    cnx = mysql.connector.connect(
            user='drussell1974', password='password',
            host='127.0.0.1',
            database='cssow_api')

    cursor = cnx.cursor()
    cursor.execute(sql)
    return cnx, cursor


def _closeSqlConn(cnx, cursor):
        cursor.close()
        cnx.close()

def execCRUDSql(db, sql):
    ''' run the sql statement without results '''
    if db == None:
        cnx, cursor = _execSql(db, sql)
        cnx.commit()        
        _closeSqlConn(cnx, cursor)


def execSql(db, sql, result):
    ''' run the sql statement '''
    if db == None:
        cnx, cursor = _execSql(db, sql)
        for tup in cursor:
            result.append(tup)
    _closeSqlConn(cnx, cursor)


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
        .replace(";", "\;")\
