# -*- coding: utf-8 -*-

import queue, random, time
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManger(BaseManager):
    pass

def t_queue():
    return task_queue
def r_queue():
    return result_queue

QueueManger.register('get_task_queue', callable=t_queue)
QueueManger.register('get_result_queue', callable=r_queue)

manager = QueueManger(address=('127.0.0.1', 5000), authkey=b'123')

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(10000)
    print('send task %d' % n)
    task.put(n)
