# -*- coding: utf-8 -*-

import queue, random, time
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def t_queue():
    return task_queue
def r_queue():
    return result_queue

QueueManager.register('get_task_queue', callable=t_queue)
QueueManager.register('get_result_queue', callable=r_queue)

manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

def server_start():
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('send task %d...' % n)
        task.put(n)

    print('Try get results...')

    for i in range(10):
        r = result.get(timeout=10)
        print('%s' % r)

    manager.shutdown()
    print('Manager exit.')

if __name__ == '__main__':
    #freeze_support()
    server_start()
