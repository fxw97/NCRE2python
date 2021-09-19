# 靠右填充，带千位分隔符
n =eval(input('请输入正整数：'))
print('{:@>30,}'.format(n))