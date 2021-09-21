# 将输入的数字改为二进制、八进制及十六进制输出
num = eval(input('输入数字:'))
print('对应的而进制数:{0:b}\n八进制数{0:o}\n十六进制数{0:X}'.format(num)) # 因为format中只传入一个数，所以在三个{}中必须指定format()中num的索引