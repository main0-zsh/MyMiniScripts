from turtle import*
penup()
goto(-300,-300)
pendown()

def sky():
    color('cyan')
    begin_fill()
    for i in range(4):
        forward(600)
        left(90)
    end_fill()
sky()

penup()
goto(195, 180)
pendown()
def sun():
    color('yellow')
    begin_fill()
    circle(50)
    end_fill()
sun()

penup()
goto(-300,-300)
pendown()

def earth():
    color('green')
    begin_fill()
    for i in range(2):
        forward(600)
        left(90)
        forward(200)
        left(90)
    end_fill()
earth()


penup()
goto(-195, 180)
pendown()

def cloud():
    color('white')
    penup()
    goto(-195, 180)
    pendown()
    begin_fill()
    circle(40)
    end_fill()
    penup()
    goto(-135, 180)
    pendown()
    begin_fill()
    circle(40)
    end_fill()
    penup()
    goto(-75, 180)
    pendown()
    begin_fill()
    circle(40)
    end_fill()
cloud()

exitonclick()