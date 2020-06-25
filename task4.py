from random import randint
a = [randint(-15, 15) for i in  range(15)]
b = [x for x in a if a.count(x) == 1]
print(a)
print(b)