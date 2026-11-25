# 1. 
def multiply_all(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(multiply_all(2, 3, 4))  # 24
print(multiply_all())         # 1


# 2. 
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_profile(name="Ravi", age=21, city="Surat")


# 3.
def make_message(name, /, *, greeting="Hello"):
    return greeting + " " + name

print(make_message("Ravi"))
print(make_message("Ravi", greeting="Hi"))

# Invalid calls:
# make_message(name="Ravi")  # name must be positional
# make_message("Ravi", "Hi") # greeting must be keyword


# 4. 
def add_three(a, b, c):
    return a + b + c

values = [4, 5, 6]
print(add_three(*values))  # 15


# 5. 
def show_person(name, age):
    print("Name:", name)
    print("Age:", age)

person = {"name": "Ravi", "age": 21}
show_person(**person)


# 6. 
def square(number):
    return number * number

print(square(5))


# 7. 
def rectangle_area(length: float, width: float) -> float:
    return length * width

print(rectangle_area(5.0, 3.0))  # 15.0


# 8. 
def double(number: int) -> int:
    return number * 2

print(double("Hi"))  # HiHi
# Python does not automatically enforce type hints.


# 9.
def greet(name):
    print("Hello", name)

# greet("Ravi", name="Amit")
# TypeError: name receives multiple values.


# 10
def display(*args):
    print(args)

values = [10, 20, 30]
display(*values)  # Output: (10, 20, 30)

# *args collects arguments into a tuple.
# *values unpacks a list or tuple into separate arguments.