import turtle as t
import random
import time
# Tạo và quy định dài rộng của đường đua
# và các tham số
screen = t.Screen()
screen.setup(height=500, width=600)
# Hiển thị cửa sổ cho phép người dùng đoán
# con rùa màu nào thắng cuộc
guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")
# List lưu lại màu của các con rùa
colors = ["red", "brown", "blue", "green", "orange", "pink"]
# Vị trí ban đầu theo trục y của các con rùa
# Theo trục x = -250, cách vị trí 0,0 250 về bên trái
y_position = [0, -30, 30, -60, 60, 90]
# List lưu lại vận tốc của các con rùa
# các giá trị này sẽ được chọn một cách ngẫu nhiên
# cho các con rùa khi chạy
turtle_speed = [10, 15, 20, 25, 30, 5]

# Tạo một list để lưu các con rùa
all_turtles = []
run = True
start =time.time()
# Xây dựng hàm để tạo và thiết đặt vị trí ban
# đầu, màu cho các con rùa và lưu vào list
for turtle in range(0, 6):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    # Di chuyển rùa về vị trí ban đầu,
    # bên trái cùng của đường đua
    turtles.goto(x=-250, y=y_position[turtle])
    # Màu của rùa
    turtles.color(colors[turtle])
    # Lưu vào list
    all_turtles.append(turtles)
    # Tạo khung cảnh và vẽ các cột mốc bên trái đường đua
screen = t.Screen()
screen.setup(height=500, width=600)
pen = t.Turtle(visible=False)
pen.penup()
pen.speed(0)
pen.goto(-250, 200)
for i in range(21):
    pen.write(i)
    pen.forward(25)

# Vẽ các đường đứt đoạn trên đường đua và
# đánh dấu các cột mốc bên phải đường đua
x = -250
pen.goto(-250, 200)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(10)
    pen.penup()
    pen.forward(5)
    pen.write(i)
    pen.goto(x + (i + 1) * 25, 200)
# Xây dựng hàm di chuyển về đích của
# mỗi con rùa, khoảng cách di chuyển được
# chọn ngẫu nhiên trong các giá trị
# được lưu trong list phía trên
def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(turtle_speed))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False
            print("Con rùa {} đã chiến thắng với thành tích {}s".format(turtle.pencolor(),time.time()-start))
        
while run:
    random_walk(all_turtles)

# Chương trình kết thúc khi click
# chuột lên màn hình
screen.exitonclick()