while True:
    seasons = {
        12 or 1 or 2: 'winter', (3 or 4 or 5): 'spring',
        (6 or 7 or 8): 'summer', (9 or 10 or 11): 'autumn'
    }
    a = input("month:")
    if int(a) < 13 and int(a) > 0:
        print(a)
        print(a + "nd month is " + seasons.get(int(a)))
        break
    else:
        print('Enter right month')
