# 计算两点之间的距离
ntxt = input('请输入四个数字(以空格分隔):')
nsl = ntxt.split(' ')
x0 = eval(nsl[0])
y0 = eval(nsl[1])
x1 = eval(nsl[2])
y1 = eval(nsl[3])

r = pow(pow(x1-x0,2)+pow(y1-y0,2),0.5)
print('{:.1f}'.format(r))