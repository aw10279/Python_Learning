# -*- coding: utf-8 -*-

#------------------------------------------------client进程，用于执行任务并返回结果---------------------------

import queue, time, math
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')                #2个队列都直接从网络获取，因此本身无需定义，直接注册接口即可
QueueManager.register('get_result_queue')

server_adr = '127.0.0.1'
m = QueueManager(address=(server_adr, 5000), authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):                                   #执行task中的任务，并将结果放入result
	try:
		n = task.get(timeout=1)
		print('run task %d...' % n)
		r = 'the square root of %d = %f' % (n, math.sqrt(n))
		time.sleep(1)
		result.put(r)
	except Queue.Empty:                              #遇到empty异常跳出循环
		print('task queue is empty.')

print('Task exit.')