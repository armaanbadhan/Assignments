n = int(input())

dick = {}
for _ in range(n):
    a, b, name, dir = input().strip().split()
    for i in a, b:
        if i in dick:
            dick[i].append(name)
        else:
            dick[i] = [name]

res = 0
for i in dick:
    if len(dick[i]) == 4 and len(set(dick[i])) == 2:
        res += 1
print(res)