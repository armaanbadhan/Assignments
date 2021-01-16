"""Draw a flowchart that takes the score of a student as input and
displays the grade of the student as follows
○ score >= 90 receives A+
○ 90 > score >= 80 receives A
○ 80 > score >= 70 receives B+
○ 70 > score >= 60 receives B
○ 60 > score >= 50 receives C+
○ 50 > score >= 40 receives C
○ score < 40 receives D"""

score = int(input("Score:"))

if score >= 90:
    print("A+")
elif score >= 80:
    print("A")
elif score >= 70:
    print("B+")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C+")
elif score >= 40:
    print("C")
else:
    print("D")
