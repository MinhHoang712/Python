def draw():
    import turtle
    t=turtle.Turtle()
    limit=float(input("Nhập giới hạn xoắn: "))
    d=10
    t.speed(0)
    t.home()
    a=t.position()
    while t.distance(a)<limit:
        t.circle(d,50)
        d+=1
    turtle.done()
if __name__ == "__main__":
    draw()
        