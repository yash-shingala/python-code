
# #  Q1 TO Q40



# # Q1.
# choice = int(input("Enter your choice: "))

# match choice:
#     case 1:
#         print("You selected Pizza")
#     case 2:
#         print("You selected Burger")
#     case 3:
#         print("You selected Pasta")
#     case 4:
#         print("You selected Sandwich")
#     case _:
#         print("Invalid Menu Choice")


# # Q2.
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Wi-Fi Selected")
#     case 2:
#         print("Bluetooth Selected")
#     case 3:
#         print("Mobile Data Selected")
#     case 4:
#         print("Airplane Mode Selected")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Setting")


# # Q3. 
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Check Balance Selected")
#     case 2:
#         print("Withdraw Money Selected")
#     case 3:
#         print("Deposit Money Selected")
#     case 4:
#         print("Change PIN Selected")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# # Q4. 
# signal = input("Enter signal: ").lower()

# match signal:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _:
#         print("Invalid Signal")


# # Q5. 
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Opening Profile")
#     case 2:
#         print("Opening Courses")
#     case 3:
#         print("Opening Marks")
#     case 4:
#         print("Opening Attendance")
#     case 5:
#         print("Logout")
#     case _:
#         print("Invalid Choice")


# # Q6. 
# choice = int(input("Enter category: "))

# match choice:
#     case 1:
#         print("Opening Electronics")
#     case 2:
#         print("Opening Clothing")
#     case 3:
#         print("Opening Books")
#     case 4:
#         print("Opening Grocery")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# # Q7. 
# choice = int(input("Enter service: "))

# match choice:
#     case 1:
#         print("Opening Account Balance")
#     case 2:
#         print("Opening Mini Statement")
#     case 3:
#         print("Opening Fund Transfer")
#     case 4:
#         print("Opening Bill Payment")
#     case 5:
#         print("Opening Customer Support")
#     case _:
#         print("Invalid Service")


# # Q8. 
# choice = int(input("Enter show: "))

# match choice:
#     case 1:
#         print("Morning Show Selected")
#     case 2:
#         print("Afternoon Show Selected")
#     case 3:
#         print("Evening Show Selected")
#     case 4:
#         print("Night Show Selected")
#     case _:
#         print("Invalid Show")


# # Q9. 
# weather = input("Enter weather: ").lower()

# match weather:
#     case "sunny":
#         print("Wear sunglasses")
#     case "rainy":
#         print("Carry an umbrella")
#     case "cloudy":
#         print("Weather may change")
#     case "snowy":
#         print("Wear warm clothes")
#     case _:
#         print("Unknown Weather")


# # Q10.
# payment = input("Enter payment method: ").lower()

# match payment:
#     case "upi":
#         print("UPI Payment Selected")
#     case "card":
#         print("Card Payment Selected")
#     case "cash":
#         print("Cash Payment Selected")
#     case "wallet":
#         print("Wallet Payment Selected")
#     case _:
#         print("Invalid Payment Method")


# # Q11. 
# extension = input("Enter extension: ").lower()

# match extension:
#     case "pdf":
#         print("Document")
#     case "jpg" | "png":
#         print("Image")
#     case "mp3":
#         print("Audio File")
#     case "mp4":
#         print("Video")
#     case _:
#         print("Unknown File Type")


# # Q12. 
# role = input("Enter role: ").lower()

# match role:
#     case "admin":
#         print("Full Access")
#     case "teacher":
#         print("Teacher Dashboard")
#     case "student":
#         print("Student Dashboard")
#     case "guest":
#         print("Limited Access")
#     case _:
#         print("Invalid Role")


# # Q13.
# day = int(input("Enter day number: "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid Day")


# # Q14.
# priority = int(input("Enter priority: "))

# match priority:
#     case 1 | 2:
#         print("Normal Priority")
#     case 3 | 4:
#         print("Urgent Priority")
#     case _:
#         print("Invalid Priority")


# # Q15.
# membership = int(input("Enter membership level: "))

# match membership:
#     case 1 | 2:
#         print("Basic Membership")
#     case 3 | 4:
#         print("Premium Membership")
#     case _:
#         print("Invalid Membership")


# # Q16. 
# user_type = int(input("Enter user type: "))
# option = int(input("Enter option: "))

