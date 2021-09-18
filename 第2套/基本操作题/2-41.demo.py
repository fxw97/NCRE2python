# 随机输出一个手机品牌
import random
brandlist = ['三星','苹果','vivo','OPPO','魅族']
random.seed(0)
i = random.randint(0,4)
name = brandlist[i]
print(name)