
class CacheProxy:

    @staticmethod
    def session_cache(request, db, name, fnc, *lookup_args):
        
        key = str((name, lookup_args)) # create unique key from name and lookup_id
        if not request.session.get(key):
            request.session[key] = fnc(db, *lookup_args).__dict__
        obj = request.session.get(key)

        return obj
