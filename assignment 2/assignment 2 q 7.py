"""Draw a flowchart for the color of light to be displayed at a traffic
signal, by reading as input the current time t, the signal
switching time s and transition time u . Assume that
● The color at t = 0 is red
(remains red from t = 0 to s − 1 )
● After s seconds (i.e. at t = s ) color changes to yellow
(remains yellow from t = s to s + u − 1 )
● After another u seconds (i.e. at t = s + u ) the color
changes to green
(remains green from t = s + u to 2s + u − 1 )
● After another s seconds (i.e. at t = 2s + u ) the color
changes to yellow
(remains yellow from t = 2s + u to 2s + 2u − 1 )
● After another u seconds (i.e. at t = 2s + 2u ) the color
changes back to red , which is displayed for s seconds and
the cycle continues
(remains red from t = 2s + 2u to 3s + 2u − 1 )
Note that red and green are displayed for s seconds, and yellow
for u seconds.
Assume all input variables t, s, u are positive integers .
Print the color to be displayed at the end."""

t = int(input("Time:"))

s = int(input("Switching time:"))
u = int(input("Transition time:"))
t = int(input("Time:"))

t = t % (2*s + 2*u)

if t < s:
        print("red")
elif s + u <= t < 2*s + u:
        print("green")
else:
        print("yellow")
