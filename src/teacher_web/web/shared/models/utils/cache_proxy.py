
class CacheProxy:

    @classmethod
    def session_cache(cls, request, db, name, fnc, *lookup_args):
        
        key = str((name, lookup_args)) # create unique key from name and lookup_id
        if not request.session.get(key):
            request.session[key] = fnc(db, *lookup_args).__dict__
        obj = request.session.get(key)

        return obj


    @classmethod
    def print_cache(cls, request, print_key = None):
        print("SESSION...")
        for key, value in request.session.items():
            if print_key is not None and print_key not in key:
                continue
            print('{} => {}'.format(key, value))
        print("...SESSION")
