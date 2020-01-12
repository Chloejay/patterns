import time 

#decorated function is the wrapper function, vice versa
def sleep(timeout, retry=2):
    def func(fn):
        def wrapper(*args, **kwargs):
            retries=0
            while retries <retry:
                try:
                    value= func(*args, **kwars)
                    if value is None:
                        return 
                except:
                    logging.info(f'sleep for {timeout} seconds')
                    time.sleep(timeout) 
                    retries +=1 
        return wrapper 
    return func 


#useful example 
# def fn(val):
#     def fn_decorator(decorator_fn):
#         def decorated_fn(*args, **kwargs):
#             for i in (val):
#                 decorator_fn(*args, **kwargs) 
#         return decorated_fn
#     return fn_decorator 

# @fn
# def decorated_fn(args):
#     pass 

