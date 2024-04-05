s = input()

pattern = 1
i = 1
b_str = s[0]

while i < len(s):

    if b_str == s[i]:
        i += 1
        continue
    else:
        b_str = s[i]
        pattern += 1

    i += 1

print(pattern)
cnt = pattern * (pattern - 1)
cnt = cnt - (pattern - 2)
print(cnt)
