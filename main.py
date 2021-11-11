g = int(input("Выберите режим работы (1-кодирование, 2-декодирование):"))
s = int(input("Введите ключ:"))
if g == 2:
    s = -s
else:
    s = s
x = input("Введите сообщение:")
x = list(x)
if g == 2:
    print("Декодированное сообщение:", end='')
else:
    print("Кодированное сообщение:", end='')
for c in x:
    m = ord(c)
    if s > 0:
        if 47 < m < 58:
            if 47 < m + s % 10 < 58:
                print(chr(m + s % 10), end='')
            else:
                print(chr(m + s % 10 - 10), end='')
        elif 64 < m < 91:
            if 64 < m + s % 26 < 91:
                print(chr(m + s % 26), end='')
            else:
                print(chr(m + s % 26 - 26), end='')
        elif 96 < m < 123:
            if 96 < m + s % 26 < 123:
                print(chr(m + s % 26), end='')
            else:
                print(chr(m + s % 26 - 26), end='')
        elif 1039 < m < 1072:
            if 1039 < m + s % 32 < 1072:
                print(chr(m + s % 32), end='')
            else:
                print(chr(m + s % 32 - 32), end='')
        elif 1071 < m < 1104:
            if 1071 < m + s % 32 < 1104:
                print(chr(m + s % 32), end='')
            else:
                print(chr(m + s % 32 - 32), end='')
        else:
            print(chr(m), end='')
    else:
        if 47 < m < 58:
            if 47 < m - (abs(s) % 10) < 58:
                print(chr(m - (abs(s) % 10)), end='')
            else:
                print(chr(m + 10 - (abs(s) % 10)), end='')
        elif 64 < m < 91:
            if 64 < m + -(abs(s) % 26) < 91:
                print(chr(m + -(abs(s) % 26)), end='')
            else:
                print(chr(m - (abs(s) % 26) + 26), end='')
        elif 96 < m < 123:
            if 96 < m - (abs(s) % 26) < 123:
                print(chr(m - (abs(s) % 26)), end='')
            else:
                print(chr(m - (abs(s) % 26) + 26), end='')
        elif 1039 < m < 1072:
            if 1039 < m - (abs(s) % 32) < 1072:
                print(chr(m - (abs(s) % 32)), end='')
            else:
                print(chr(m - (abs(s) % 32) + 32), end='')
        elif 1071 < m < 1104:
            if 1071 < m - (abs(s) % 32) < 1104:
                print(chr(m - (abs(s) % 32)), end='')
            else:
                print(chr(m - (abs(s) % 32) + 32), end='')
        else:
            print(chr(m), end='')
