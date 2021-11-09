print("Введите на сколько символов произвести смещение:")
s = int(input())
print("Введите сообщение:")
x = input()
for c in x:
    m = ord(c)
    if s > 0:
        if 47 < m < 58:
            if 47 < m + s % 10 < 58:
                print(chr(m + s % 10))
            else:
                print(chr(m + s % 10 - 10))
        elif 64 < m < 91:
            if 64 < m + s % 26 < 91:
                print(chr(m + s % 26))
            else:
                print(chr(m + s % 26 - 26))
        elif 96 < m < 123:
            if 96 < m + s % 26 < 123:
                print(chr(m + s % 26))
            else:
                print(chr(m + s % 26 - 26))
        elif 1039 < m < 1072:
            if 1039 < m + s % 32 < 1072:
                print(chr(m + s))
            else:
                print(chr(m + s % 32 - 32))
        elif 1071 < m < 1104:
            if 1071 < m + s % 32 < 1084:
                print(chr(m + s))
            else:
                print(chr(m + s % 32 - 32))
        else:
            print(chr(m))
    else:
        if 47 < m < 58:
            if 47 < m - (abs(s) % 10) < 58:
                print(chr(m - (abs(s) % 10)))
            else:
                print(chr(m + 10 - (abs(s) % 10)))
        elif 64 < m < 91:
            if 64 < m + -(abs(s) % 26) < 91:
                print(chr(m + -(abs(s) % 26)))
            else:
                print(chr(m - (abs(s) % 26) + 26))
        elif 96 < m < 123:
            if 96 < m - (abs(s) % 26) < 123:
                print(chr(m - (abs(s) % 26)))
            else:
                print(chr(m - (abs(s) % 26) + 26))
        elif 1039 < m < 1072:
            if 1039 < m - (abs(s) % 32) < 1072:
                print(chr(m - (abs(s) % 32)))
            else:
                print(chr(m - (abs(s) % 32) + 32))
        elif 1071 < m < 1104:
            if 1071 < m - (abs(s) % 32) < 1104:
                print(chr(m - (abs(s) % 32)))
            else:
                print(chr(m - (abs(s) % 32) + 32))
        else:
            print(chr(m))
