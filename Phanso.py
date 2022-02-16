class Phanso:
    tuso =0
    mauso=1
    def __init__(self,tuso,mauso):
        self.tuso = tuso 
        self.mauso = mauso
        if self.mauso == 0:
            self._del_()
        pass
    def _del_(self):
        print("Chuẩn bị xóa đối tượng")
    def add(a,b,c,d):
        obj1 = Phanso(a,b)
        obj2 = Phanso(c,d)
        result = Phanso(0,1)
        if obj2.mauso == obj1.mauso:
            result.mauso = obj2.mauso
            result.tuso = obj1.tuso + obj2.tuso
            print(result.tuso/result.mauso)
        else:
            result.mauso = obj1.mauso * obj2.mauso
            result.tuso = obj1.tuso*obj2.mauso + obj2.tuso*obj1.mauso
            print(result.tuso/result.mauso)
       
            
        