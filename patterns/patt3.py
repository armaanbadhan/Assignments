n = int(input())
num = 1
for i in range(n):
    for j in range(2**i):
        print(num%10, end='')
        num += 1
        if num%10 == 0:
            num += 1
    print("")
