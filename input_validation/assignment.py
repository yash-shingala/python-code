# Q1.
# marks = int(input("Enter marks (0-100): "))
# while marks < 0 or marks > 100:
#     print("Invalid marks!")
#     marks = int(input("Enter marks (0-100): "))
# print("Accepted marks:", marks)



# Q2.
# n = int(input("Enter a positive integer: "))
# while n <= 0:
#     n = int(input("Invalid! Enter a positive integer: "))
# print("Accepted:", n)



# Q3. 
# age = int(input("Enter age: "))
# while age < 0 or age > 120:
#     age = int(input("Invalid age! Enter again: "))
# print("Accepted age:", age)



# Q4.
# choice = 0
# while choice < 1 or choice > 4:
#     print("1. View profile\n2. Edit profile\n3. Settings\n4. Exit")
#     choice = int(input("Choose (1-4): "))
# print("Selected option:", choice)



# Q5
# password = input("Enter password: ")
# while len(password.strip()) < 8:
#     password = input("Password needs 8 characters: ")
# print("Password accepted!")



# Q6. 
# temp = float(input("Temperature (-20 to 45): "))
# while temp < -20 or temp > 45:
#     temp = float(input("Invalid! Enter temperature again: "))
# print("Accepted temperature:", temp)



# Q7.
# balance = 5000
# amount = float(input("Withdrawal amount: "))
# while amount <= 0 or amount > balance:
#     amount = float(input("Invalid amount! Enter again: "))
# balance -= amount
# print("Remaining balance:", balance)



# Q8. 
# username = input("Enter username: ").strip()
# while len(username) < 5 or " " in username:
#     username = input("Invalid! Enter username again: ").strip()
# print("Accepted username:", username)



# Q9. 
# n = int(input("Enter number: "))
# while n <= 0 or n % 3 != 0 or n % 5 != 0:
#     n = int(input("Invalid! Enter a positive multiple of 15: "))
# print("Accepted:", n)



# Q10.
# secret_pin = 2468
# attempts = 0
# while attempts < 3:
#     pin = int(input("Enter PIN: "))
#     attempts += 1
#     if pin == secret_pin:
#         print("Access granted!")
#         break
# else:
#     print("Access denied!")



# Q11. 
# n = int(input("Enter number (10-50): "))
# while n < 10 or n > 50:
#     n = int(input("Invalid! Enter again: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")




# Q12. 
# balance = 2000
# amount = float(input("Deposit amount: "))
# while amount <= 0:
#     amount = float(input("Invalid! Enter a positive amount: "))
# balance += amount
# print("New balance:", balance)




# Q13. 
# n = int(input("Enter integer (1-100): "))
# while n < 1 or n > 100:
#     n = int(input("Invalid! Enter again: "))
# print("Accepted:", n)



# Q14.
# marks = int(input("Enter marks (0-100): "))
# while marks < 0 or marks > 100:
#     marks = int(input("Invalid marks! Enter again: "))
# if marks >= 75:
#     print("Distinction")
# elif marks >= 60:
#     print("First Class")
# elif marks >= 35:
#     print("Pass")
# else:
#     print("Fail")



# Q15. 
# username = input("Username: ").strip()
# password = input("Password: ")
# while (len(username) < 5 or " " in username
#        or len(password.strip()) < 8):
#     print("Invalid username or password!")
#     username = input("Username: ").strip()
#     password = input("Password: ")
# print("Login details accepted!")


# Q16.
# a = float(input("First number: "))
# op = input("Operator (+, -, *, /): ")
# while op not in ["+", "-", "*", "/"]:
#     op = input("Invalid operator! Enter again: ")
# b = float(input("Second number: "))
# while op == "/" and b == 0:
#     b = float(input("Cannot divide by zero! Enter again: "))
# if op == "+":
#     result = a + b
# elif op == "-":
#     result = a - b
# elif op == "*":
#     result = a * b
# else:
#     result = a / b
# print("Result:", result)

# Q17. 
# balance = 10000
# choice = 0
# while choice != 4:
#     print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
#     choice = int(input("Choose: "))
#     if choice == 1:
#         print("Balance:", balance)
#     elif choice == 2:
#         amount = float(input("Deposit amount: "))
#         while amount <= 0:
#             amount = float(input("Enter positive amount: "))
#         balance += amount
#         print("New balance:", balance)
#     elif choice == 3:
#         amount = float(input("Withdrawal amount: "))
#         while amount <= 0 or amount > balance:
#             amount = float(input("Invalid amount! Enter again: "))
#         balance -= amount
#         print("New balance:", balance)
#     elif choice == 4:
#         print("Goodbye!")
#     else:
#         print("Invalid menu choice!")




# Q18. 
# month = int(input("Month (1-12): "))
# while month < 1 or month > 12:
#     month = int(input("Invalid month! Enter again: "))
# day = int(input("Day (1-31): "))
# while day < 1 or day > 31:
#     day = int(input("Invalid day! Enter again: "))
# print("Month:", month, "Day:", day)

# Q19
# quantity = int(input("Quantity: "))
# while quantity <= 0:
#     quantity = int(input("Enter positive quantity: "))
# price = float(input("Unit price: "))
# while price <= 0:
#     price = float(input("Enter positive price: "))
# print("Total cost:", quantity * price)



# Q20. 
# count = int(input("How many numbers (1-20)? "))
# while count < 1 or count > 20:
#     count = int(input("Invalid count! Enter 1-20: "))
# total = 0
# for i in range(count):
#     value = float(input("Enter number: "))
#     total += value
# print("Average:", total / count)



# Q21.
# password = input("Enter password: ")
# while True:
#     upper = lower = digit = False
#     whitespace = False
#     for ch in password:
#         if ch.isupper():
#             upper = True
#         if ch.islower():
#             lower = True
#         if ch.isdigit():
#             digit = True
#         if ch.isspace():
#             whitespace = True
#     valid = True
#     if len(password) < 8:
#         print("Need at least 8 characters")
#         valid = False
#     if not upper:
#         print("Need an uppercase letter")
#         valid = False
#     if not lower:
#         print("Need a lowercase letter")
#         valid = False
#     if not digit:
#         print("Need a digit")
#         valid = False
#     if whitespace:
#         print("Whitespace is not allowed")
#         valid = False
#     if valid:
#         print("Strong password accepted!")
#         break
#     password = input("Try another password: ")



# Q22. 
# n = 0
# while n < 1 or n > 10:
#     n = int(input("Enter integer (1-10): "))
# print("Accepted:", n)



# Q23. 
# total = 0
# for i in range(1, 4):
#     score = int(input("Enter score (0-100): "))
#     while score < 0 or score > 100:
#         score = int(input("Invalid score! Enter again: "))
#     total += score
# print("Total:", total)
# print("Average:", total / 3)




# Q24. 
# balance = 10000
# amount = int(input("Withdrawal amount (multiple of 100): "))
# while (amount <= 0 or amount > balance
#        or amount % 100 != 0):
#     amount = int(input("Invalid! Enter valid amount: "))
# balance -= amount
# print("Withdrawn:", amount)
# print("Remaining balance:", balance)
