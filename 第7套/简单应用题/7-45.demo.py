# 输入区间内所有素数
lower = eval(input('输入区间最小值:'))
upper = eval(input('输入区间最大值:'))
for num in range(lower+1,upper):
    flag = True  # 定义一个判断变量
    for i in range(2,num):  # 判断是否为合数，若为合数，则flag设为false
        if num%i == 0:
            flag = False
    if flag == True:
        print(num)