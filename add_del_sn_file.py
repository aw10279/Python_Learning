#  coding: utf-8

import os, random, re


def add_sn(path='C:\\儿歌', suffix='mp3'):
    file = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and suffix in os.path.splitext(x)[1]]
    n = len(file)
    sn = random.sample([num for num in range(1, n+1)], n)
    print(n)
    print(file)
    for i in range(n):
        os.rename(os.path.join(path,file[i]),os.path.join(path,str(sn[i])+'.'+file[i]))

def del_sn1(path='C:\\儿歌'):  #开头无数字的文件不可用
    for x in os.listdir(path):
        name = x
        while name[0] != ".":
            name = name.replace(name[0], '', 1)  #replace的第三个参数是替换个数，1表示只替换第一个，3表示替换前三个，无参数表示全部替换
        name = name.replace(name[0], '', 1)
        os.rename(os.path.join(path,x),os.path.join(path,name))

def del_sn2(path='C:\\儿歌'):
    for x in os.listdir(path):
        name = re.sub('^\d+.', '', x)           #用正则直接匹配出前面的数字和“.”并删除,若无数字则不操作，比sn1更通用
        os.rename(os.path.join(path,x),os.path.join(path,name))



if __name__ == '__main__':
    del_sn2()
    add_sn()