# 计算输入的平均年龄和女性的人数
fo = open("PY202.txt","w")
data = input("请输入一组人员的姓名、性别、年龄：")  # 姓名 年龄 性别
women_num = 0
age_amount = 0
person_num = 0
while data:
    name, sex, age = data.split(' ')  # 注意分隔字符串并赋值要在循环内部
    if sex == '女':
        women_num += 1
    age_amount += int(age)
    person_num += 1
    data = input("请输入一组人员的姓名、性别、年龄：")
average_age = age_amount / person_num
fo.write("平均年龄是{:.1f} 女性人数是{}".format(average_age, women_num))
fo.close()