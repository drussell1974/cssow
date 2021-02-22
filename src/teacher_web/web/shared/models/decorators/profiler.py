from datetime import datetime, timedelta

class running_time_log():
    _instance = None
    log = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(running_time_log, cls).__new__(cls)
            cls._instance.running_time_log = {}

        return cls._instance
    

    def write(self, func_name, arg_key, timespan):

        min_key = f"{func_name}_{arg_key}__min";

        if min_key in running_time_log.log:
            min_cur = running_time_log.log[min_key]
            if min_cur > timespan:
                running_time_log.log[min_key] = timespan
        else:
            running_time_log.log[min_key] = timespan
        
        max_key = f"{func_name}_{arg_key}__max"
        
        if max_key in running_time_log.log:
            max_cur = running_time_log.log[max_key]
            if max_cur < timespan:
                running_time_log.log[max_key] = timespan
        else:
            running_time_log.log[max_key] = timespan
                

    def show(self):
        print("printing 'running time logs'...")
        for entry in running_time_log.log.items():
            print(entry)


class running_time():
    def __init__(self, max_benchmark_ms, arg_idx = 0):
        self.arg_idx = arg_idx
        self.max_benchmark_ms = max_benchmark_ms
        

    def write(self, func, args, timespan):
        time_log = running_time_log()
            
        key2 = args[self.arg_idx] if self.arg_idx > 0 else ""
        time_log.write(func.__name__, key2, timespan)
        time_log.show()
        

    def __call__(self, func):
        def inner(*args, **kwargs):

            s1 = datetime.now()

            # calling function
            res = func(*args, **kwargs)

            s2 = datetime.now()
            
            timespan = s2 - s1
            
            if timespan > timedelta(microseconds=self.max_benchmark_ms):
                self.write(func, args, timespan.total_seconds())

            return res


        return inner