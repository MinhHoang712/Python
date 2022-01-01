def sortArray(num1,num2,num3):
    list = []
    list.append(num1)
    list.append(num2)
    list.append(num3)
    sorted(list,reverse=False)
    print(sorted(list,reverse=False))
if __name__ == '__main__':
    num1 = int(input("Nhập 3 số nguyên: "))
    num2 = int(input("Nhập 3 số nguyên: "))
    num3 = int(input("Nhập 3 số nguyên: "))
    sortArray(num1,num2,num3)
        