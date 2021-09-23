fi = open('score.csv','r')
fo = open('avg-score.txt','w')
ls = []
txt = fi.readlines()
for i in txt[1:]:
    sum = 0
    for k in range(1,4):
        sum += int(i.split(',')[k])
        avg_score = sum/3
    ls.append(i.split(',')[0]+':'+'{:.2f}'.format(avg_score))
fo.writelines('\n'.join(ls))
fi.close()
fo.close()