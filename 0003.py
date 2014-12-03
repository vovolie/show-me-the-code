#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'vovo'


import redis
import uuid
client = redis.Redis()
i = 0
client.flushdb()
for a in xrange(0, 200):
    i = i+1
    a = uuid.uuid1()
    key = "api_key:%s" % i
    client.set(key, a)

print client.keys()
print client.dbsize()


