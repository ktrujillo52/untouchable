#!/usr/bin/python
#Untouchable numbers
import random

array = range(1,10000)
k = 0
while k == 0:
    for i in range(1,10000):
        s = []
        for j in range(1,1000000):
            if i % j == 0:
                if i not in s:
                    s.append(i)
                if j not in s:
                    s.append(j)
        r = []
        for i in s:
            if i not in r:
                r.append(i)
        h = []
        for i in range(1,10000):
            for j in r:
                if i == j:
                    h.append(j)
        h = h[:-1]
        tot = 0
        for i in h:
            tot += i
        try:
            array.remove(tot)
        except:
            k = 0
        sort = []
        for i in range(1,10000):
            for j in array:
                if i == j:
                    sort.append(j)
        print str(sort)+"\n"
        
