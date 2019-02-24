# -*- coding: utf-8 -*-
"""
helper routines for retrieving and saving values in the database
"""

last_sql = ()

def to_db_null(val):
    return "NULL" if val is None else val


def to_empty(val):
    return "" if val is None else val


def add_escape_chars(string):
    return str(string).replace("'", "\"")
