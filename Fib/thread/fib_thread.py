import time
from tools import timeconsume, asynchronized

def fib(num):
  if num <= 1:
    return 1
  else:
    return fib(num - 1) + fib(num - 2)

@timeconsume
def TestSync(num):
  fib(40)
  fib(40)

@timeconsume
def TestAsync(num):

  @asynchronized
  def _inner():
    fib(num)

  thread_list = []
  for _ in range(2):
    thread_list.append(_inner())

  for thread in thread_list:
    thread.start()

  for thread in thread_list:
    thread.join()

TestAsync(40)
TestSync(40)