# match user_type:
#     case 1:
#         match option:
#             case 1:
#                 print("Opening Student Courses")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case _:
#                 print("Invalid Student Option")

#     case 2:
#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Opening Teacher Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case _:
#                 print("Invalid Teacher Option")

#     case _:
#         print("Invalid User Type")


# # Q17.
# account = int(input("Enter account type: "))
# operation = int(input("Enter operation: "))

# match account:
#     case 1:
#         print("Savings Account")
#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case 2:
#         print("Current Account")
#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case _:
#         print("Invalid Account Type")


# # Q18.
# category = int(input("Enter category: "))
# product = int(input("Enter product: "))

# match category:
#     case 1:
#         match product:
#             case 1:
#                 print("Mobile Selected")
#             case 2:
#                 print("Laptop Selected")
#             case 3:
#                 print("Headphones Selected")
#             case _:
#                 print("Invalid Product")

#     case 2:
#         match product:
#             case 1:
#                 print("Shirt Selected")
#             case 2:
#                 print("Jeans Selected")
#             case 3:
#                 print("Shoes Selected")
#             case _:
#                 print("Invalid Product")

#     case _:
#         print("Invalid Category")


# # Q19. 
# category = int(input("Enter category: "))
# food = int(input("Enter food: "))

# match category:
#     case 1:
#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid Food")

#     case 2:
#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid Food")

#     case _:
#         print("Invalid Category")


# # Q20. 
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# operator = input("Enter operator: ")

# match operator:
#     case "+":
#         print("Result =", a + b)
#     case "-":
#         print("Result =", a - b)
#     case "*":
#         print("Result =", a * b)
#     case "/":
#         if b == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Result =", a / b)
#     case _:
#         print("Invalid Operator")


# # Q21.
# choice = int(input("Enter choice: "))
# temperature = float(input("Enter temperature: "))

# match choice:
#     case 1:
#         fahrenheit = (temperature * 9 / 5) + 32
#         print("Temperature =", fahrenheit, "F")
#     case 2:
#         celsius = (temperature - 32) * 5 / 9
#         print("Temperature =", celsius, "C")
#     case _:
#         print("Invalid Choice")


# # Q22.
# choice = int(input("Enter choice: "))
# value = float(input("Enter value: "))

# match choice:
#     case 1:
#         print(value * 1000, "meters")
#     case 2:
#         print(value / 1000, "kilometers")
#     case 3:
#         print(value * 1000, "grams")
#     case 4:
#         print(value / 1000, "kilograms")
#     case _:
#         print("Invalid Choice")


# # Q23.
# account = int(input("Enter account type: "))
# amount = float(input("Enter amount: "))

# match account:
#     case 1:
#         print("Savings Account")
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case 2:
#         print("Current Account")
#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case _:
#         print("Invalid Account Type")


# # Q24.
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         age = int(input("Enter age: "))

#         if age >= 18:
#             print("You can start the exam")
#         else:
#             print("You cannot start the exam")

#     case 2:
#         print("Viewing Result")

#     case 3:
#         print("Exit")

#     case _:
#         print("Invalid Choice")


# # Q25.
# ticket = int(input("Enter ticket type: "))
# age = int(input("Enter age: "))

# if age < 5:
#     print("Free Entry")
# else:
#     match ticket:
#         case 1:
#             print("Regular Ticket")
#         case 2:
#             print("Premium Ticket")
#         case 3:
#             print("VIP Ticket")
#         case _:
#             print("Invalid Ticket Type")


# # Q26. 
# device = int(input("Enter device: "))

# match device:
#     case 1:
#         print("Light Controller Opened")
#     case 2:
#         print("Fan Controller Opened")
#     case 3:
#         print("AC Controller Opened")
#     case 4:
#         print("TV Controller Opened")
#     case _:
#         print("Invalid Device")


# # Q27. 
# department = int(input("Enter department: "))

# match department:
#     case 1:
#         print("General Medicine")
#     case 2:
#         print("Cardiology")
#     case 3:
#         print("Orthopedics")
#     case 4:
#         print("Pediatrics")
#     case 5:
#         print("Emergency")
#     case _:
#         print("Invalid Department")


