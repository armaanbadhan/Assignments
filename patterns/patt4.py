n = int(input("Odd number: "))
rows = 2*n - 1
for row in range(1, rows + 1):
    if row == n:
        print("* "*n)
        continue
    q = n - abs(row - n)
    p = ""
    for i in range((q-1)//2 + 1):
        if q&1:
            p += "*"
        p += " "
        if not q&1:
            p += "*"
    print(p + " "*(rows - 2*len(p)) + p[::-1])

"""
n = 7
*           *
 *         * 
* *       * *
 * *     * * 
* * *   * * *
 * * * * * * 
* * * * * * *
 * * * * * * 
* * *   * * *
 * *     * * 
* *       * *
 *         * 
*           *
"""