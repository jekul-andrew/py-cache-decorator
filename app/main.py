from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}
    f_name = func.__name__

    if not cache_data.get("f_name", False):
        cache_data[f_name] = {}

    cur_cache = cache_data[f_name]

    def inner(*args) -> Callable:

        result = cur_cache.get(args, False)
        if result is not False:
            print("Getting from cache")
            return result

        result = func(*args)
        cur_cache[args] = result
        print("Calculating new result")
        return result

    return inner
