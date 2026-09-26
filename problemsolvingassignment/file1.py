#1
# num=int(input("enter a number:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# elif num==0:
#     print("zero")



#2
# num=int(input("enter a number:"))
# if num>0:
#     if num%2==0:
#         print("positive even")
#     elif num%2!=0:
#         print("positive odd")
# elif num<0:
#     if num%2==0:
#         print("negative even")
#     elif num%2!=0:
#          print("negative odd")
# else:
#     print("zero")


#3
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# if num1>num2:
#     print("num1")
# elif num2>num1:
#     print("num2")
# else:
#     print("both are equal")


#4
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# num3=int(input("enter a number:"))
# if num1<num2 and num1<num3:
#     print(f"{num1}")
# elif num2<num1 and num2<num3:
#     print(f"{num2}")
# elif num3<num1 and num3<num2:
#     print(f"{num3}")
# elif num1==num2 and num1<num3:
#     print(f"{num1}")
# elif num3==num2 and num3<num1:
#     print(f"{num3}")
# elif num1==num3 and num1<num2:
#     print(F"{num1}")
# else:
#     print(F"{num1}")




#5
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# num3=int(input("enter a number:"))
# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# elif num3>num1 and num3>num2:
#     print(num3)
# elif num1==num2 and num1>num3:
#     print(num1)
# elif num3==num2 and num3>num1:
#     print(num3)
# elif num1==num3 and num1>num2:
#     print(num1)
# else:
#     print(num1)


#6
# num=int(input("enter a number:"))
# if num%5==0 and num%11==0:
#     print("divisible by 5 and 11.")
# elif num%5==0:
#     if num%11!=0:
#         print("divisible only by 5.")
# elif num%11==0:
#     if num%5!=0:
#         print("divisible only by 11.")
# else:
#     print("divisible bt neither.")


#7
# num=int(input("enter a number:"))
# if num%3==0 and num%7==0:
#     print("divisible by 3 and 7.")
# elif num%3==0:
#     if num%7!=0:
#         print("divisible only by 3.")
# elif num%7==0:
#     if num%3!=0:
#         print("divisible only by 7.")
# else:
#     print("divisible bt neither.")


#8
# marks=int(input("enter your marks:"))
# if marks<0:
#     print("invalied marks")
# elif marks>100:
#     print("invalied marks")
# elif marks>=40:
#     print("pass")
# elif marks<40:
#     print("fail")


#9
# marks=int(input("enter your marks:"))
# if marks<0:
#     print("invalied marks")
# elif marks>100:
#     print("invalied marks")
# elif marks>=90:
#     print("A")
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("C")
# elif marks>=60:
#     print("D")
# elif marks>=40:
#     print("E")
# elif marks<40:
#     print("FAIL")


#10
# age=int(input("enter age :"))
# if age<0:
#     print("invalied age")
# elif age>120:
#     print("invalied age")
# elif age<18:
#     print("cannot vote!")
# elif age>=18:
#     print("can vote!")


##LEVEL 2

#11
# year=int(input("enter year:"))
# if (year%400==0 or year%4==0) and year%100!=0:
#     print("Leap year!")
# else:
#     print("NOT Leap year!")


#12
# char = input("Enter one character: ")
# if char >= 'A' and char <= 'Z':
#     print("Uppercase alphabet")
# elif char >= 'a' and char <= 'z':
#     print("Lowercase alphabet")
# elif char >= '0' and char <= '9':
#     print("Digit")
# else:
#     print("Special character")


#13
# char = input("Enter one character: ").lower()
# if char>="a" and char<="z":
#     if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#         print("vowel")
#     else:
#         print("consonent")
# else:
#     print("invalied")


#14
# cost=int(input("enter cost:"))
# selling=int(input("enter selling price:"))
# if selling-cost==0:
#     print("no profit and no loss")
# elif selling-cost>0:
#     print("profit")
# elif selling-cost<0:
#     print("loss")


#15
# cost_price = float(input("Enter cost price: "))
# selling_price = float(input("Enter selling price: "))

# if cost_price <= 0:
#     print("Invalid cost price")

