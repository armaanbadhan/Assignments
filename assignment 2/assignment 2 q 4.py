"""Draw a flowchart that takes an integer, the year as input and
displays “yes” if the year is a leap year and “no” otherwise.
Note : Please refer Wikipedia for the exact criteria to determine if
a given year is a leap year."""

year = int(input("Enter Year:"))

if year % 4 != 0:
    print("no")
else:
    if year % 100 == 0 and year % 400 != 0:
        print("no")
    else:
        print("yes")
