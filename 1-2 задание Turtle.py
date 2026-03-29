from turtle import*
penup()
goto(100,0)
pendown()
color('purple')
pensize(15)
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()

penup()
goto(-100,0)
pendown()

def пятиугольник():
    begin_fill()
    for i in range(5):
       forward(70)
       left(72)
    end_fill()

пятиугольник()
exitonclick()