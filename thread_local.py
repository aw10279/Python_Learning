# -*- coding: utf-8 -*-

import threading

weapon = threading.local()  #用local新建全局对象weapon，每个线程都可以调用

def weapon_display(N, T):  
    weapon.name = N        #给weapon新建2个属性并赋值
    weapon.type = T

    weapon_type()          #调用另一函数使用这2个属性


def weapon_type():  #使用已赋值的2个属性并调用线程名称
    print('%s for %s in (%s)' % (weapon.name, weapon.type, threading.current_thread().name))

#新建2个线程都运行weapon_display，但赋不同的值。每个线程都调用weapon，但数据彼此独立，从而实现用全局对象存储所有线程下某变量并
#根据线程名查找对应变量值的功能
t1 = threading.Thread(target= weapon_display, args=('Tank', 'Heavy',), name='WAR-1')
t2 = threading.Thread(target= weapon_display, args=('Rifle', 'Light',), name='WAR-2')
t1.start()
t2.start()
t1.join()
t2.join()
