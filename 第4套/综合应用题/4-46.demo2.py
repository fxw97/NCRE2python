fi = open('earpa001.txt','r')
fo = open('earpa001_count.txt','w')
d = {}
for line in fi:
    temp = line.strip('\n').split(',')
    floor_area = temp[2]+'-'+temp[3]
    d[floor_area] = d.get(floor_area, 0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[-1],reverse=True)
for i in ls:
    fo.write('{},{}\n'.format(i[0],i[1]))
fi.close()
fo.close()