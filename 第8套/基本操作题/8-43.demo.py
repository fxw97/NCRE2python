# 使用循环输出1-50之间的奇数
count = 0
while count<50:
    count += 1
    if count%2 ==0:
        continue
    print(count,end=',')