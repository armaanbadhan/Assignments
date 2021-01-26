n = int(input())

for i in range(n):
    q = abs((abs(i-n//2)) - n//2)
    print(" "*q + "*"*(q+1))

"""
n = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
""""
