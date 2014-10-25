import sys
import time
import os
import linecache
import functools
import logging
import datetime
import threading
import signal


def synchronized(locker):
  def wrapper(func):
    @functools.wraps(func)
    def new_func(*args, **kwds):
      with locker:
        return func(*args, **kwds)
    return new_func
  return wrapper

def asynchronized(func, name = ''):
  def new_func(*args, **kwds):
    thread = threading.Thread(name = name, target = func, args = args, kwargs = kwds)
    return thread
  return new_func

def timeconsume(func = None, logger_func = sys.stdout.write):
  origin_func = sys.stdout.write
  def new_func(ifunc, *args, **kwds):
    start = datetime.datetime.now()
    value = ifunc(*args, **kwds)
    end = datetime.datetime.now()
    if logger_func == origin_func:
      print("time consume(%s): %s" % (ifunc.__name__, (end - start)))
      return value
    logger_func("time consume(%s): %s" % (ifunc.__name__, (end - start)))
    return value

  def decorator_func(ifunc):
    inner_func = functools.partial(new_func, ifunc)
    functools.wraps(ifunc)(inner_func)
    inner_func.__code__ = ifunc.__code__
    #_funcwrapper(ifunc, inner_func)
    return inner_func

  if func is None:
    return decorator_func

  inner_func = functools.partial(new_func, func)
  functools.wraps(func)(inner_func)
  inner_func.__code__ = func.__code__
  #_funcwrapper(func, inner_func)
  return inner_func
