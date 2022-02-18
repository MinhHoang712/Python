from re import S
from sinhvien import sinhvien 
class Student_List:
    def __init__(self, student_db: list):
        self.student_db = student_db 
    def display(self):
        for _ in student_db:
            _.show()
    def addFresher(self,sinhvien_new: sinhvien):
        (self.student_db).append(sinhvien_new)
    def updateFresher(self,id_find: int):
        id = int(input("Nhập id: "))
        ten = str(input("Nhập tên sinh viên: "))
        date = str(input("Nhập ngày sinh: "))
        lop = str(input("Nhập lớp: "))
        khoa = str(input("Nhâp khoa"))
        sinhvien_new = sinhvien(id,ten,date,lop,khoa)
        for _ in self.student_db:
            if _.id == id_find:
                print("Cập nhật lại thông tin sinh viên có mã sinh viên {}".format(_.id))
                (self.student_db).pop(_)
                (self.student_db).append(sinhvien_new)
    def removeFresher(self,id_find):
        for _ in (self.student_db):
            if sinhvien.id == id_find:
                (self.student_db).remove(_)
    def searchFresher(self,name_find):
         for _ in (self.student_db):
                if sinhvien.name == name_find:
                    _.show()
    def sortFresher(self):
        (self.student_db).sort(reverse=True)
if __name__=="__main__":
    student_db = [sinhvien(132965,'Đặng Hoàng Minh','07/12/2002','65IT3','CNTT'),
              sinhvien(123112,'Đặng Hoàng Vũ',"07/12/2002",'65IT3','CNTT'),
              sinhvien(12311,'Long','12/12/2002','65IT3','CNTT')]
    list = Student_List(student_db)
    while True:
        option = int(input("Nhập lựa chọn: "))
        if option ==1:
            list.display()
        elif option ==2:
            id = int(input("Nhập id: "))
            ten = str(input("Nhập tên sinh viên: "))
            date = str(input("Nhập ngày sinh: "))
            lop = str(input("Nhập lớp: "))
            khoa = str(input("Nhâp khoa"))
            sinhvien_new = sinhvien(id,ten,date,lop,khoa)
            list.addFresher(sinhvien_new)
            list.display()
        elif option==3:
            id_find=int(input("Nhập id sinh viên cần cập nhật: "))
            list.updateFresher(id_find)
            list.display()
        elif option==4:
            name_find = str(input("Nhập tên sinh viên tìm kiếm: "))
            list.searchFresher(name_find)
        elif option==5:
            id_remove = int(input("Nhập id sinh viên cần xóa"))
            list.removeFresher(id_remove)
        elif option==6:
            list.sortFresher()
        elif option ==7:
            break
        else:
            print("Error")

     