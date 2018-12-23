
def to_db_null(val):
    return "NULL" if val is None else val


def to_utf8(val):
    return str(val).encode(val, 'utf-8')