# elif selling_price > cost_price:
#     profit = selling_price - cost_price
#     profit_percentage = (profit / cost_price) * 100

#     print("Profit =", profit)
#     print("Profit Percentage =", profit_percentage, "%")

# elif selling_price < cost_price:
#     loss = cost_price - selling_price
#     loss_percentage = (loss / cost_price) * 100

#     print("Loss =", loss)
#     print("Loss Percentage =", loss_percentage, "%")

# else:
#     print("No Profit No Loss")


#16
# unit=int(input("enter electricity unit:"))
# if unit>0 and unit<=100:
#     price_of_aunit1=5
#     print(unit*price_of_aunit1)
# elif unit>100 and unit<=200:
#     first_hundred=100*5
#     remaining_unit=(unit-100)*7
#     print(first_hundred+remaining_unit)
# elif unit>200:
#     first_hundred=100*5
#     next_hundred=100*7
#     remaining_unit=(unit-200)*10
#     print(first_hundred+next_hundred+remaining_unit)



#17
# a=int(input("firstnumber:"))
# b=int(input("secondnumber:"))
# num=int(input("enter number :- 1/addition  2/subtractiob  3/multiplication  4/division  :-"))
# if num==1:
#     print(f"addition:- {a+b}")
# elif num==2:
#     print(f"subtraction:- {a-b}")
# elif num==3:
#     print(f"multiplication:- {a*b}")
# elif num==4 and b!=0:
#     print(f"division:- {a/b}")
# if num==4 and b==0:
#     print("undefined value of division")



#18
# temp=float(input("enter a temperature:"))
# if temp<0:
#     print("freezing")
# elif temp>=0 and temp<=15:
#     print("very cold")
# elif temp>=16 and temp<=25:
#     print("cold")
# elif temp>=26 and temp<=35:
#     print("normal")
# else:
#     print("hot")



#19
# num=float(input("enter a number:"))
# if num<0:
#     print("negative")
# elif num>=0 and num<=10:
#     print("number is between 0 to 10")
# elif num>=11 and num<=50:
#     print("number is between 11 to 50")
# elif num>=51 and num<=100:
#     print("number is between 51 to 100")
# elif num>100:
#     print("number is above 100")


#20
# a = float(input("Enter side 1: "))
# b = float(input("Enter side 2: "))
# c = float(input("Enter side 3: "))

# if a <= 0 or b <= 0 or c <= 0:
#     print("Invalid side lengths")

# elif a + b > c and a + c > b and b + c > a:
#     print("Valid triangle")

# else:
#     print("Invalid triangle")




# # 21. TRIANGLE TYPE

# a = float(input("Enter side 1: "))
# b = float(input("Enter side 2: "))
# c = float(input("Enter side 3: "))

# if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("Equilateral")
#     elif a == b or b == c or a == c:
#         print("Isosceles")
#     else:
#         print("Scalene")
# else:
#     print("Invalid triangle")



# # 22. ATM WITHDRAWAL

# balance = float(input("\nEnter account balance: "))
# withdrawal = float(input("Enter withdrawal amount: "))

# if withdrawal <= 0:
#     print("Invalid withdrawal amount")
# elif withdrawal % 100 != 0:
#     print("Withdrawal amount must be divisible by 100")
# elif withdrawal > balance:
#     print("Insufficient balance")
# elif balance - withdrawal < 500:
#     print("At least ₹500 must remain in the account")
# else:
#     remaining_balance = balance - withdrawal
#     print("Withdrawal successful")
#     print("Remaining balance:", remaining_balance)



# # 23. LOGIN SYSTEM


# username = input("\nEnter username: ")
# password = input("Enter password: ")

# if username != "admin":
#     print("User not found")
# elif password != "python123":
#     print("Wrong password")
# else:
#     print("Login successful")



# # 24. DISCOUNT CALCULATOR


# purchase = float(input("\nEnter purchase amount: ₹"))

# if purchase < 500:
#     discount_percent = 0
# elif purchase < 1000:
#     discount_percent = 5
# elif purchase < 2000:
#     discount_percent = 10
# elif purchase < 5000:
#     discount_percent = 15
# else:
#     discount_percent = 20

