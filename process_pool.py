# -*- coding: utf-8 -*-

from multiprocessing import Process
from multiprocessing import Pool
import os, time, random

def proc(name):
    print('Child %s: %s' % (name, os.getpid()))

#if __name__ == '__main__':
    #print('Parent: %s' % (os.getpid()))
    #p = Process(target = proc, args = ('test',))    #使用Process创建1个子进程实例
    #print('Child is ready now.Go!!!')
    #p.start()
    #p.join()
    #print('Child stopped.')

def mp(name):
    print('Prcess %s is starting: %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Process %s lasts %0.2f seconds.' % (name, (end-start)))

if __name__ == '__main__':
    print('Parent: %s' % (os.getpid()))
    p = Pool(4)                                     #使用Pool创建包含4个进程的进程池
    for i in range(6):
        p.apply_async(mp, args = (i,))
    
    print('Wating all processes finished...')    
    p.close()
    p.join()

    print('All processes finished.')
