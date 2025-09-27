

from operator import attrgetter

class Employee:
    def __init__(self , name , age , salary ):
        self.name = name
        self.age = age
        self.salary = salary


    def __repr__(self):
        return f"{self.name} is  {self.age} years old "





e1 = Employee("ash" , 21 , 70)
e2 = Employee("rey" , 28 , 70)
e3 = Employee("maxo" , 29 , 69)

def sort_key(obj):
    return obj.name

employees = [e1,e2,e3]

new_list = sorted(employees , key=attrgetter('salary'))
print(new_list)





