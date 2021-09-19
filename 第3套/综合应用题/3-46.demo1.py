fi = open('论语.txt','r')
fo = open('论语-原文.txt','w')
flag = False
for line in fi:
    if '【' in line:
        flag = False
    if '【原文】' in line:
        flag = True
        continue
    if flag == True:
        fo.write(line.lstrip()) # lstrip()作用是去除字符串左侧的空白或指定字符
fo.close()
fi.close()