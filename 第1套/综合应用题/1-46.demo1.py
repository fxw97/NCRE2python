import jieba
fi = open('小女孩.txt','r')
fo = open('PY301-1.txt','w')
txt = fi.read()
d = {}
exclude = "，"
for world in txt:
    if world in exclude:
        continue
    else:
        d[world] = d.get(world,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
fo.write('{}:{}'.format(ls[0][0],ls[0][1]))
fo.close()
fi.close()