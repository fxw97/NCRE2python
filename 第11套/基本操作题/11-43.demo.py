a,b,c = [int(x) for x in input().split(',')]
ls = []
for i in range(c):
    ls.append(a+b*i)
print(ls)