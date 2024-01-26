# print("Hello world")

# a="Hello world"
# print("Hello world")

# print(a[1])
# print(a[4])

# for x in "banana":
#     print(x)

# a = "Hello world"
# print(len(a))

# txt = "The best things in life are free"
# print("free" in txt)

# txt = "The best things in life are free"
# print("Expensive"  not in txt)

# a =" Hello world"
# print(a.upper())
# print(a.lower())
# print(a.strip())

# print(a.replace("H", "J"))
# print(a.split())
# print(a.split(","))


# quantity = 3
# itemo = 567
# price = 49.95
# myorder = "I want {} peice of item {} for {} dollars"
# print(myorder.format(quantity, itemo, price))

# myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}"
# print(myorder2.format(quantity, itemo, price))

# print(bool("hello"))
# print(bool(15))


# x = "World"
# y = 30
# print(bool(x))
# print(bool(y))


# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# print(thislist[1])
# print(len(thislist))



# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Yes, apple is an th fruits list")


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(thislist1)
# thislist1[1:3] = ["blackcurrant", "watermelon"]
# print(thislist1)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist1 = ["mango", "pineaple", "papaya"]
# thislist.extend(thislist1)
# print(thislist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)

# thislist1 = [100, 50, 65, 82, 23]
# thislist1.sort()
# print(thislist1)
# thislist1.sort(reverse=True)
# print(thislist1)

# def myfunc(n):
#     return abs( n - 50)

# thislist1.sort(key = myfunc)
# print(thislist1)



# thsidict = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year" : 1964
# }

# print(thsidict)
# print(thsidict["brand"])

# thsidict1 = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year" : 1964,
#     "year" : 2020
# }

# print(thsidict1)
# print(len(thsidict1))

# x = thsidict1["model"]
# print(x)

# y = thsidict1.get("model")
# print(y)

# z = thsidict1.keys()
# print(z)

# values = thsidict1.values()
# print(values)


# car = {
#     "brand" : "ford",
#     "model" : "mustang",
#     "year" : 1964
# }

# x =car.keys()
# print(x)

# car["color"] = "white"
# print(car)

# y = car.items()
# print(y)


# thisdict = {
#     "brand" : "ford",
#     "model" : "mustang",
#     "year" : 1964
# }
# thisdict["year"] = 2018
# print(thisdict)
# thisdict.update({"year" : 2020})
# print(thisdict)


# def my_function():
#     print("Hello from a function")

# my_function()

# def my_function(name):
#     print(name + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("linus")


# def my_function(fname, lname):
#     print(fname+ " "+ lname)
# my_function("Emil", "Refsnes")


# def my_function(*kids):
#     print("The youngest chils is "+ kids[2])
# my_function("Emil", "Tobias", "linus")


# def my_function(country = "Norway"):
#     print("I am from " + country)

# my_function("sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# class Myclass:
#     x=5
    
# p1 = Myclass()
# print(p1.x)



# class person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
    
# p1 = person("john", 36)

# print(p1.name)
# print(p1.age)
# print(p1)

# class person:
#     def __init__(self, fname, lname) :
#         self.firstname = fname
#         self.lastname = lname

#     def my_function(self):
#         print(self.firstname, self.lastname)

# x = person("John", "Doe")
# x.my_function()


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x

# Myclass = MyNumbers()
# myiter = iter(Myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class car:
#     def __init__(self, brand, model) :
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Drive!")
    
# class Boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
#     def move(self):
#         print("sail!")

    
# class plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
#     def move(self):
#         print("Fly!")

# car1 = car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = plane("Boeing", "747")

# for x in (car1, boat1, plane1):
#     x.move()

# import platform
# x= platform.system()
# print(x)

# y = dir(platform)
# print(y)

# import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))

# y = datetime.datetime(2020, 5, 17)
# print(y)
# print(y.strftime("%B"))

# x = min(5,10,25)
# y = max(5,10,25)
# print(x)
# print(y)

# x = abs(-5.45)
# print(x)
# import math

# x = math.pi
# print(x)


# import json
# x = '{"name": "John", "age": "30", "city": "New York"}'

# y = json.loads(x)
# print(y)
# print(y["age"])

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple","banans"]))
# print(json.dumps(("apple", "apple")))
# print(json.dumps("hello"))
# print(json.dumps(43))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json

# x ={
#     "name" : "john",
#     "age" : 30,
#     "married" : True,
#     "divorced" : False,
#     "children" : ("Ann","Billy"),
#     "pets" : None,
#     "cars" :[
#         {"model" : "BMW 230", "mpg": 27.5},
#         {"model" : "Ford Edge", "mpg": 24.1}
#     ]
# }
# print(json.dumps(x))
# print(json.dumps(x, indent=9))
# print(json.dumps(x, indent=3, separators=(".","=")))


# import re
# txt = "The rain in Spain"
# x = re.search("^The. *Spain$", txt)
# print(x)



