L = []
f = open('score.txt','r')
lines = f.readlines()
f.close()
fi = open('candidate0.txt','w')
for line in lines:
    score_sum = 0
    line_temp = line.strip('\n').split(' ')
    for score in line_temp[3:]:
        score_sum += int(score)
    line_temp.append(str(score_sum))
    L.append(line_temp)
L.sort(key = lambda x:x[-1],reverse = True)
print(L)
for i in range(10):
    fi.write(' '.join(L[i][:-1])+'\n')
fi.close()