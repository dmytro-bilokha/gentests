#!/usr/local/bin/python
# -*- coding: koi8-u -*-
import locale, sys, os, random

numq = 10 # number of questions in test

afile = file("ansdb.txt", "rb")

shifr = {}
for line in afile.readlines():
   qnum, ashifr = line.split("-")
   shifr[qnum] = ashifr
afile.close()
argums = sys.argv
ans_sh = argums[1]
qnum, ashifr = ans_sh.split("-")
bals = 0
for i in range(numq):
    if shifr[qnum][i] == ashifr[i]:
        bals += 1
print "Right answers: %d" % bals
