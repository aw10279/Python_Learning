# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):

    dt = b*b-4*a*c
    if dt < 0:
        print('该组参数无解')
    elif dt == 0:
        print('x1 = x2 =',-b/(2*a))
    else:
        x1 = (-b+math.sqrt(dt))/(2*a)
        x2 = (-b-math.sqrt(dt))/(2*a)
        print('x1 =',x1,'\nx2 =',x2)
    return

quadratic(3,-4,-31)