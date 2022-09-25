import math
a = int (input('Введите значение а: '))
b = int (input('Введите значение b: '))
c = (9*math.pi*b)+(10*math.cos(a))
d = (math.sqrt(b)-math.fabs(math.sin(b)))
e = (c/d*math.pow(math.e,a))
print(e)