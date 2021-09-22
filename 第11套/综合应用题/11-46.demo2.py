fo = open('candidate0.txt','r')
lines = fo.readlines()
fo.close()
fi = open('candidate.txt','w')
L=[]
for line in lines:
    student = line.strip('\n').split(' ')
    for i in student[-10:]:
        if int(i) < 60:
            break
    else:
        L.append(student)
print(L)
for l in L:
    fi.write(' '.join(l)+'\n')
fi.close()