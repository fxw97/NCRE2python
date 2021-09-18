fi = open('小女孩.txt','r')
fo = open('PY301-3.txt','w')
text = fi.read()
d = {}
for i in text:
    d[i] = d.get(i,0)+1
del d['\n']
del d[' ']
ls = list(d.items())
ls.sort(key= lambda x:x[1],reverse=True)
for k in range(len(ls)):
    ls[k] = '{}:{}'.format(ls[k][0],ls[k][1])
fo.write(','.join(ls))
fo.close()
fi.close()