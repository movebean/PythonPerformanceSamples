import sys
import time
import os
import linecache
import functools
import logging
import datetime
import threading
import signal

InputDebugFunc = None
OutputDebugFunc = None
Enable = True

class IgnoreType(object):
  pass

def input(* types):
  def check_accepts(f):
    assert len(types) == f.func_code.co_argcount
    def new_f(* args, ** kwds):
      if not Enable:
        return f(* args, ** kwds)
      i = 0
      for (a, t) in zip(args, types):
        i += 1
        try:
          if t is IgnoreType:
            continue
          assert isinstance(a, t), "arg(%d) %r does not match %s" % (i, a, t)
        except AssertionError, e:
          if InputDebugFunc:
            InputDebugFunc(i, a, t)
          else:
            raise e
      return f(* args, ** kwds)
    new_f.func_name = f.func_name
    return new_f
  return check_accepts

def output(rtype):
  def check_returns(f):
    def new_f(* args, ** kwds):
      if not Enable:
        return f(* args, ** kwds)
      result = f(* args, ** kwds)
      try:
        if rtype is IgnoreType:
          return result
        assert isinstance(result, rtype), "return value %r does not match %s" % (result, rtype)
      except AssertionError, e:
        if InputDebugFunc:
          InputDebugFunc(i, a, t)
        else:
          raise e
      return result
    new_f.func_name = f.func_name
    return new_f
  return check_returns
