# 列表中的值两两相乘
a = [11,3,8]
b = eval(input())
s = 0
for i in range(3):
    s += a[i]*b[i]
print(s)