my_list = [7, 5, 3, 3, 2]
while True:
    b = input()
    for c in my_list:
        if c < int(b):
            print(b + ',\n' + str(c) + ', ')
            b = 0
        else:
            print(str(c) + ', ')
