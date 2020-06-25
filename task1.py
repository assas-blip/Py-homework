from sys import argv



def salary():
    hours, rate, bonus = map(int, argv[1:])
    return int(hours) * int(rate) + int(bonus)


salary()