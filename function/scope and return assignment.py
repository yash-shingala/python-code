# # Beginner

# # 1. 
# def welcome():
#     print("Welcome to Python")

# welcome()
# welcome()
# welcome()

# # 2. 
# def greet(name):
#     print("Hello", name)

# greet("Yash")

# # 3. 
# def show_number(number):
#     print(number)

# show_number(10)

# # 4.
# def add(a, b):
#     return a + b

# print(add(5, 3))

# # 5.
# def square(number):
#     return number * number

# print(square(4))

# # 6.
# def is_even(number):
#     return number % 2 == 0

# print(is_even(6))

# # 7.
# def get_full_name(first_name, last_name):
#     return first_name + " " + last_name

# print(get_full_name("Yash", "Shingala"))

# # 8.
# def introduce(name, city="Pune"):
#     print(name, "lives in", city)

# introduce("Yash")
# introduce("Yash", "Surat")

# # 9.
# def subtract(a, b):
#     return a - b

# print(subtract(10, 5))  # 5
# print(subtract(5, 10))  # -5

# # 10. 
# def get_min_max(a, b):
#     return min(a, b), max(a, b)

# print(get_min_max(10, 5))


# # Intermediate

# # 11. 
# def calculate(a, b):
#     return a + b, a - b, a * b, a / b

# print(calculate(10, 2))

# # 12. 
# def count_digits(number):
#     if number == 0:
#         return 1
#     count = 0
#     while number > 0:
#         count += 1
#         number //= 10
#     return count

# print(count_digits(12345))

# # 13. 
# def classify_number(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"

# print(classify_number(-5))

# # 14. 
# def calculate_total(price, quantity=1):
#     return price * quantity

# print(calculate_total(50, 3))
# print(calculate_total(50))

# # 15.
# def create_email(username, domain="example.com"):
#     return username + "@" + domain

# print(create_email("yash"))
# print(create_email("yash", "gmail.com"))

# # 16. 
# def format_name(first, last, uppercase=False):
#     name = first + " " + last
#     if uppercase:
#         return name.upper()
#     return name

# print(format_name("Yash", "Shingala"))
# print(format_name("Yash", "Shingala", True))

# # 17. 
# def percentage(marks, total=100):
#     return marks / total * 100

# print(percentage(450, 500))

# # 18.
# def convert_minutes(minutes, seconds_per_minute=60):
#     return minutes * seconds_per_minute

# print(convert_minutes(5))

# # 19. 
# def student_details(name, age, city):
#     print(name, age, city)

# student_details(city="Surat", name="Yash", age=18)

# # 20. 
# def bill(item, quantity=1, price=100):
#     return quantity * price

# print(bill("Pen", 3, 10))                 
# print(bill("Book", price=50, quantity=2)) 
# print(bill("Pencil"))                    



# def compare(a,b):
#     if a>b:
#         return "a is greater", a-b
#     elif b>a:
#         return "b is greater", b-a
#     else:
#         return "equal", a-b
# print(compare(5,10))
    

# def analyze_number(a):
#     if int(a)<0:
#         absolute=-int(a)
#     else:
#         absolute=int(a)
#     count=0
#     for i in range(0,len(a)):
#         count+=1
#     if absolute%2==0:
#         return absolute,"even",count
# b=input("enter a number")
# print(analyze_number(b))

# c=1
# def factorial(b):
#     global c
    
#     if b == 0 or b == 1:
#         return c
#     c*=b
#     b-=1
#     return factorial(b)
# b=int(input("enter a number:"))
# print(factorial(b))




# # 21. 
# def analyze_number(number):
#     absolute = number if number >= 0 else -number
#     even = number % 2 == 0
#     digits = len(str(absolute))
#     return absolute, even, digits

# print(analyze_number(-246))


# # 22. 
# def calculate_stats(a, b, c):
#     return min(a, b, c), max(a, b, c), a + b + c

# print(calculate_stats(10, 20, 5))


# # 23. 
# def make_sentence(subject, verb, object):
#     return subject + " " + verb + " " + object

# print(make_sentence(object="Python", subject="I", verb="love"))


# # 24.
# def apply_discount(price, discount=0):
#     return price - (price * discount / 100)

# print(apply_discount(1000, 20))


# # 25. 
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus

# print(calculate_pay(8))
# print(calculate_pay(8, 300))
# print(calculate_pay(8, bonus=500))
# print(calculate_pay(8, rate=250, bonus=500))


# # 26.
# def get_coordinates(x=0, y=0):
#     return x, y

# print(get_coordinates())
# print(get_coordinates(x=5))
# print(get_coordinates(y=10))


# # 27.
# def compare(a, b):
#     difference = a - b if a >= b else b - a

#     if a > b:
#         return "A is greater", difference
#     elif b > a:
#         return "B is greater", difference
#     else:
#         return "Equal", difference

# print(compare(10, 5))
# print(compare(4, 9))
# print(compare(7, 7))


# # 28. 
# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9 / 5) + 32
#     else:
#         return (value - 32) * 5 / 9

# print(convert_temperature(25))
# print(convert_temperature(98.6, "F"))


# # 29.
# def calculate_result(marks, passing_marks=35):
#     if marks >= passing_marks:
#         return "Pass"
#     else:
#         return "Fail"

# print(calculate_result(75))
# print(calculate_result(30))


# # 30.
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return quantity * price + delivery_fee

# print(order_summary("Pen"))
# print(order_summary("Book", quantity=3, price=50))
# print(order_summary("Pen", delivery_fee=10))




# def find_word_manual(main_string, target_word):
#     main_len = 0
#     for i in main_string:
#         main_len += 1
        
#     target_len = 0
#     for j in target_word:
#         target_len += 1

#     if target_len > main_len:
#         return -1

#     for i in range((main_len - target_len) + 1):
#         match = True
#         for j in range(target_len):
#             if main_string[i + j] != target_word[j]:
#                 match = False
#                 break 
#         if match:
#             return i
#     return -1

# text = "hello world, welcome to python"
# word_to_find = "welcome"
# index = find_word_manual(text, word_to_find)

# if index != -1:
#     print(f"Word found! It starts at index: {index}")
# else:
#     print("Word not found.")


# def divide(c,/,*args,d=20,**kwargs):
#     return args,kwargs,c+d
# print(divide(14,15,2,32,52,c=23,p=67))



# text = input("Enter a string: ")

# for i in range(len(text)):
#     frequency = 0
#     already_counted = False

#     for j in range(i):
#         if text[i] == text[j]:
#             already_counted = True
#             break

#     if already_counted == False:
#         for j in range(len(text)):
#             if text[i] == text[j]:
#                 frequency += 1

#         print(text[i], "=", frequency)




