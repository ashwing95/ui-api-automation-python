from logger import Logger
import time
from functools import wraps


def logged(func):
    log = Logger().get_logger()
    @wraps(func)
    def run(*args,**kwargs):
        log.info("Functionstatrted|{0}".format(func.__name__))
        out = func(*args,**kwargs)
        log.info("Functionstopped|{0}".format(func.__name__))
        return out


    return run


def timed(func):
    log = Logger().get_logger()
    @wraps(func)
    def run(*args,**kwargs):
        time1 = time.time()
        out = func(*args,**kwargs)
        time2 = time.time() - time1
        log.info("Function {} executed in {:.4f} seconds".format(func.__name__))
        return out
    return run



