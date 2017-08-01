import math
def sum2(start, end, func):          #将累加运算抽象出来单独做函数，这样可以把任何函数进行累加运算，无需写入每个函数。
    total = 0
    for x in range(start, end+1):
        total += func(x)
    return total


def func1(x):
    return x


def func2(x):
    return x ** 2 + 1

def circle(r):
    return (math.pi*r**2)

print(sum2(1, 100, func1))
print(sum2(1, 100, func2))
print(circle(10))
