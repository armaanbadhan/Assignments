t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    
    myarr = []

    for i in range(n):
        l, r = map(int, input().strip().split())
        myarr.append([l, 0])
        myarr.append([r, 1])
    
    count = 0
    ans = 0
    myarr.sort()

    for i in myarr:
        if (i[1] == 0):
            count += 1
        else:
            count -= 1
        ans = max(ans, count)
    
    print(ans)
