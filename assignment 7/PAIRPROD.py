n = int(input())
su = 0
sqsu = 0
for _ in range(n):
    x = int(input())
    su += x
    sqsu += x*x


print(2)
print(((su*su)-sqsu)//2)
