def BMI():
    weight = int(input('Nhập cân nặng: '))
    height = int(input('Nhập chiều cao: '))
    bmi=weight/(height**2)
    if bmi<16:
        print("Gầy cấp độ III")
    elif bmi<=16 and bmi<17:
        print("Gầy cấp độ II")
    elif bmi>=17 and bmi<=18.5:
        print("Gầy cấp độ I")
    elif bmi>18.5 and bmi<25:
        print("Bình thường")
    elif bmi>=25 and bmi<30:
        print("Thừa cân")
    elif bmi>=30 and bmi<35:
        print("Béo phì cấp đọ I")
    elif bmi>=35 and bmi<40:
        print("Béo phì cấp đọ II")
    elif bmi>=40:
        print("Bép phì cấp độ III")
if __name__ == "__main__":
    BMI()