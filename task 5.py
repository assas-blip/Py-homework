i = 0
while True:
    print("Выберете действие")
    print("1Выйти")
    print("2Продолжить")
    chs = input()
    if chs == "2":
        a = [int(i) for i in input("Введите ряд чисел").split()]
        def my_func(b):
            d = 0
            for c in b:
                 d += c
            return d
        i = i + my_func(a)
        print(i)
    else:
        break