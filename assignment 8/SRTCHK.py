t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    if sorted(a) == b:
        print('yes')
    else:
        print('no')
