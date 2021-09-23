fi = open('score.csv','r')
fo = open('avg-score-2.txt','w')
ls = []
x = []
sum = 0
for row in fi:
    ls.append(row.strip('\n').split(','))
for line in ls[1:]:
    for i in line[1:]:
        sum = int(i)+sum
        avg = sum/3
    x.append(avg)
    sum=0
fo.write('语文:{:.2f}\n数学:{:.2f}\n英语:{:.2f}\n物理:{:.2f}\n科学:{:.2f}\n'.format(x[0],x[1],x[2],x[3],x[4]))