# discount_amount = purchase * discount_percent / 100
# final_amount = purchase - discount_amount

# print("Original amount: ₹", purchase)
# print("Discount percentage:", discount_percent, "%")
# print("Discount amount: ₹", discount_amount)
# print("Final amount: ₹", final_amount)



# # 25. STUDENT RESULT SYSTEM


# marks1 = float(input("\nEnter marks for Subject 1: "))
# marks2 = float(input("Enter marks for Subject 2: "))
# marks3 = float(input("Enter marks for Subject 3: "))

# if (marks1 < 0 or marks1 > 100 or
#     marks2 < 0 or marks2 > 100 or
#     marks3 < 0 or marks3 > 100):
#     print("Invalid marks")
# elif marks1 < 35 or marks2 < 35 or marks3 < 35:
#     print("Fail")
# else:
#     average = (marks1 + marks2 + marks3) / 3

#     print("Average:", average)

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")



# # 26. DATE VALIDATOR


# day = int(input("\nEnter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))

# if month < 1 or month > 12:
#     print("Invalid date")
# else:
#     # Check leap year
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         leap_year = True
#     else:
#         leap_year = False

#     if month == 2:
#         if leap_year:
#             max_days = 29
#         else:
#             max_days = 28
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         max_days = 30
#     else:
#         max_days = 31

#     if day >= 1 and day <= max_days:
#         print("Valid date")
#     else:
#         print("Invalid date")



# # 27. TIME VALIDATOR


# hours = int(input("\nEnter hours: "))
# minutes = int(input("Enter minutes: "))
# seconds = int(input("Enter seconds: "))

# if (hours >= 0 and hours <= 23 and
#     minutes >= 0 and minutes <= 59 and
#     seconds >= 0 and seconds <= 59):
#     print("Valid time")
# else:
#     print("Invalid time")



# # 28. YOUNGEST OF THREE PEOPLE


# name1 = input("\nEnter Person 1 name: ")
# age1 = int(input("Enter Person 1 age: "))

# name2 = input("Enter Person 2 name: ")
# age2 = int(input("Enter Person 2 age: "))

# name3 = input("Enter Person 3 name: ")
# age3 = int(input("Enter Person 3 age: "))

# if age1 < age2 and age1 < age3:
#     print(name1, "is the youngest")
# elif age2 < age1 and age2 < age3:
#     print(name2, "is the youngest")
# elif age3 < age1 and age3 < age2:
#     print(name3, "is the youngest")
# elif age1 == age2 and age2 < age3:
#     print(name1, "and", name2, "are the youngest")
# elif age1 == age3 and age3 < age2:
#     print(name1, "and", name3, "are the youngest")
# elif age2 == age3 and age2 < age1:
#     print(name2, "and", name3, "are the youngest")
# else:
#     print("All three are the same age")



# # 29. SECOND LARGEST OF THREE NUMBERS


# num1 = float(input("\nEnter number 1: "))
# num2 = float(input("Enter number 2: "))
# num3 = float(input("Enter number 3: "))

# if num1 > num2:
#     if num2 > num3:
#         second_largest = num2
#     elif num1 > num3:
#         second_largest = num3
#     else:
#         second_largest = num1
# else:
#     if num1 > num3:
#         second_largest = num1
#     elif num2 > num3:
#         second_largest = num3
#     else:
#         second_largest = num2

# print("Second largest:", second_largest)



# # 30. COMPLETE SCHOLARSHIP DECISION


# age = int(input("\nEnter student age: "))
# marks = float(input("Enter marks: "))
# income = float(input("Enter family income: ₹"))
# attendance = float(input("Enter attendance percentage: "))

# if (age >= 18 and age <= 25 and
#     marks >= 85 and
#     income <= 300000 and
#     attendance >= 75):

#     print("Scholarship Approved")

# else:
#     print("Scholarship Rejected")

#     if age < 18 or age > 25:
#         print("Reason: Age must be between 18 and 25")

#     if marks < 85:
#         print("Reason: Marks below 85")

#     if income > 300000:
#         print("Reason: Family income above ₹300000")

#     if attendance < 75:
#         print("Reason: Attendance below 75%")
