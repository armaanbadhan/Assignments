"""Draw a flowchart that takes the attendance of three people as
input (input will be 0 if they were absent and 1 if present) and
displays whether all of them attended the class or not. Assume
that the two values taken from input are always either 0 or 1."""

a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))

if a == 1 and b == 1 and c == 1:
    print("all present")
else:
    print("Absent")
