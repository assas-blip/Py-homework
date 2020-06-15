while True:
    names = []
    prices = []
    amount = []
    units = []
    name = ""
    price = 0
    num = 0
    unit = ""
    a1 = (1, {})
    a2 = (2, {})
    a3 = (3, {})
    a4 = (4, {})
    a5 = (5, {})
    a6 = (6, {})
    a7 = (7, {})
    a8 = (8, {})
    a9 = (9, {})
    a10 = (10, {})
    if names == []:
        print("Нет товаров")
    print("Выберите действие:")
    print('1Добавить товар(max = 10):' )
    print('2Узнать названия/цену/колиество/единицы измерения.')
    print("3Узнать о (Номер слота)")
    search = input("Введите номер опции:")
    if search == "1":
        search=input('выберете номер слота (1 - 10):')
        if search == "1":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a1[1]["Название"] = name
            a1[1]["Цена"] = price
            a1[1]["Количество"] = num
            a1[1]["Единица"] = unit
        if search == "2":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a2[1]["Название"] = name
            a2[1]["Цена"] = price
            a2[1]["Количество"] = num
            a2[1]["Единица"] = unit
        if search == "3":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a3[1]["Название"] = name
            a3[1]["Цена"] = price
            a3[1]["Количество"] = num
            a3[1]["Единица"] = unit
        if search == "4":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a4[1]["Название"] = name
            a4[1]["Цена"] = price
            a4[1]["Количество"] = num
            a4[1]["Единица"] = unit
        if search == "5":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a5[1]["Название"] = name
            a5[1]["Цена"] = price
            a5[1]["Количество"] = num
            a5[1]["Единица"] = unit
        if search == "6":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a6[1]["Название"] = name
            a6[1]["Цена"] = price
            a6[1]["Количество"] = num
            a6[1]["Единица"] = unit
        if search == "7":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a7[1]["Название"] = name
            a7[1]["Цена"] = price
            a7[1]["Количество"] = num
            a7[1]["Единица"] = unit
        if search == "8":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a8[1]["Название"] = name
            a8[1]["Цена"] = price
            a8[1]["Количество"] = num
            a8[1]["Единица"] = unit
        if search == "9":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a9[1]["Название"] = name
            a9[1]["Цена"] = price
            a9[1]["Количество"] = num
            a9[1]["Единица"] = unit
        if search == "10":
            print("Введите название:")
            name = input()
            print("Введите цену:")
            price = input()
            print("Введите кол - во:")
            num = input()
            print("Введите единицу измерения:")
            unit = input()
            a10[1]["Название"] = name
            a10[1]["Цена"] = price
            a10[1]["Количество"] = num
            a10[1]["Единица"] = unit
    if search == "3":
        search = input("Введите номер:")
        if search == "1":
            print(a1)
        if search == "2":
            print(a2)
        if search == "3":
            print(a3)
        if search == "4":
            print(a4)
        if search == "5":
            print(a5)
        if search == "6":
            print(a6)
        if search == "7":
            print(a7)
        if search == "8":
            print(a8)
        if search == "9":
            print(a9)
        if search == "10":
            print(a10)
    names = [
        a1[1].items(), a2[1].items(), a3[1].items(), a4[1].items(), a5[1].items(), a6[1].items(),
        a7[1].items(), a8[1].items(), a9[1].items(), a10[1].items()
    ][0]
    prices = [
        a1[1].items(), a2[1].items(), a3[1].items(), a4[1].items(), a5[1].items(), a6[1].items(),
        a7[1].items(), a8[1].items(), a9[1].items(), a10[1].items()
    ][1]
    amount = [
        a1[1].items(), a2[1].items(), a3[1].items(), a4[1].items(), a5[1].items(), a6[1].items(),
        a7[1].items(), a8[1].items(), a9[1].items(), a10[1].items()
    ][2]
    units = [
        a1[1].items(), a2[1].items(), a3[1].items(), a4[1].items(), a5[1].items(), a6[1].items(),
        a7[1].items(), a8[1].items(), a9[1].items(), a10[1].items()
    ][3]
    if search == "2":
        print("Что вы хотите узнать:")
        print("1Наименования")
        print("2Цены")
        print("3Количество")
        print("4Единицы измерения")


