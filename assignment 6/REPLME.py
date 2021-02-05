ar = []
for i in range(int(input())):
    ar.append(int(input()))

while len(ar) != 1:
    x, y, *ar = sorted(ar)
    ar.append((3*x + 2*y) % 100)

print(*ar)

"""
ar = []
for i in range(int(input())):
    ar.append(int(input()))

def dostuff(a):
    if len(a) == 1:
        return a[0]
    else:
        x, y, *a = sorted(a)
        a.append((3*x + 2*y) % 100)
        return dostuff(a)

print(dostuff(ar))
"""