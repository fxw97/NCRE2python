# 计算输入一段话的平均词长
import jieba
txt = input('请输入一段中文文本:')
ls = jieba.lcut(txt)
print('{:.1f}'.format(len(txt)/len(ls)))
