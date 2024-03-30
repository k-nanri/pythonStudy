first = list(map(int, input().split()))
data = list(map(int, input().split()))

n = first[0]
k = first[1]

result = ""
i = 0

while i < n:
    if data[i] % k == 0:
        if len(result) == 0:
            result = str(data[i] // k)
        else:
            result = result + " " + str(data[i] // k)

    i += 1

print(result)