# # Q28. 
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Book Ticket")
#     case 2:
#         print("Cancel Ticket")
#     case 3:
#         print("Check PNR")
#     case 4:
#         print("Train Schedule")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# # Q29. 
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Search Book")
#     case 2:
#         print("Issue Book")
#     case 3:
#         print("Return Book")
#     case 4:
#         print("View Issued Books")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# # Q30.
# status = input("Enter status: ").lower()

# match status:
#     case "placed":
#         print("Your order has been placed")
#     case "confirmed":
#         print("Your order is confirmed")
#     case "preparing":
#         print("Your order is being prepared")
#     case "out_for_delivery":
#         print("Your order is on the way")
#     case "delivered":
#         print("Your order has been delivered")
#     case "cancelled":
#         print("Your order has been cancelled")
#     case _:
#         print("Unknown Order Status")


# # Q31. 
# banking_type = int(input("Enter banking type: "))
# option = int(input("Enter option: "))

# match banking_type:
#     case 1:
#         match option:
#             case 1:
#                 print("Personal Balance Selected")
#             case 2:
#                 print("Personal Transfer Selected")
#             case 3:
#                 print("Personal Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         match option:
#             case 1:
#                 print("Business Balance Selected")
#             case 2:
#                 print("Payroll Selected")
#             case 3:
#                 print("Business Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Banking Type")


# # Q32. 
# role = int(input("Enter role: "))
# option = int(input("Enter option: "))

# match role:
#     case 1:
#         match option:
#             case 1:
#                 print("Student Marks")
#             case 2:
#                 print("Student Attendance")
#             case 3:
#                 print("Student Homework")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         match option:
#             case 1:
#                 print("Enter Marks")
#             case 2:
#                 print("Teacher Attendance")
#             case 3:
#                 print("Assign Homework")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         match option:
#             case 1:
#                 print("Child Marks")
#             case 2:
#                 print("Child Attendance")
#             case 3:
#                 print("Contact Teacher")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")


# # Q33.
# transport = int(input("Enter transport: "))
# option = int(input("Enter option: "))

# match transport:
#     case 1:
#         match option:
#             case 1:
#                 print("Economy Flight")
#             case 2:
#                 print("Business Flight")
#             case _:
#                 print("Invalid Flight Option")

#     case 2:
#         match option:
#             case 1:
#                 print("Sleeper Train")
#             case 2:
#                 print("AC Train")
#             case _:
#                 print("Invalid Train Option")

#     case 3:
#         match option:
#             case 1:
#                 print("Ordinary Bus")
#             case 2:
#                 print("Volvo Bus")
#             case _:
#                 print("Invalid Bus Option")

#     case _:
#         print("Invalid Transport")


# # Q34. 
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Start Game")
#     case 2:
#         print("Load Game")
#     case 3:
#         setting = int(input("Enter setting: "))

#         match setting:
#             case 1:
#                 print("Sound Settings")
#             case 2:
#                 print("Graphics Settings")
#             case 3:
#                 print("Controls Settings")
#             case _:
#                 print("Invalid Setting")

#     case 4:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# # Q35. 
# category = int(input("Enter category: "))
# item = int(input("Enter item: "))

# match category:
#     case 1:
#         match item:
#             case 1:
#                 print("Soup Selected")
#             case 2:
#                 print("Spring Roll Selected")
#             case 3:
#                 print("Garlic Bread Selected")
#             case _:
#                 print("Invalid Starter")

#     case 2:
#         match item:
#             case 1:
#                 print("Pizza Selected")
#             case 2:
#                 print("Pasta Selected")
#             case 3:
#                 print("Biryani Selected")
#             case _:
#                 print("Invalid Main Course")

#     case 3:
#         match item:
#             case 1:
#                 print("Ice Cream Selected")
#             case 2:
#                 print("Cake Selected")
#             case 3:
#                 print("Gulab Jamun Selected")
#             case _:
#                 print("Invalid Dessert")

#     case 4:
#         match item:
#             case 1:
#                 print("Coffee Selected")
#             case 2:
#                 print("Tea Selected")
#             case 3:
#                 print("Juice Selected")
#             case _:
#                 print("Invalid Drink")

#     case _:
#         print("Invalid Category")


# # Q36. 
# payment = int(input("Enter payment type: "))
# option = int(input("Enter option: "))

