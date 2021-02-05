n = int(input())
i = 1
while i <= n:
    print(5*(1 + i), end=' ')
    i += 1
    if i > n:
        break
    print(i, end=' ')
    i += 1