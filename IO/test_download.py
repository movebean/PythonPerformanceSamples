#!/usr/bin/python
import gevent
from gevent import socket
from gevent import monkey
import time
from tools import timeconsume
from tools import asynchronized
import os
from urllib2 import urlopen

monkey.patch_all()

TOTAL_NUM = 1
URL = "http://www.google.com"
URL = "http://kosmixmedia.com/static/4b7609c0cb834864b992d908504c03ba.jpg"

@timeconsume
def TestGevent():
  def _inner(url):
    _ = urlopen(url).read()
  jobs = []
  for i in  range(TOTAL_NUM):
    jobs.append(gevent.spawn(_inner, URL))

  gevent.joinall(jobs)

@timeconsume
def TestThreading():
  @asynchronized
  def _inner():
    _ = urlopen(URL).read()

  thread_list = []
  for i in  range(TOTAL_NUM):
    thread_list.append(_inner())

  for thread in thread_list:
    thread.start()
  for thread in thread_list:
    thread.join()

@timeconsume
def TestSynchron():
  for i in  range(TOTAL_NUM):
    a = urlopen(URL).read()
  print a



TestSynchron()
#TestThreading()
#TestGevent()
