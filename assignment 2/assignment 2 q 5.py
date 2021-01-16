"""Draw a flowchart that takes the three angles of a triangle (in
degrees) as input and prints whether the triangle is acute,
right-angled, obtuse or invalid (i.e. a triangle with such angles
does not exist). Assume that the 3 numbers obtained from input
are positive real numbers."""
while True:
    a = float()
    b = float()
    c = float()
    while True:
        try:
            a = float(input("angle 1:"))
            b = float(input("angle 2:"))
            c = float(input("angle 3:"))
            break
        except ValueError:
            print("Enter float only")
            continue

    if a >= 180 or a <= 0:
        print("angle a invalid")
        continue
    if b >= 180 or b <= 0:
        print("angle b invalid")
        continue
    if c >= 180 or c <= 0:
        print("angle c invalid")
        continue
    else:
        pass

    if a + b + c == 180:
        break
    else:
        print("sum not equal to 180")
        continue

if a < 90 and b < 90 and c < 90:
    print("Acute")
elif a == 90 or b == 90 or c == 90:
    print("right angled triangle")
else:
    print("Obtuse")
