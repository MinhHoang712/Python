def min_in_array(list):
    min = list[0]
    for num in list:
        if num<min:
            min = num
    print(min)
if __name__ == "__main__":
    n = int(input("Nhập số phần tử trong mảng: "))
    list = []
    for i in range(n):
        list.append(int(input('Nhập phần tử mảng=: ')))
    min_in_array(list)