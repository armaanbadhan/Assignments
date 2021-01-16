"""Draw a flowchart for finding the maximum of 4 numbers which
are obtained as input from the user. Print “maximum value =
<the maximum number>“ at the end."""

a = float(input("Enter number a:"))
b = float(input("Enter number b:"))
c = float(input("Enter number c:"))
d = float(input("Enter number d:"))

if a > b and a > c and a > d:
    print("Max value is:", a)
elif b > c and b > d:
    print("Max value is:", b)
elif c > d:
    print("Max value is:", c)
else:
    print("Max value is:", d)
