fi = open('arrogant.txt','r')
txt = fi.read()
fi.close()
fo = open('PY301-2.txt','w')
d = {}
for i in txt:
    d[i] = d.get(i,0)+1
del d['\n']
ls = list(d.items())
ls.sort(key = lambda x:x[-1],reverse=True)
for k in ls[0:10]:
    fo.write('{}:{}\n'.format(k[0],k[1]))
fo.close()