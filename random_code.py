# -*- coding: utf-8 -*-

import random
import string

L = string.ascii_letters + string.digits  #使用string的2个属性，即可得到所有字母+数字，返回字符串

def random_code(number, amount = 1):
    for x in range(amount):
    	code = ''.join(random.choice(L) for y in range(number))  #choice属性随机选择；''.join是用某种方式（此处是空）将所有元素连接起来
    	print(code)


random_code(20, 10)