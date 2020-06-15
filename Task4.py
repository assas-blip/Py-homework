a = input('Enter:')
b = ''
c = 0
for i in a:
    if i != ' ':
        b = b + i
    else:
        print(str(c) + b[0:9])
        c += 1
        b = ''
print(str(c) + b[0:9])