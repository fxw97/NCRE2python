# 统计一句话中中文字符个数及中文词组个数
import jieba
s = input('请输入一个字符串')
n = len(s)
m = len(jieba.lcut(s))
print('中文字符数为{}，中文词语数为{}。'.format(n,m))