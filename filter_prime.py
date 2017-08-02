# -*- coding: utf-8 -*-

def odd_iter():  #专门生成奇数的无限生成器
	n = 1
	while True:
		n +=2
		yield n

def no_div(n):   #返回的匿名函数用于判断是否可被n整除
	return lambda x: x % n > 0

def prime():
	yield 2      #先返回第一个素数：2
	L = odd_iter()
	while True:
		n = next(L) #不断返回下一个奇数用于判断
		yield n
		L = filter(no_div(n), L)  #将奇数序列中所有能被n整除的全部过滤掉

for i in prime():
	if i < 1000:  #由于是无限生成器，需给定范围
		print (i)
	else:
		break