def Ve():
    import turtle
    shapeInput = input('Circle or Square, what is your favorite shape?: ')
    if shapeInput == 'circle' or shapeInput == 'square':
        mau = input("what color will it be? yellow or blue or red? ")
        if mau == 'yellow' or mau=='blue' or mau=='red':
            turtle.Screen().bgcolor('black')
            turtle.Screen().title('your shape')
            turtle.Turtle().shape(shapeInput)
            turtle.Turtle().color(mau)
            turtle.done()
            
        else:
            print("SR,i dont have this color")
    else:
        print("SR, i dont have this shape")
if __name__ == "__main__":
    Ve()
        
        
        
    