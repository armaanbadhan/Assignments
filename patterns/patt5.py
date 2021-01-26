n = int(input())
rows = 2*n - 1
for i in range(1, rows + 1):
    q = n - abs(i - n)
    print(" "*(q-1) + str(q), end = "")
    if q != n:
        print(" "*(rows-(2*q)) + str(q))
    else:
        print('')


"""
n = 5
1       1
 2     2
  3   3
   4 4
    5
   4 4
  3   3
 2     2
1       1
"""