# -*- coding: utf-8 -*-

def move(n,a,b,c):

    if n == 1:
        print(a,'-->',c)
        return
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(10,'A','B','C')