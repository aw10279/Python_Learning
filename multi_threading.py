# -*- coding: utf-8 -*-

import time, threading

mid = 0
lock = threading.Lock()  #给线程加锁，以保证在当前线程完成之前其他线程不能修改变量

def do_it(n):
	global mid
	mid += n
	mid -= n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()  #获得锁
        try:
            do_it(n)
        finally:
        	lock.release()  #释放锁，后续进程才能再获得锁

t1 = threading.Thread(target = run_thread, args = (5,))  #创建2个线程。不加锁的情况下，mid被2个线程同时操作，mid可能不会为0
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()

print(mid)