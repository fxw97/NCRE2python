import math
try:
    a = eval(input('请输入底数:'))
    b = eval(input('请输入真数:'))
    c = math.log(b,a)
except ValueError:
    if a<=0 and b>0:
        print('底数不能小于等于0')
    if a>=0 and b<0:
        print('真数不能小于等于0')
    elif a <= 0 and b<=0:
        print('真数和底数都不能小于等于0')
except ZeroDivisionError:
    print('底数不能为1')
except NameError:
    print('输入必须为实数')
else:
    print(c)