# match payment:
#     case 1:
#         match option:
#             case 1:
#                 print("Scan QR Selected")
#             case 2:
#                 print("Enter UPI ID Selected")
#             case _:
#                 print("Invalid UPI Option")

#     case 2:
#         match option:
#             case 1:
#                 print("Credit Card Selected")
#             case 2:
#                 print("Debit Card Selected")
#             case _:
#                 print("Invalid Card Option")

#     case 3:
#         match option:
#             case 1:
#                 print("Add Money Selected")
#             case 2:
#                 print("Pay Using Wallet Selected")
#             case _:
#                 print("Invalid Wallet Option")

#     case _:
#         print("Invalid Payment Type")


# # Q37. 
# subject = int(input("Enter subject: "))
# course = int(input("Enter course: "))

# match subject:
#     case 1:
#         match course:
#             case 1:
#                 print("Python Selected")
#             case 2:
#                 print("Java Selected")
#             case 3:
#                 print("C++ Selected")
#             case _:
#                 print("Invalid Course")

#     case 2:
#         match course:
#             case 1:
#                 print("Algebra Selected")
#             case 2:
#                 print("Calculus Selected")
#             case 3:
#                 print("Statistics Selected")
#             case _:
#                 print("Invalid Course")

#     case 3:
#         match course:
#             case 1:
#                 print("English Selected")
#             case 2:
#                 print("Presentation Selected")
#             case 3:
#                 print("Interview Skills Selected")
#             case _:
#                 print("Invalid Course")

#     case _:
#         print("Invalid Subject")


# # Q38. 
# choice = int(input("Enter option: "))

# match choice:
#     case 1:
#         option = int(input("Enter engine option: "))

#         match option:
#             case 1:
#                 print("Engine Started")
#             case 2:
#                 print("Engine Stopped")
#             case _:
#                 print("Invalid Engine Option")

#     case 2:
#         option = int(input("Enter light option: "))

#         match option:
#             case 1:
#                 print("Headlights Selected")
#             case 2:
#                 print("Indicators Selected")
#             case 3:
#                 print("Hazard Lights Selected")
#             case _:
#                 print("Invalid Light Option")

#     case 3:
#         option = int(input("Enter music option: "))

#         match option:
#             case 1:
#                 print("Music Playing")
#             case 2:
#                 print("Music Paused")
#             case 3:
#                 print("Next Song")
#             case 4:
#                 print("Previous Song")
#             case _:
#                 print("Invalid Music Option")

#     case 4:
#         option = int(input("Enter navigation option: "))

#         match option:
#             case 1:
#                 print("Navigation Started")
#             case 2:
#                 print("Navigation Stopped")
#             case _:
#                 print("Invalid Navigation Option")

#     case _:
#         print("Invalid Choice")


# # Q39. 
# role = int(input("Enter role: "))
# option = int(input("Enter option: "))

# match role:
#     case 1:
#         match option:
#             case 1:
#                 print("View Profile")
#             case 2:
#                 leave_days = int(input("Enter leave days: "))

#                 if leave_days > 0:
#                     print("Leave Request Submitted")
#                 else:
#                     print("Invalid Leave Days")

#             case 3:
#                 print("View Salary")

#             case _:
#                 print("Invalid Employee Option")

#     case 2:
#         match option:
#             case 1:
#                 print("View Team")
#             case 2:
#                 print("Approve Leave")
#             case 3:
#                 print("View Reports")
#             case _:
#                 print("Invalid Manager Option")

#     case _:
#         print("Invalid Role")


# # Q40. 
# role = int(input("Enter role: "))
# option = int(input("Enter option: "))

# match role:

#     case 1:
#         match option:
#             case 1:
#                 print("Opening Student Profile")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case 4:
#                 print("Opening Student Courses")
#             case _:
#                 print("Invalid Student Option")

#     case 2:
#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Opening Teacher Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case 4:
#                 print("Opening Teacher Courses")
#             case _:
#                 print("Invalid Teacher Option")

#     case 3:
#         match option:
#             case 1:
#                 print("Opening Fees")
#             case 2:
#                 print("Opening Admissions")
#             case 3:
#                 print("Opening Notices")
#             case 4:
#                 print("Opening Departments")
#             case _:
#                 print("Invalid Administration Option")

#     case _:
#         print("Invalid Role")