import turtle
t=turtle.Turtle()
t.speed(0)
_ = 0
while _ <6:
    for color in ('red','green','yellow','brown','sky blue','dark blue'):
        t.color(color)
        count=0
        while count<2:
            t.circle(100,90)
            t.circle(50,90)
            count+=1
        t.right(10)
    _ +=1
    
turtle.done()