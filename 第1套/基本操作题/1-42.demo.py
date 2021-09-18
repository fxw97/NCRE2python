# 斐波拉切数列，输出不大于50的序列数
a,b = 0,1
while a <= 500000000000:
    print(a,end = ',')
    a,b=b,a+b