fi = open('PY301-vacations.csv','r')
ls = []
for line in fi:
    ls.append(line.strip('\n').split(','))
s = input('请输入节假日序号:').split(' ')
while True:
    for i in s:
        for line in ls:
            if i == line[0]:
                print('{}({})假期是{}月{}日至{}月{}日之间'.format(line[1],line[0],line[2][0:2],line[2][2:4],line[3][:2],line[3][2:]))
    s = input('请输入节假日序号').split(' ')