#  coding: utf-8

import os, random

def rn(path='F:\\1', suffix='mp3'):
    file = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and suffix in os.path.splitext(x)[1]]
    n = len(file)
    sn = random.sample([num for num in range(1, n+1)], n)
    for i in range(n):
        os.rename(os.path.join(path,file[i]),os.path.join(path,str(sn[i])+'.'+file[i]))

if __name__ == '__main__':

    rn()