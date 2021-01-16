from time import time

"""List down the values of the units digit of the first 10 powers of 3.
In other words calculate 3x % 10 for x = 0, 1, ... 9 . Observe the
pattern and draw a flowchart to calculate 3x % 10 , where x is
any non-negative integer which is obtained as input."""
"""
for i in range(0, 10):
    print(3**i % 10)
1
3
9
7
1
3
9
7
1
3
"""

x = int(input("enter x:"))
"""
THIS CODE IS TIME CONSUMING
start = time()

print(3**x % 10)

print(time() - start)
"""
start = time()

n = x % 4

if n == 0:
    print(1)
elif n == 1:
    print(3)
elif n == 2:
    print(9)
else:
    print(7)
print(time() - start)
