# 键盘输入一组水果名称并以空格分隔，共一行，统计水果数量
txt = input('请输入类型序列')
fo = open('PY202.txt','w')
fruits = txt.split(' ')
d = {}
for i in fruits:
    d[i] = d.get(i,0)+1 #当键i在d中时返回该键的值，若不在d中则返回0
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True) #python排序默认是升序，所以输入reverse=True进行降序排序
for k in ls:
    fo.write('{}:{}\n'.format(k[0],k[1]))
fo.close()