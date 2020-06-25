import functools
def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el
print(functools.reduce(my_func,[i for i in range(100, 1000) if i % 2 == 0]))