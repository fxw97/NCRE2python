fruit = input('输入水果:')
lis = ['苹果','哈密瓜','橘子','猕猴桃','杨梅','西瓜']
if fruit in lis:
    print("{}在列表lis中".format(fruit))
else:
    print("{}不在列表lis中".format(fruit))