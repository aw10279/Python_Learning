# -*- coding: utf-8 -*-

import re

email1 = re.compile(r'^(\w+|\w+.\w+)@([a-zA-Z0-9]+\w*.\w+)$') # \w可匹配字母、数字和下划线，要只允许字母和数字，必须[a-zA-Z0-9]
x = email1.match('someone_123@gmail.cn')                      # .和@无需转义，_ ； ，需要。尽量用r''来避免转义错误
y = email1.match('bill.gates@micro_soft.com')                 # +至少1个，*至少0个，^表示头部，$表示尾部
print(x.group(1), x.group(2))
print(y.group(1), y.group(2))


email2 = re.compile(r'<(\w+\s\w+)>\s+(\w+@\w+.\w+)$')
z = email2.match('<Tom Paris> tom09@voyage38.org')
print(z.group(1), z.group(2))
