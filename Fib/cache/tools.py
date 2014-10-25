import functools
import sys
import datetime

DEFAULT_CACHE_LENGTH = 100000

def cached(func = None, cached_dict = None, cache_length = DEFAULT_CACHE_LENGTH):
  if cached_dict is None:
    cached_dict = {}
  key_list = []

  def new_func(ifunc, *arg, **kwds):
    key = str(arg) + str(kwds)
    if key in cached_dict:
      return cached_dict[key]
    result = ifunc(*arg, **kwds)
    if len(cached_dict) >= cache_length:
      front_key = key_list[0]
      key_list.remove(front_key)
      del cached_dict[front_key]
    cached_dict[key] = result
    key_list.append(key)
    return result

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

  return new_func
