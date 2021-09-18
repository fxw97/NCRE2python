# 买不同件数衣服打不同折扣
n = eval(input('请输入数量:'))
if n==1:
    cost = 150
elif n>=2 and n<=3:
    cost = n*150*0.9
elif n>=4 and n<=9:
    cost = n*150*0.8
elif n>=10:
    cost = n*150*0.7
print('总额为:{:.0f}'.format(cost))