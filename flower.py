from turtle import *


t = Turtle()

bgcolor("black")
t.pencolor("purple")
t.speed(0)
for i in range(320):
    t.circle(290 - i, 90)
    t.left(90)
    t.circle(290 - i, 90)
    t.left(10)
    if i > 90:
        t.pensize(3)
mainloop()


