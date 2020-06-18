name = input('Your name:')
surname = input('Surname:')
bdate = input('Birth date:')
city = input('Your city:')
email = input("Email:")
pnum = input("Phone number:")
def sum(name, surname, bdate, city, email, pnum):
    return ' '.join([name, surname, bdate, city, email, pnum])
print(sum(name, surname, bdate, city, email, pnum))

