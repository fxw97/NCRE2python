# 统计输入的职业数
fo = open('PY202.txt', 'w')
names = input('请输入各个同学行业名称，行业之间用空格间隔:')
name_list=names.split(' ')
d = {}
for i in name_list:
    d[i] = d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for k in ls:
    fo.write('{}:{}'.format(k[0],k[1]))
fo.close()