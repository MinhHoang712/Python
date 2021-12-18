start = int(input("Nhập điểm bắt đầu: "))
end = int(input("Nhập điểm kết thúc: "))
if end<start:
    print('End phải lớn hơn Start')
else: 
    for i in range(start,end+1):
        if i %3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        elif i%3==0 and i%5==0:
            print('FizzBuzz')
        else:
            print(i)
