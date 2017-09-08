# -*- coding: utf-8 -*-

"""在一个宾馆里住着六个不同国籍的人，他们分别来自美国、德国、英国、法国、俄罗斯和意大利。他们的名字叫 A、B、C、D、E、F。名字的
顺序与上面的国籍不一定相互对应。

A 和美国人是医生
E 和俄罗斯人是教师
C 和德国人是技师
B 和 F 曾经当过兵，而德国人从未参过军
法国人比 A 年龄大，意大利人比 C 年龄大
B 同美国人下周要去西安旅行，而 C 同法国人下周要去杭州度假

通过上述描述，判断 A、B、C、D、E、F 各是哪国人？"""


[print(i) for p in __import__('itertools').permutations('美俄德法意英') if all([p[0] not in "美俄德法", p[1] not in "德美", p[2] not in "美俄德意法", p[4] not in "美俄德", p[5] not in "德"]) for i in zip('ABCDEF', p)]

#只用列表生成式即可实现，非常精彩。使用itertools.permutations实现list的全序排列；all()同时满足所有条件；zip()直接实现配对输出。
#生成式中的语句排列顺序，实际就是改编为正常语句的顺序，此例为：for-if-for，3层依次套嵌。