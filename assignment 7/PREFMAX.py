n = int(input())
ans = 0
max = -1
for _ in range(n):
    x = int(input())
    if x >= max:
        max = x
        ans += 1

print(2)
print(ans)
