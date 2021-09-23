fi = open('arrogant.txt','r')
txt = fi.read()
fi.close()
fo = open('PY301-1.txt','w')
d = {}
for i in txt:
    d[i] = d.get(i,0)+1
del d['\n']
ls = list(d.items())
for k in ls:
    fo.write('{}:{}\n'.format(k[0],k[1]))
fo.close()