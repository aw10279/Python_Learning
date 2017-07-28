# -*- coding: utf-8 -*-

import os

def search1(path, kw):    #先将path下的文件和目录分类，再对每个目录进行递归，完成遍历。
    dir = [m for m in os.listdir(path) if os.path.isdir(os.path.join(path, m))]
    file = [os.path.join(path, n) for n in os.listdir(path) if os.path.isfile(os.path.join(path, n)) and kw in os.path.splitext(n)[0]]
    if dir:
        for x in dir:
            file = file + search1(os.path.join(path, x),kw)

    return file


L = []
def search2(path, kw):    #对path下的文件和目录单独判断、执行，执行完毕再进入下一个。
    for n in os.listdir(path):
        if os.path.isfile(os.path.join(path, n)):
            if kw in os.path.splitext(n)[0]:
                L.append(os.path.join(path, n))
        if os.path.isdir(os.path.join(path, n)):
            search2(os.path.join(path, n), kw)
    return L

#print(search1('C:\\111', 'test') )
print(search2('C:\\111', 'test') )