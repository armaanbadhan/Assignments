
def weirdsort(arr):
    neg_denom = [i for i in arr if i[1]<0]
    pos_denom = [i for i in arr if i[1]>0]
    neg_denom.sort(key=lambda x : abs(x[0]))
    pos_denom.sort(key=lambda x : abs(x[0]))
    return pos_denom + neg_denom


n = int(input())
inp = list(map(int, input().strip().split()))

arr = []
for i in range(0, 2*n, 2):
    arr.append((inp[i], inp[i+1]))


p_inf = []
n_inf = []
all = []

for i in arr:
    a, b = i[0], i[1]
    if b == 0:
        if a > 0:
            p_inf.append(i)
        else:
            n_inf.append(i)
    else:
        all.append(i)

p_inf.sort()
n_inf.sort(reverse=True)

dick = {}

for i in all:
    x = i[0]/i[1]
    if x not in dick:
        dick[x] = [i]
    else:
        dick[x].append(i)


_dick = []
for i in dick:
    _dick.append([i, dick[i]])

_dick.sort()
all_res = []

for i in _dick:
    all_res.append(weirdsort(i[1])[0])

res = []

if n_inf:
    res.append(tuple(n_inf[0]))

res += all_res

if p_inf:
    res.append(tuple(p_inf[0]))

print(len(res))
for i in res:
    print(*i, end=' ')
