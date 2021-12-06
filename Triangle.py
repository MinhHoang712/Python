def Triangle():
    import math 
    a=float(input("Nhập cạnh a: "))
    b=float(input("Nhập cạnh b: "))
    c=float(input("Nhập cạnh c: "))
    #Điều kiện:
    if a+b>c and a-b<c or a+c>b and a-c>b or b-c>a and c+b>a:   
        Perimeter = a+b+c
        Area = math.sqrt(Perimeter/2*(Perimeter/2-a)*(Perimeter/2-b)*(Perimeter/2-c))
        print("Chu vi tam giác là: " + str(Perimeter))
        print("Diện tích tam giác là: " + str(Area))
    else:
        print("Tam giác ko tồn tại")
if __name__ == "__main__":
    Triangle()