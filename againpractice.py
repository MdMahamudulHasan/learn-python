'''

print("Hello World")


if (5>2):
    print("Five is greater than two")
    

if(5>2):
    print("Two is less then five")
    

#This is a comment
print ("This is a comment.")

print("Comment") #this is a comment 


x = 4 
x = "Sally"

print(x)
print(type(x))


x = str(3+3)
y = int(3.1416)
z = float(5)

print(x)
print(y)
print(z)


print(type(x))
print(type(y))
print(type(z))

myVariableName = "john" #Camel Case
MyVariableName = "John" #Pascal Case
my_variable_name = "John" #Snake Case

x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''

# fruits ={"apple", "banana", "cherry"}
# x,y,z = fruits
# print(x)
# print(y)

# """"
# cout << "Enter the number";
# cin >> n;

# """

# NUmber2 = float(input("Enter the number"))

# Number1 = int(input("Enter the number"))



# --------------------------------------------------------------Array-------------------------------
"""
my_string = "Hello"
print(my_string[0])
# Index count on every character
print(my_string)

my_array = ["Hello", "World", "I", "am", "Durjoy"]
print(my_array[0])
# index count on every string


"""


cars = ["BMW", "Ford", "Volvo"]
print(cars)

for x in cars: 
    print(x)   

print(cars[0])
print(cars[2])

print(len(cars))


# Delete method for any index ,,,pop(), remove()

cars.pop(1) # pop use on index
print(cars)
# cars = ["BMW", "Volvo"]
cars.remove("Volvo") # remove use on value
print(cars)


cars.clear() # remove all element
print(cars)



cars = ["BMW", "Volvo", "Ford"]
cars.sort() # sort work on every string first character
print(cars)

numbers = [ 3, 6, 7,  9, 10, 4, 5, 1, 2, 8,]

print(numbers)

for x in numbers:
    print(x)


print("length:",len(numbers))

numbers.pop(4)
print(numbers)


numbers.remove(4)
print(numbers)

numbers.sort()
print(numbers)

numbers.clear()
print(numbers)

numbers.append(10)
print(numbers)