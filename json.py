# -*- coding: utf-8 -*-

import json

class Std(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def s2d(s):
    return {'name':s.name, 'age':s.age, 'score':s.score}

def d2s(d):
    return Std(d['name'], d['age'], d['score'])


s = Std('Bob', 20, 88)
print(json.dumps(s, default = s2d))
#print(json.dumps(s, default = lambda obj: obj.__dict__))  default后面可用通用格式


d = '{"age": 20, "score": 88, "name": "Bob"}'   #json必须以字符串为参数
t = json.loads(d, object_hook=d2s)              #转化为实例对象

print(t.name, t.age, t.score)