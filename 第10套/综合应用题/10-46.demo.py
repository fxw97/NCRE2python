import random
var='a'
lst=[chr(ord(var)+i) for i in range(26)]
letter = lst[random.randint(0,25)]
count = 0
while True:
    letter_input = input('请输入26个字母中的任一个：')
    count += 1
    if letter_input not in lst:
        print('请重新输入字母')
    else:
        if count > 100:
            print('猜测超过5次，答题失败')
            break
        else:
            if letter_input == letter:
                print('恭喜你猜对了，共猜了{}次'.format(count))
                break
            elif letter_input > letter:
                print('你输入的字母在该字母之后')
            elif letter_input < letter:
                print('你输入的字母在该字母之前')
            else:
                print('未知错误')