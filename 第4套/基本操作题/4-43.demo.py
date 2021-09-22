# 整数和unicode编码之间互相转换
n = eval(input('请输入整数：'))
print('{:+^11}'.format(chr(n-1)+chr(n)+chr(n+1)))