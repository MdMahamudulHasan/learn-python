# print("Python")
# python = int(input("Enter your number: "))
# print(python)



# --------------------------------------------------PYTHON INHERITANCE---------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

"""
class person:
    def __init__(self, fname, lname):
        self.firstname  = fname
        self.lastname = lname
        
    
    def printname(self):
        print(self.firstname,self.lastname)
        

x=person("john", "Doe")
x.printname()

y =person("Munna","Babu")
y.printname()

"""







"""
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, fname, lname):
        person.__init__(self,fname, lname)
        

x = student("Khanna","Babu")
x.printname()

"""






"""
class person:
    def __init__(self,  fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printName(self):
        print(self.firstname, self.lastname)
    
    
def student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x= person("Sakib", "Hossain")
x.printName()

"""






"""
class Person:
    def __init__(self, fname, lname):
        self.firstName= fname
        self.lastName= lname
    
    def printName(self):
        print(self.firstName, self.lastName)

class student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear = 2026
        

x = student("Munna", "babu")
x.printName()
print(x.graduationYear)

"""




"""
class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    
    
    def printName(self):
        print(self.firstName, self.lastName)


class student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year


x = student("Munna", "Babu", 2026)
x.printName()
print(x.graduationYear)

"""





"""

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    
    
    def printName(self):
        print(self.firstName, self.lastName)


class student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year
    
    
    def welcome(self):
        print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)

x= student("Munna", "Babu", 2026)
x.printName()
print(x.graduationYear)
x.welcome()


"""


#--------------------------------------------------------Python POlymorphism----------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    
    def move(self):
        print("Move......")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail.....")

class Plane(Vehicle):
    def move(self):
        print("Fly........")

car1 = Car("Ford", "mustang")
boat1 = Boat("Ibiza", "Touring")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
    print("\n \n")
    
    

