#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'vovo'

import re

file_name = "word.txt"

lines_count = 0
words_count = 0
chars_count = 0
words_dict = {}
lines_list = []

with open(file_name, 'r') as f:
    for line in f:
        line = line.strip() #去掉前後空白
        if len(line): #去掉空行
            lines_count = lines_count + 1
            chars_count = chars_count + len(line)
            match = re.findall(r'[^a-zA-Z0-9]+', line)
            for a in match:
                line = line.replace(a, ' ')
            lines_list = line.split()
            for i in lines_list:
                if i not in words_dict:
                    words_dict[i] = 1
                else:
                    words_dict[i] = words_dict[i] + 1
f.closed

print '總字數爲:', len(words_dict)
print '不爲空的行爲:', lines_count
print '字符數爲：', chars_count

words_dict = sorted(words_dict.iteritems(), key = lambda d:d[1], reverse=True)

for k in words_dict:
    print k