from turtle import *
speed(0)
color("red", "white")
pensize(width=2)
begin_fill()
for i in range(4):
    left(120)
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    forward(50)
    left(30)
end_fill()
mainloop()