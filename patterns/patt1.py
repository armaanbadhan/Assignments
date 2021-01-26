n = int(input())

print("*"*n)
for row in range(1, n - 1):
    q = abs(row - (n-1)//2) + 1
    print("*"*q + " "*(n - 2*q) + "*"*q)
print("*"*n)

"""

for n = 7

*******
*** ***
**   **
*     *
**   **
*** ***
*******
"""
