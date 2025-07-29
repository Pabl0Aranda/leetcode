import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"⏱ Tiempo: {time.time() - start:.6f}s")
        return result
    return wrapper
