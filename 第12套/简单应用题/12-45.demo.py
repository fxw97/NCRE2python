# 村长选举
f = open('name.txt')
names = f.readlines()
f.close()
f = open('vote.txt')
votes = f.readlines()
f.close()
f = open('vote1.txt','w')
d = {}
NUM = 0
for vote in votes:
    num = len(vote.split(' '))
    if num==1 and vote in names:
        d[vote[:-1]] = d.get(vote[:-1],0)+1
        num+=1
    else:
        f.write(vote)
f.close()
l = list(d.items())
l.sort(key=lambda x:x[-1],reverse=True)
name = l[0][0]
score = l[0][1]
print('有效票数为:{} 当选村长村民为:{} 票数为:{}'.format(NUM,name,score))