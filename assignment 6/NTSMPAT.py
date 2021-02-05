n = int(input())
for i in range(n):
    for j in range(2*i + 1):
        q = i - abs(j-i)
        print(i + q + 1, end=' ')
    print("")
