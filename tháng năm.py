def month(i):
    switcher = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: "June",
        7: 'July',
        8: "August",
        9: "September",
        10: 'October',
        11: 'November',
        12: 'December',
    }
    return switcher.get(i,"Invalid month")
def season(i):
    switcher  = {
        1: 'sqring',
        2: 'summer',
        3: "autumn",
        4: 'winter' ,   
    }
    return switcher.get(i,"Invalid season")
def monthtoseason(i):
    _ = 0
    if i in range(1,4):
        _=1
    elif i in range(4,7):
        _=2
    elif i in range(7,10):
        _=3
    elif i in range(10,13):
        _=4
    return _
if __name__ == "__main__":
    monthInput= int(input("Nhập tháng: "))
    print("Tháng vừa nhập là: {} thuộc mùa {}".format(month(monthInput),season(monthtoseason(monthInput))))

    
