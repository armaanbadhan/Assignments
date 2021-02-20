
def makebinaryarr(n):
    res = []
    for i in range(2**n):
        temp_bin = []
        while i:
            temp_bin.append(i%2)
            i //= 2
        temp_bin += [0]*(n-len(temp_bin))
        res.append(temp_bin)
    return res


def powerset(arr, length):
    bin = makebinaryarr(length)
    res = []
    for i in range(len(bin)):
        temp_res = []
        for j in range(length):
            if bin[i][j] == 1:
                temp_res.append(arr[j])
        res.append(temp_res)
    return res


t = int(input())

for _ in range(t):
    n = int(input())
    myarr = [i+1 for i in range(n)]
    subsets = powerset(myarr, n)
    for i in subsets:
        print(*i)
