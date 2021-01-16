"""Draw a flowchart that takes the perimeter and area of a rectangle
as input and displays whether such a rectangle exists or not.
Assume that the perimeter and area taken from input are
positive real numbers. (Note: You should use only the operators
that you have learned, i.e. +, -, *, /, //, **, and , or , not and xor )."""

area = float(input("area:"))
perimeter = float(input("perimeter:"))

if perimeter**2 >= 8*area:
    print("exists")
else:
    print("doesnt exist")
