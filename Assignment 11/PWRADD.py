import sys
 
def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())
# --------------------- Do not touch anything above this line ----------------------

def modm(x):
    return add(x//2, x-x//2)


def multi(q, p):
    temp = 0
    for _ in range(p):
        temp += q
        temp = modm(temp)
    return temp


def pwr(a, b):
    ans = 1
    for _ in range(b):
        ans = multi(ans, a)
        ans = modm(ans)
    return ans
 
# --------------------- Do not touch anything below this line ----------------------
 
 
a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)
 