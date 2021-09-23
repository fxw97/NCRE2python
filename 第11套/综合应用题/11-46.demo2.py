fo = open('candidate0.txt','r')
lines = fo.readlines()
fo.close()
fi = open('candidate.txt','w')
L=[]
for line in lines:
    student = line.strip('\n').split(' ')
    for i in student[-10:]:
        if int(i) < 60:
            break                # 当不满足条件则退出当前循环
    else:                        # 只要循环正常运行了，则将student添加到L中 这里是for...else结构，当for中循环没有break时，才执行else语句
        L.append(student)
print(L)
for l in L:
    fi.write(' '.join(l)+'\n')
fi.close()