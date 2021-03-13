
def isprime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n&1 == 0:
        return False
    if n%3 == 0:
        return False
    cnt = 5
    s = int(n**(0.5)) + 1
    while cnt <= s:
        if n%cnt == 0:
            return False
        cnt += 2
        if n%cnt == 0:
            return False
        cnt += 4
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    a = n//2
    b = n-a
    found = False
    while a > 0 and b < n:
        if isprime(a) and isprime(b):
            print(a, b)
            found = True
            break
        a -= 1
        b += 1
    if not found:
        print(-1, -1)
