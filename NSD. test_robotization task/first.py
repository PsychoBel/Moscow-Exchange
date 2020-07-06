string = input() + ' '
s = 0
n = string[0]
for i in string:
    if n != i:
        if s == 1:
            print(n, end = '')
        else:
            print(str(s) + n, end = '')
        s = 0
        n = i
    s += 1

