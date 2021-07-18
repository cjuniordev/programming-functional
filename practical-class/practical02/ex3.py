l = int(input())
c = int(input())

if 1 <= l <= 1000 and 1 <= c <= 1000:
    if (l % 2) == 0 and (c % 2) == 0 or (l % 2) == 1 and (c % 2) == 1:
        print('1')
    else:
        print('0')