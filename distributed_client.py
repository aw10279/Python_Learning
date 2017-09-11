# -*- coding: utf-8 -*-

import queue, time, math
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_adr = '127.0.0.1'
m = QueueManager(address=(server_adr, 5000), authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d...' % n)
		r = 'the square root of %d = %f' % (n, math.sqrt(n))
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')

print('Task exit.')