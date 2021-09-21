for i in range(0,4):
    for j in range(0,4-i):
        print(' ',end='')
    print('*'*i)
for i in range(0,4):
    for k in range(0,i):
        print(' ', end = '')
    print('*'*(4-i))