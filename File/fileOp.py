from tools import timeconsume

NUM = 30000000
@timeconsume
def TestWrite():
  f = open("a.txt", 'w')
  for _ in range(NUM):
    f.write("go")

@timeconsume
def TestRead():
  f = open("a.txt", "r")
  for line in f.readlines():
    pass

TestWrite()
TestRead()
