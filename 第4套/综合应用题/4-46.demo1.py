fi = open('sensor.txt','r')
fo = open('earpa001.txt','w')
txt = fi.readlines()
ls = []
for i in txt:
    info = i.strip().split(',')
    if info[1] == ' earpa001':
        ls.append(info)
for k in ls:
    fo.writelines(','.join(k)+'\n')
# for k in ls:
#     fo.write("{},{},{},{}\n".format(k[0],k[1],k[2],k[3]))
fo.close()
fi.close()