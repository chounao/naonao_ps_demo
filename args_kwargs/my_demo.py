# from args_kwargs.common_logger import MyLogger
# import logging
# logger = MyLogger('mylog.log')
#
#
# def suppress_errors(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             print(f"函数 {func.__name__} 执行时发生了错误：{e}")
#     return wrapper
#
# @suppress_errors
# def my_function(c):
#     a=1
#     b=2
#     if a+b==c:
#         logger.log(logging.INFO)
#         raise ValueError("对了")
#     else:
#         logger.log(logging.ERROR)
#         raise ValueError("错了")
#
# my_function(5)
x = 10
y = 20

def my_function():
    z = 30
    print(globals())
    print("--------------")

my_function()