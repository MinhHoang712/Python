def picture():
    
    import turtle 
    turtle.bgcolor("light blue")

    t=turtle.Turtle() 
    t.penup()
    t.goto(-250,-150)
    t.pendown()
    #mặt trc
    t.fillcolor("blue")
    t.begin_fill()
    a=100 #độ dài tường
    for i in range(5):
        t.fd(a)
        t.rt(90)
    t.end_fill()
    #mặt bên
    t.fillcolor("yellow")
    t.begin_fill()
    t.left(a)
    t.fd(130)
    t.right(100)
    t.fd(a)
    t.right(80)
    t.fd(130)
    t.end_fill()

    t.rt(100)
    t.fd(a)
    #mái trc
    t.fillcolor("pink")
    t.begin_fill()
    t.left(30)
    t.fd(a)
    t.left(120)
    t.fd(a)
    t.end_fill()

    t.fd(-a)
    t.left(180)
    #mái bên
    t.fillcolor("orange")
    t.begin_fill()
    t.right(50)
    t.fd(130)
    t.right(70)
    t.fd(a)
    t.right(110)
    t.fd(130)
    t.end_fill()
    t.left(80)
    t.fd(a)
    # cửa
    t.right(90)
    t.fd(25)
    t.right(90)
    t.fillcolor("green")
    t.begin_fill()
    b=a/2 #độ dài cửa
    for i in range(3):
        t.fd(b)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(-140,-170)
    t.pendown()
    #cửa sổ
    t.fillcolor("brown")
    t.begin_fill()
    c=b/2 # độ dài cửa sổ
    t.left(10)
    t.fd(c)
    t.right(100)
    t.fd(c)
    t.right(80)
    t.fd(c)
    t.right(100)
    t.fd(c)
    t.end_fill()
    

    t.penup()
    t.goto(200,-250)
    t.pendown()
    #cây
    t.fillcolor("brown")
    t.begin_fill()
    for i in range (2):
        t.fd(50)
        t.right(90)
        t.fd(25)
        t.right(90)
    t.end_fill()
    t.right(90)
    t.fd(25)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(62.5)
    t.fillcolor("green")
    
    for i in range(2):
        t.begin_fill()
        for i in range(4):
            t.right(120)
            t.fd(112.5)
        t.end_fill()
        t.left(120)
        t.fd(62.5)
    t.fillcolor("green")
    t.begin_fill()
    for i in range(4):  
        t.right(120)
        t.fd(112.5)
    t.end_fill()
    
    #mặt trời
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.goto(200,200)
    
    t.penup()
    t.goto(100,300)
    t.pendown()
    t.goto(100,100)
    
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.goto(200,100)
    
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.goto(200,300)
    
    t.penup()
    t.goto(135,170)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    turtle.done()
    
if __name__ == "__main__":
    picture()