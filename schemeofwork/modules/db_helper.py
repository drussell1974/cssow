# -*- coding: utf-8 -*-
"""
helper routines for retrieving and saving values in the database
"""

last_sql = ()

def to_db_null(val):
    return "NULL" if val is None else sql_safe(val)


def to_empty(val):
    return "" if val is None else val

def to_db_bool(val):
    return 1 if bool(val) == True else 0

def sql_safe(string):
    return str(string)\
        .strip(' ')\
        .replace("'", "\"")\
        .replace(";", "\;")\
