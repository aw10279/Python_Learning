import random
r=random.randint(0,9)
L=['0','1','2','3','4','5','6','7','8','9']  #限定输入字符的范围，后面方便判断

def rightinput(s):                           #判断输入字符是否合法，后面3处都会用到该函数
    while (s in L)==False:
        s=input("输入错误，请输入数字0-9:")
    return s

print('------猜数游戏开始------')
temp=input('0-9,你猜会是哪一个:')


guess=int(rightinput(temp))
i=1
while guess!=r and i<3:
    i+=1
    if guess>r:
        temp=input('有点大哦，再猜一次:')
        guess=int(rightinput(temp))#函数判断
    else:
        temp=input('有点小哦，再猜一次:')
        guess=int(rightinput(temp))#函数判断
if guess==r:
    print('恭喜你猜中啦！！！')
else:
    print('很遗憾，已经猜错三次了。。。答案是',r)
print('------游戏结束------')