# 生成5个0到50的随机数，每个随机数之间用空格分隔，打印输出这五个数
import random
random.seed(255)
for i in range(5):
    print(random.randint(0,50),end=' ')