#tính kế thừa:
class Person(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id 
    def display(self):
        print(self.name)
        print(self.id)
    
class Employee(Person):
    def __init__(self, name, id,salary,post):
        self.salary = salary
        self.post = post 
        Person.__init__(self,name,id)
    def display(self):
        print(self.salary)
        print(self.post)
        Person.display(self)
if __name__ ==  "__main__":
    emp = Person("Hoang",1) 
    emp.display()
    a = Employee("Diệt",2,6000,'FRESHER')
    a.display()
        