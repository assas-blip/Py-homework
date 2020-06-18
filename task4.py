'''x = input('first number')
y = input('second number')
def my_func(x, y):
    return x ** y
print(my_func(x, y))'''
# 1 способ

x = int(input('first number'))
y = int(input('second negative number'))
def my_func(x, y):
    y = y * -1
    i = y
    while i != 0:
        x = x * y
        i -= 1
    return 1 / x
print(my_func(x, y))