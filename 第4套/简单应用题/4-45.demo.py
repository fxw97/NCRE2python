fo = open('PY202.txt', 'w')
data = input('请输入课程名及对应的成绩:')
d = {}
while data:
    name, score = data.split(' ')
    d[name] = eval(score)
    data = input('请输入课程名及对应的成绩:')
course_list = sorted(list(d.values()))
max_score,min_score = course_list[-1],course_list[0]
average_score = sum(course_list)/len(course_list)
max_course, min_course = '',''
for i in d.items():
    if i[1]==max_score:
        max_course = i[0]
    if i[1] == min_score:
        min_course = i[0]
fo.write('最高分课{}{},最低分课是{}{},平均分是{}'.format(max_course,max_score,min_course,min_score,average_score))
fo.close()