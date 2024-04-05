line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

n = line1[0]
a = line1[1]
b = line1[1]

i = 0
is_holiday = True
while i < n:
    target = line2[i]
    while target > (a + b):
        target = target - (a + b)

    if target > a:
        # not holiday
        is_holiday = False
        break

    i += 1

if is_holiday is True:
    print("Yes")
else:
    print("No")
