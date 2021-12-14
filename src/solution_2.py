l = []
for i in range(int(input())):
    l.append(int(input()))

l = sorted(l)


res = 0

for i in l:
    temp = i * (len(l) - l.index(i))
    if temp > res:
        res = temp

print(res)