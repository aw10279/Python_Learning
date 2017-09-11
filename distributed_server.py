# -*- coding: utf-8 -*-

#-----------------------------------------------server进程，用于分发任务并接收结果----------------------------------

import queue, random, time
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()                      #新建任务队列和结果队列
result_queue = queue.Queue()

class QueueManager(BaseManager):               #让QueueManager继承所有Basemanager的方法
    pass

def t_queue():                                 #建2个返回队列的函数，专用于下面的网络调用
    return task_queue
def r_queue():
    return result_queue

QueueManager.register('get_task_queue', callable=t_queue)     #将2个队列在网络上注册，并定义网络接口名称
QueueManager.register('get_result_queue', callable=r_queue)

manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')   #实例化QueueManager并定义IP、端口号、验证码

def server_start():                           #将manager的启动封装到一个函数内，用于下面的main函数调用
    manager.start()

    task = manager.get_task_queue()           #从网络渠道获取2个队列（非本地获取）
    result = manager.get_result_queue()

    for i in range(10):                       #将任务放入task队列
        n = random.randint(0, 10000)
        print('send task %d...' % n)
        task.put(n)

    print('Try get results...')

    for i in range(10):                       #从result队列获取结果
        r = result.get(timeout=10)
        print('%s' % r)

    manager.shutdown()
    print('Manager exit.')

if __name__ == '__main__':
    #freeze_support()
    server_start()
