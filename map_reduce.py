# -*- coding: utf-8 -*-

from functools import reduce

#map最后得到一个列表，reduce得到一个数，但在实际使用之前本身都只是一个迭代器。它们后面跟的参数也都必须是迭代器。

def str2float(s):

    index = s.find('.')         #用string的find和replace属性确定除以的倍数，并去掉小数点。
    time = len(s)-index-1
    L = s.replace(".","")

    def fn(x, y):               #reduce该函数，合并成整数
        return x * 10 + y

    def char2num(s):            #map该函数，完成str-num的映射
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
        
    num = reduce(fn, map(char2num, L))
    return num/(10**time)       #得到浮点数

print(str2float('1234.56'))