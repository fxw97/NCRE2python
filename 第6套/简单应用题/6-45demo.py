# 判断是否为闰年
def judge_year(year):
    if (year%4==0 and year%100!=0) or (year%400 ==0):
        print(year,'年是闰年')
    else:
        print(year,'年不是闰年')

year = eval(input('请输入年份:'))
judge_year(year)