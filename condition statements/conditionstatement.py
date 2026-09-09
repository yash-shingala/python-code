# Number=int(input("Enter a number: "))
# if Number%2==0:
#     print("The number is even.")

# if Number%2!=0:
#     print("The number is odd.")

# if Number%2==1:
#     print("The number is odd.")


# num = int(input("Enter a number: "))

# if num > 10:
#     print("Greater than 10")



# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Adult")



# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")




# marks = int(input("Enter your marks: "))

# if marks >= 35:
#     print("Pass")+

# age=map(int,input("Enter your age: ").split()[0:1])
# age=list(age)
# print(age)

# doubt
# age =int(input("Enter your age: ").split()[0])
# print(age)


# number = input("Enter a number: ").split()
# print(number, type(number))
# number = int(number)
# print(number, type(number))




# age = int(input("Enter your age: ").split()[0])
# gender = input("Enter your gender: ")
# gender = gender.lower().strip()
# print(age, gender)
# if age>=18 :
#     if gender=="female":
#         print("seat are available.")

#     if gender=="male":
#         print("seat are not available.")


# username=input("Enter your username: ")
# password=input("Enter your password: ")
# if username=="mansukh":
#     if password=="mansukh123":
#         print("Login successful.")
#     else:
#         print("Incorrect password.")
# else:
#     print("Incorrect username.")


#"18"==18
#"18">=18

# number_enter_byuser=int(input("enter any number from 1 2 3 4 5:"))
# a=input("enter number1:")
# b=input("enter number2:")
# a=int(a)
# b=int(b)
# if number_enter_byuser==1:
#     print(a+b)
# elif number_enter_byuser==2:
#     print(a-b)
# elif number_enter_byuser==3:
#     print(a*b)
# elif number_enter_byuser==4:
#     print(a/b)
# elif number_enter_byuser==5:
#     print(a//b)
# else:
#     print("there is an error!")


#time complexciy or code optimization
# number_enter_byuser=int(input("enter any number from 1 2 3 4 5:"))
# if number_enter_byuser==1 or number_enter_byuser==2 or number_enter_byuser==3 or number_enter_byuser==4 or number_enter_byuser==5:
#    a=input("enter number1:")
#    b=input("enter number2:")
#    a=int(a)
#    b=int(b)
#    if number_enter_byuser==1:
#     print(a+b)
#    elif number_enter_byuser==2:
#     print(a-b)
#    elif number_enter_byuser==3:
#     print(a*b)
#    elif number_enter_byuser==4:
#     print(a/b)
#    elif number_enter_byuser==5:
#     print(a//b)
# else:
#     print("there is an error!")


# has_id=input("enter if he has id (yes/no):").strip().lower()
# if has_id=="no":
#     has_id=True
# elif has_id=="yes":
#     has_id=False
# else:
#     print("enter valied value!!")

# if has_id:
#     print("welcome!!")
# else:
#     print("bring your id")

yes=True
no=False
has_id=input("enter if he has id (yes/no):").strip().lower()
if has_id=="no":
    print("welcome!!")
elif has_id=="yes":
    print("bring your id")
else:
    print("enter valied value!!")