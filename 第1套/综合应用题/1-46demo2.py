fi = open('小女孩.txt','r')
fo = open('PY301-2.txt','w')
text = fi.read()
d = {}
for i in text:
    d[i] = d.get(i,0)+1
del d['\n']
ls = list(d.items())
ls.sort(key= lambda x:x[1],reverse=True)
for k in range(10):
    fo.write(ls[k][0])
fo.close()
fi.close()