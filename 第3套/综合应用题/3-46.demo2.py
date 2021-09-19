fi = open('论语-原文.txt','r')
fo = open('论语-提纯原文.txt','w')
for line in fi:
    for i in line: # 或者 for i in range(0,23)
        line = line.replace('({})'.format(i),'')
    fo.write(line)
fo.close()
fi.close()