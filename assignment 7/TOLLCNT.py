from math import ceil
def calc(t1, t2):
    t = ceil((t2 - t1)/60)
    return t*30 +30

n = int(input())
final = 0
mydicc = {}
for _ in range(n):
    ee = input().strip()
    lic = input().strip()
    t = int(input().strip())
    if ee == "entry":
        mydicc[lic] = t
    else:
         final += calc(mydicc[lic], t)
         del mydicc[lic]

    # print(final, mydicc, t)

print(final)
