import jieba
f = open('data.txt','r')
lines = f.readlines()
f.close()
f = open('out.txt','w')
for line in lines:
    line = line.strip()
    worldList = jieba.lcut(line)
    f.write('\n'.join(worldList))
f.close()
f = open('out.txt','r')
worlds = f.readlines()
f.close()
d = {}
for w in worlds:
    d[w[:-1]] = d.get(w[:-1],0)+1
print('曹操出现次数:{}'.format(d['曹操']))