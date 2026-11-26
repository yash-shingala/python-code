# 1
def show_city():
    city = "Ahmedabad"
    print("City:", city)
show_city()


# 2.
school = "Swaminarayan University"
def show_school():
    print("School:", school)
show_school()


# 3
if True:
    number = 100
print("Number:", number)


# 4
for i in range(1, 6):
    print(i)
print("Loop variable after loop:", i)


# 5
# Scope: Scope defines where a variable can be accessed.
# Lifetime: Lifetime defines how long a variable exists in memory.


# 6.
value = 100
def test():
    value = 200
    print(value)
test()
print(value)

# Output:
# 200
# 100


# 7
clicks = 0
def click():
    global clicks
    clicks += 1
click()
click()
print("Total clicks:", clicks)

# Output: Total clicks: 2


# 8. 
name = "Asha"
def show():
    # print(name)  # Error
    name = "Ravi"
    print(name)
show()

# Explanation:
# Python considers name a local variable because
# we assign a value to it inside the function.
# Accessing it before assignment causes UnboundLocalError.


# 9
def outer():
    message = "Hello Python"
    def inner():
        print(message)
    inner()
outer()

# Output: Hello Python


# 10
def create_list():
    numbers = [10, 20, 30]
    return numbers
result = create_list()
print("Original List:", result)
result.append(40)
result[0] = 100
print("Modified List:", result)

# Output:
# Original List: [10, 20, 30]
# Modified List: [100, 20, 30, 40]



#11
def counter():
    count = 0
    def increament():
        nonlocal count
        count = count + 1
        return count
    return increament
my_counter = counter()
print(my_counter())
print(my_counter())
print(my_counter())




#12
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)
outer()
print(x)



#14
def outerfunction():
    name = "yash"
    def innerfunction():
        print(name)
    return innerfunction
y_function = outerfunction()
y_function()
