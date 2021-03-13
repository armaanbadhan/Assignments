
def issymmetric(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


def islowertri(arr, n):
    for i in range(n):
        for j in range(i):
            if arr[i][j] != 0:
                return 0
    return 1


def isuppertri(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][j] != 0:
                return 0
    return 1


t = int(input())

for asdf in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        lust = list(map(int, input().strip().split()))
        arr.append(lust)

    x = isuppertri(arr, n)
    y = islowertri(arr, n)
    z = issymmetric(arr, n)

    print(z + (2*(x or y)) + (4*(x and y)))
