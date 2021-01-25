n = int(input())

print("*"*n)
for row in range(1, n - 1):
    q = (abs(row - int((n-1)/2)) + 1)
    print("*"*q + " "*(2*(abs((q - (int((n+1)/2))))) - 1) + "*"*q)
print("*"*n)
