# 将9×9乘法表写入txt中
fo = open('PY202.txt','w')
for i in range(1,10):
    for j in range(1,i+1):
        fo.write('{}×{}={} '.format(j,i,i*j))
    fo.write('\n')
fo.close()