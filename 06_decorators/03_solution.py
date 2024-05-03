import time

def cache(func):
    cached_value ={}
    print(cached_value)
    def wrapper(*args):
        if args in cached_value:
            return cached_value[args]
        result = func(*args)
        cached_value[args] = result
        return result
    return wrapper

@cache
def long_run_func(a,b):
    time.sleep(4)
    return a+b

print(long_run_func(2,3))
print(long_run_func(2,3))


