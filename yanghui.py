# -*- coding: utf-8 -*-

def yanghui(m,n):

    L = [1]
    i = 0

    while i < m:
        L.append(0)
        L = [L[j-1]+L[j] for j in range(len(L))]
        i += 1

    if 0 <= n <= m:
        print(L[n])
    else:
        print('invalid query')

def tri(m):

    L = [1]
    i = 0

    while i < m:
        print (L)
        L.append(0)
        L = [L[j-1]+L[j] for j in range(len(L))]
        i += 1


def triangles():

    L = [1]
    i = 0

    while True:
        yield L
        L.append(0)
        L = [L[j-1]+L[j] for j in range(len(L))]
        i += 1

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break