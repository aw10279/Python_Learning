# -*- coding: utf-8 -*-

import functools

def log(txt=''):    #txt默认为空，也可以赋值。所以可以根据log的参数数量决定是否导入文本，无需if即可实现2种功能
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s begin call %s()" % (txt, func.__name__))
            ret = func(*args, **kw)
            print("%s end call %s()" % (txt, func.__name__))
            return ret
        return wrapper
        
    return decorator

@log()          #()表示只有1个函数参数，txt取默认值；('excute')先给txt赋值，然后传入函数参数
#@log('excute')         
def f():               
    print("Just now!")
f()