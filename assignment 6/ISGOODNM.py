n = int(input())

s = n**(1/2)
sum = 1

if s*s == n:
    sum += s

s = int(s)

for i in range(2, s):
    if n%i == 0:
        sum += i + n//i
if sum == n:
    print("YES")
else:
    print("NO")
