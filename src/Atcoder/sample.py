year = int(input())

a = year % 4
if a == 2:
    print(year)
elif a < 2:
    plus = 2 - a
    print(year + plus)
else:
    plus = 6 - a
    print(year + plus)
