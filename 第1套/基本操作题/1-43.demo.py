# 将输入的文本逆序输出
import jieba
text = input('请输入一段中文文本:')

ls = jieba.lcut(text)
for i in ls[::-1]:
    print(i,end='')