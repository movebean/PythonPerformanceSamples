from tools import timeconsume, cached

@cached
def fib(num):
  if num <= 1:
    return 1
  else:
    return fib(num - 1) + fib(num - 2)

@timeconsume
def TestCache(num):
  fib(num)

TestCache(40)

