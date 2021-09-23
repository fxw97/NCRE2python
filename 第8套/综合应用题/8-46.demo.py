# 凯撒密码解码
intxt = input('请输入明文:')
for i in intxt:
    if "a" <= i <= "z":
        print(chr(ord("a") + (ord(i) - ord("a") + 3) % 26), end='')
    elif 'A' <= i <= 'Z':
        print(chr(ord('A') + (ord(i) - ord('A') + 3) % 26), end='')
    else:
        print(i, end='')


