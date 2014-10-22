cdef inline int fib(int num):
  if num <= 1:
    return 1
  else:
    return fib(num - 1) + fib(num - 2)

def fib_import(int num):
  return fib(num)
