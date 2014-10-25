from tools import *

@input(str)
def printA(a):
  print a

@output(str)
def printStr(s):
  return s

@input(IgnoreType)
def printIgnore(a):
  print a

#printA(10)    # fail
printA('hello world')
#printStr(10)    # fail
printStr('hello world')
printIgnore([1,2,3])
