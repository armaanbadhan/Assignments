n = int(input())
myset = set()
for _ in range(n):
    myset.add(int(input()))

print(1)

q = int(input())
for _ in range(q):
    if int(input()) in myset:
        print('yes')
    else:
        print('no')
