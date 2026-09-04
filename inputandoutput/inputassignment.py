#1
name = input("Enter your name: ")
print(name)

#2
city = input("Enter your city: ")
print(f"Your city is {city}")

#3
name = input("Enter your name: ")
age = input("Enter your age: ")
print(name)
print(age)

#4
age = input("Enter your age: ")
print(type(age))

#5
value = input("Enter a value: ")
print(type(value))

#6
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(first_name, last_name)

#7
name = input("Enter your name: ")
city = input("Enter your city: ")
college = input("Enter your college: ")

print("Name:", name)
print("City:", city)
print("College:", college)


#8
name1, name2 = input("Enter two names: ").split()

print(name1)
print(name2)



#9
a, b = input().split()
print(a)
print(b)


#10
word1, word2, word3 = input("Enter three words: ").split()

print(word1)
print(word2)
print(word3)


#11
value = int("25")

print(value)
print(type(value))



#12
value = float("25.5")

print(value)
print(type(value))


#13
value = str(100)

print(value)
print(type(value))


#14
number = int(input("Enter an integer: "))

print(number)
print(type(number))


#15
number = float(input("Enter a floating-point number: "))

print(number)
print(type(number))


#16
a = input()
b = input()

print(a + b)


#17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)


#18
name = "Rahul"
age = 20

print(f"My name is {name} and I am {age} years old.")



#19
a = 10
b = 20

print(f"The sum is {a + b}")



#20
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")



#21
price = float(input("Enter the price: "))

print(f"Price: {price:.2f}")


#22
price = 99.5

print(f"{price:.2f}")



#23
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")



#24
print("A", "B", "C")



#25
print("2026", "08", "19", sep="-")



#26
print("Hello", end=" ")
print("World")


#27
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

sum_value = first + second

print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {sum_value}")




#28
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")




#29
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")




#30
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
height = float(input("Enter student's height: "))
city = input("Enter student's city: ")

print("\n--- Student Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")