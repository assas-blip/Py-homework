from math import factorial
from itertools import count
def a():
    for el in count(1):
        yield factorial(el)
gen = a()
c = 0
for i in gen:
    if c == 15:
        break
    else:
        c += 1
        print(i)