n = input()
d = {}
for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
dup = []
for i in d.items():
    dup.append([i[1],i[0]])
dup.sort()
for i in dup:
    print(i[1])
