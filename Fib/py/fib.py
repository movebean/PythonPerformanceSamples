import pyximport
import time
pyximport.install()

from fib import fib_import

start = time.time()
print fib_import(45)
end = time.time()
print end - start
