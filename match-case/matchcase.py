# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))

# i=1
# while i>=1:
#     operation=input("Enter an operation (+, -, *, /): ")

#     match operation:
#         case "+":
#             print(a + b)
#         case "-":
#             print(a - b)
#         case "*":
#             print(a * b)
#         case "/":
#             if b==0:
#                print("Division by zero is not allowed")
#             else: 
#                print(a / b)
#         case _:
#             print("Invalid operation")
#             break

#     i+=1


#or
# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))

# flag=True
# while flag:
#     operation=input("Enter an operation (+, -, *, /): ")

#     match operation:
#         case "+":
#             print(a + b)
#         case "-":
#             print(a - b)
#         case "*":
#             print(a * b)
#         case "/":
#             if b==0:
#                print("Division by zero is not allowed")
#             else: 
#                print(a / b)
#         case _:
#             print("Invalid operation")
#             flag=False


# num=int(input("Enter a number: "))

# flag=True
# while flag:
#     operation=input("Enter an operation (even,odd,prime): ")

#     match operation:
#         case "even":
#             if num%2==0:
#                 print(f"{num} is even")
#             else:
#                 print(f"{num} is not even")
#         case "odd":
#             if num%2!=0:
#                 print(f"{num} is odd")
#             else:
#                 print(f"{num} is not odd")
#         case "prime":
#             if num>1:
#                 for i in range(2,num):
#                     if num%i==0:
#                         print(f"{num} is not prime")
#                         break
#                 else:
#                     print(f"{num} is prime")
#             else:
#                 print(f"{num} is not prime")
#         case _:
#             print("Invalid operation")
#             flag=False




# day = 6

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid Day")



# marks = 74

# match marks:
#     case y if y >= 90:
#         print("A")
#     case x if x >= 75:
#         print("B")
#     case zq if zq >= 60:
#         print("C")
#     case n if n >= 40:
#         print("D")
#     case _:
#         print("Fail")


# account = "student"
# choice = 2

# match account:

#     case "student":

#         match choice:
#             case 1:
#                 print("View Courses")
#             case 2:
#                 print("View Marks")
#             case 3:
#                 print("View Attendance")
#             case _:
#                 print("Invalid Choice")

#     case "teacher":

#         match choice:
#             case 1:
#                 print("View Students")
#             case 2:
#                 print("Enter Marks")
#             case _:
#                 print("Invalid Choice")

#     case _:
#         print("Invalid Account Type")



# customer_type = "premium"
# purchase_amount = 1200
# total_amount = 0
# match customer_type:
#     case "regular":
#         print("Discount: 5%")
#         total_amount = purchase_amount - (purchase_amount * 0.05)
#     case "premium":
#         match purchase_amount:
#             case amount if amount >= 1000:
#                 print("Discount: 20%")
#                 total_amount = purchase_amount - (purchase_amount * 0.20)
#             case amount if amount >= 500:
#                 print("Discount: 10%")
#                 total_amount = purchase_amount - (purchase_amount * 0.10)
#             case _:
#                 print("No Discount")  
#                 total_amount = purchase_amount
#     case _:
#         print("Invalid Customer Type")
#         total_amount = purchase_amount    

# print(f"Total Amount to be paid: {total_amount}")









