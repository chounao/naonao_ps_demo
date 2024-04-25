import random
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {attempts+1} failed: {e}")
                    attempts += 1
                    time.sleep(delay)
            raise Exception(f"Function {func.__name__} failed after {max_attempts} attempts")
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2)
def perform_operation():
    # 模拟执行操作的代码
    if random.random() < 0.8:
        raise Exception("Operation failed")
        # raise ValueError('a')
    else:
        return "Operation successful"

result = perform_operation()
print(result)