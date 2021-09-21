# 将列表中的素数去除
fo = open('PY202.txt','w')
def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True
ls = [51,33,54,56,67,88,431,111,141,72,45,2,78,12,15,5,69]
lis = []
for i in ls:
    if prime(i) == False:
        lis.append(i)
fo.write('>>>{},列表长度为{}'.format(lis,len(lis)))
fo.close()