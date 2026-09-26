# #q1
# text = input("Enter a string: ")

# uppercase = 0
# lowercase = 0
# digits = 0
# spaces = 0
# special = 0

# for ch in text:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         special += 1

# print("Uppercase:", uppercase)
# print("Lowercase:", lowercase)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special Characters:", special)

# # Find the category with the highest count
# highest = uppercase
# category = "Uppercase"

# if lowercase > highest:
#     highest = lowercase
#     category = "Lowercase"

# if digits > highest:
#     highest = digits
#     category = "Digits"

# if spaces > highest:
#     highest = spaces
#     category = "Spaces"

# if special > highest:
#     highest = special
#     category = "Special Characters"

# # Check for tie
# tie_count = 0

# if uppercase == highest:
#     tie_count += 1

# if lowercase == highest:
#     tie_count += 1

# if digits == highest:
#     tie_count += 1

# if spaces == highest:
#     tie_count += 1

# if special == highest:
#     tie_count += 1

# if tie_count > 1:
#     print("Highest Category: Tie")
# else:
#     print("Highest Category:", category)







# # Q2
# fail = 0
# passed = 0
# good = 0
# excellent = 0

# for i in range(1, 11):
#     marks = int(input("Enter marks for student " + str(i) + ": "))

#     if marks < 35:
#         print("Fail")
#         fail += 1

#     elif marks <= 49:
#         print("Pass")
#         passed += 1

#     elif marks <= 74:
#         print("Good")
#         good += 1

#     elif marks <= 100:
#         print("Excellent")
#         excellent += 1

#     else:
#         print("Invalid marks")


# print("Fail:", fail)
# print("Pass:", passed)
# print("Good:", good)
# print("Excellent:", excellent)

# # Q3
# sentence = input("Enter a sentence: ")

# words = sentence

# highest_score = 0
# highest_word = ""

# for word in words:
#     score = 0

#     for ch in word:
#         if ch in "aeiouAEIOU":
#             score += 2
#         elif ch.isalpha():
#             score += 1
#         elif ch.isdigit():
#             score += 3
#         else:
#             score += 4

#     print(word, "=", score)

#     if score > highest_score:
#         highest_score = score
#         highest_word = word

# print("Word with highest score:", highest_word)
# print("Highest score:", highest_score)

# print("Word with highest score:", highest_word)
# print("Highest score:", highest_score)

# # # Q4
# strong = 0
# medium = 0
# weak = 0

# for i in range(1, 6):
#     password = input("Enter password for user " + str(i) + ": ")

#     length = False
#     uppercase = False
#     lowercase = False
#     digit = False
#     special = False

#     if len(password) >= 8:
#         length = True

#     for ch in password:
#         if ch.isupper():
#             uppercase = True
#         elif ch.islower():
#             lowercase = True
#         elif ch.isdigit():
#             digit = True
#         else:
#             special = True

#     conditions = 0

#     if length:
#         conditions += 1
#     if uppercase:
#         conditions += 1
#     if lowercase:
#         conditions += 1
#     if digit:
#         conditions += 1
#     if special:
#         conditions += 1

#     if conditions == 5:
#         print("Strong")
#         strong += 1
#     elif conditions >= 3:
#         print("Medium")
#         medium += 1
#     else:
#         print("Weak")
#         weak += 1


# print("Strong:", strong)
# print("Medium:", medium)
# print("Weak:", weak)


# # # Q5
# sentence = input("Enter a sentence: ")

# short = 0
# medium = 0
# long = 0

# words = sentence.split()

# for word in words:
#     length = len(word)

#     print(word, "Length:", length)

#     if length <= 3:
#         print("Short")
#         short += 1

#     elif length <= 6:
#         print("Medium")
#         medium += 1

#     else:
#         print("Long")
#         long += 1

# print("\n--- Summary ---")
# print("Short words:", short)
# print("Medium words:", medium)
# print("Long words:", long)

# # # Q6
# for i in range(1, 6):
#     number = input("Enter number " + str(i) + ": ")

#     even = 0
#     odd = 0

#     number_string = str(number)

#     for digit in number_string:
#         if int(digit) % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Even digits:", even)
#     print("Odd digits:", odd)

#     if even > odd:
#         print("Even occurs more")
#     elif odd > even:
#         print("Odd occurs more")
#     else:
#         print("Equal")

#     print()

# # # Q7
# text = input("Enter a string: ")

# for ch in text:
#     count = 0

#     for x in text:
#         if ch == x:
#             count += 1

#     if count > 1:
#         already_printed = False

#         for previous in text:
#             if previous == ch:
#                 if text.index(previous) < text.index(ch):
#                     already_printed = True

#         if not already_printed:
#             print(ch, "->", count, "times")

#             if count == 2:
#                 print("Duplicate")
#             elif count <= 4:
#                 print("Repeated")
#             else:
#                 print("Highly Repeated")



# text = input("Enter a string: ")

# printed = ""

# for ch in text:
#     count = 0

#     for x in text:
#         if ch == x:
#             count += 1

#     if count > 1 and ch not in printed:
#         print(ch, "->", count, "times")

#         if count == 2:
#             print("Duplicate")
#         elif count <= 4:
#             print("Repeated")
#         else:
#             print("Highly Repeated")

#         printed += ch



# # # Q8
# total = 0

# budget = 0
# regular = 0
# premium = 0
# luxury = 0

# for i in range(1, 9):
#     price = float(input("Enter price of product " + str(i) + ": "))

#     total += price

#     if price < 500:
#         print("Budget")
#         budget += 1

#     elif price < 2000:
#         print("Regular")
#         regular += 1

#     elif price < 5000:
#         print("Premium")
#         premium += 1

#     else:
#         print("Luxury")
#         luxury += 1

# average = total / 8


# print("Total amount:", total)
# print("Budget products:", budget)
# print("Regular products:", regular)
# print("Premium products:", premium)
# print("Luxury products:", luxury)
# print("Average product price:", average)


# # # Q9
# text = input("Enter a string: ")

# vowels = 0
# consonants = 0
# digits = 0
# special = 0



# for ch in text:
#     position=int(input("enter position number:"))
#     if position % 2 == 0:
#         position_type = "Even"
#     else:
#         position_type = "Odd"

#     if ch in "aeiouAEIOU":
#         category = "Vowel"
#         vowels += 1
#     elif ch.isalpha():
#         category = "Consonant"
#         consonants += 1
#     elif ch.isdigit():
#         category = "Digit"
#         digits += 1
#     else:
#         category = "Special Character"
#         special += 1

#     print("Character:", ch, " Position:", position,
#            position_type, category)

#     position += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Special Characters:", special)


# # # Q10
# n = int(input("Enter n: "))

# for row in range(1, n + 1):

#     for number in range(1, row + 1):

#         if number % 3 == 0 and number % 5 == 0:
#             print("Z", end=" ")

#         elif number % 3 == 0:
#             print("X", end=" ")

#         elif number % 5 == 0:
#             print("Y", end=" ")

#         else:
#             print(number, end=" ")

#     print()

# # # Q11
# for i in range(1, 6):
#     username = input("Enter username " + str(i) + ": ")

#     digits = 0
#     underscores = 0
#     invalid = False

#     if len(username) < 5:
#         length_ok = False
#     else:
#         length_ok = True

#     if len(username) > 0 and username[0].isalpha():
#         first_ok = True
#     else:
#         first_ok = False

#     for ch in username:
#         if ch.isdigit():
#             digits += 1
#         elif ch == "_":
#             underscores += 1
#         elif ch.isalpha():
#             pass
#         else:
#             invalid = True

#     print("Length:", len(username))
#     print("Digits:", digits)
#     print("Underscores:", underscores)

#     if invalid:
#         print("Invalid")
#     elif length_ok and first_ok:
#         print("Valid")
#     else:
#         print("Needs Improvement")

#     print()



# # # Q12
# sentence = input("Enter a sentence: ")

# vowels = 0
# consonants = 0

# a = 0
# e = 0
# i = 0
# o = 0
# u = 0

# for ch in sentence:
#     if ch.isalpha():

#         if ch.lower() == "a":
#             vowels += 1
#             a += 1

#         elif ch.lower() == "e":
#             vowels += 1
#             e += 1

#         elif ch.lower() == "i":
#             vowels += 1
#             i += 1

#         elif ch.lower() == "o":
#             vowels += 1
#             o += 1

#         elif ch.lower() == "u":
#             vowels += 1
#             u += 1

#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)

# if vowels > consonants:
#     print("Vowels Win")
# elif consonants > vowels:
#     print("Consonants Win")
# else:
#     print("Draw")

# print("a:", a)
# print("e:", e)
# print("i:", i)
# print("o:", o)
# print("u:", u)

# # # Q13
# total_revenue = 0

# for i in range(1, 7):
#     units = float(input("Enter units for customer " + str(i) + ": "))

#     if units <= 100:
#         bill = units * 5

#     elif units <= 200:
#         bill = (100 * 5) + ((units - 100) * 7)

#     elif units <= 400:
#         bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

#     else:
#         bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 15)

#     total_revenue += bill

#     print("Bill: ₹", bill)

#     if bill < 1000:
#         print("Low")
#     elif bill <= 3000:
#         print("Medium")
#     else:
#         print("High")

#     print()

# print("Total Revenue: ₹", total_revenue)

# # # Q14
# sentence = input("Enter a sentence: ")

# words = sentence


# vowels = 0
# consonants = 0

# for ch in words:
#         if ch.isalpha():

#             if ch.lower() in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

# print(words)
# print("Vowels:", vowels)
# print("Consonants:", consonants)

# if vowels > consonants:
#         print("Vowel Heavy")
# elif consonants > vowels:
#         print("Consonant Heavy")
# else:
#         print("Balanced")

# print()

# Q15
# even = 0
# odd = 0
# positive = 0
# negative = 0
# zero = 0


# largest = 0

# for i in range(3):
#     for j in range(3):
#         number = int(input("Enter matrix value: "))

#         if number % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#         if number > 0:
#             positive += 1
#         elif number < 0:
#             negative += 1
#         else:
#             zero += 1

#         if i == 0 and j == 0:
#             largest = number
#         elif number > largest:
#             largest = number

# print("\nEven:", even)
# print("Odd:", odd)
# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)
# print("Largest:", largest)


# # # Q16
# password = input("Enter password: ")

# uppercase = 0
# lowercase = 0
# digits = 0
# special = 0

# for ch in password:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
#     elif ch.isdigit():
#         digits += 1
#     else:
#         special += 1

# length = len(password)

# print("Uppercase:", uppercase)
# print("Lowercase:", lowercase)
# print("Digits:", digits)
# print("Special:", special)

# if length > 0:
#     print("Uppercase %:", uppercase * 100 / length)
#     print("Lowercase %:", lowercase * 100 / length)
#     print("Digits %:", digits * 100 / length)
#     print("Special %:", special * 100 / length)

# if uppercase >= lowercase and uppercase >= digits and uppercase >= special:
#     print("Dominant category: Uppercase")

# elif lowercase >= uppercase and lowercase >= digits and lowercase >= special:
#     print("Dominant category: Lowercase")

# elif digits >= uppercase and digits >= lowercase and digits >= special:
#     print("Dominant category: Digits")

# else:
#     print("Dominant category: Special characters")

# # # Q17
# highest_marks = -1
# highest_student = ""

# for i in range(1, 6):
#     name = input("Enter student name: ")
#     marks = float(input("Enter marks: "))

#     vowels = 0
#     consonants = 0

#     for ch in name:
#         if ch.isalpha():
#             if ch.lower() in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     if marks >= 90:
#         grade = "A"
#     elif marks >= 75:
#         grade = "B"
#     elif marks >= 60:
#         grade = "C"
#     elif marks >= 40:
#         grade = "D"
#     else:
#         grade = "F"

#     print("\nName:", name)
#     print("Marks:", marks)
#     print("Grade:", grade)
#     print("Name length:", len(name))
#     print("Vowels:", vowels)
#     print("Consonants:", consonants)

#     if vowels > consonants:
#         print("More vowels")
#     elif consonants > vowels:
#         print("More consonants")
#     else:
#         print("Equal vowels and consonants")

#     if marks > highest_marks:
#         highest_marks = marks
#         highest_student = name

#     print()

# print("Highest marks:", highest_marks)
# print("Top student:", highest_student)

# # # Q18
# balance = float(input("Enter starting balance: "))

# deposits = 0
# withdrawals = 0

# for i in range(1, 8):
#     transaction = input("Enter transaction (Deposit/Withdrawal): ")
#     amount = float(input("Enter amount: "))

#     if transaction.lower() == "deposit":
#         balance += amount
#         deposits += 1
#         print("Deposit successful")

#     elif transaction.lower() == "withdrawal":

#         if amount <= balance:
#             balance -= amount
#             withdrawals += 1
#             print("Withdrawal successful")

#             if balance < 1000:
#                 print("Low Balance")

#         else:
#             print("Insufficient balance")

#     else:
#         print("Invalid transaction")

#     print("Current balance:", balance)
#     print()


# print("Final balance:", balance)
# print("Deposits:", deposits)
# print("Withdrawals:", withdrawals)

# # # Q19
# sentence = input("Enter a sentence: ")

# has_digit = False
# has_dot = False
# has_at = False
# password_like = False
# repeated_special = False

# for ch in sentence:
#     if ch.isdigit():
#         has_digit = True

#     if ch == ".":
#         has_dot = True

#     if ch == "@":
#         has_at = True

# for i in range(len(sentence) - 1):
#     if not sentence[i].isalnum() and sentence[i] == sentence[i + 1]:
#         repeated_special = True

# words = sentence.split()

# for word in words:
#     uppercase = False
#     lowercase = False
#     digit = False

#     for ch in word:
#         if ch.isupper():
#             uppercase = True
#         elif ch.islower():
#             lowercase = True
#         elif ch.isdigit():
#             digit = True

#     if uppercase and lowercase and digit and len(word) >= 8:
#         password_like = True

# if password_like or repeated_special:
#     print("Suspicious")

# elif has_digit or has_dot or has_at:
#     print("Review")

# else:
#     print("Safe")


# # # Q20
# n = int(input("Enter n: "))

# for i in range(1, n + 1):

#     for j in range(1, n + 1):

#         result = i * j

#         if result % 5 == 0:
#             print("F", end=" ")

#         elif result % 2 == 0:
#             print("E", end=" ")

#         else:
#             print("O", end=" ")

#     print()



# Q21
# total_discount = 0

# discount_20 = 0
# discount_15 = 0
# discount_10 = 0
# no_discount = 0

# for i in range(1, 11):
#     price = float(input("Enter price of product " + str(i) + ": "))

#     if price >= 5000:
#         discount_rate = 20
#         discount_20 += 1

#     elif price >= 3000:
#         discount_rate = 15
#         discount_15 += 1

#     elif price >= 1000:
#         discount_rate = 10
#         discount_10 += 1

#     else:
#         discount_rate = 0
#         no_discount += 1

#     discount = price * discount_rate / 100
#     final_price = price - discount

#     total_discount += discount

#     print("Original price:", price)
#     print("Discount:", discount)
#     print("Final price:", final_price)
#     print()


# print("20% discount:", discount_20)
# print("15% discount:", discount_15)
# print("10% discount:", discount_10)
# print("No discount:", no_discount)
# print("Total discount:", total_discount)

# # # Q22
# text = input("Enter a string: ")

# compressed = ""
# count = 1   

# for i in range(len(text)):

#     if i < len(text) - 1 and text[i] == text[i + 1]:
#         count += 1

#     else:
#         compressed += text[i] + str(count)
#         count = 1

# print("Compressed string:", compressed)

# # # Q23
# total = 0

# junior = 0
# mid = 0
# senior = 0
# executive = 0

# for i in range(1, 9):
#     salary = float(input("Enter salary of employee " + str(i) + ": "))

#     total += salary

#     if salary < 25000:
#         print("Junior")
#         junior += 1

#     elif salary <= 50000:
#         print("Mid")
#         mid += 1

#     elif salary <= 100000:
#         print("Senior")
#         senior += 1

#     else:
#         print("Executive")
#         executive += 1

# average = total / 8

# print("Junior:", junior)
# print("Mid:", mid)
# print("Senior:", senior)
# print("Executive:", executive)
# print("Average salary:", average)

# # # Q24
# sentence = input("Enter a sentence: ")
# secret = input("Enter secret word: ")

# found = 0
# positions = []

# for i in range(len(sentence) - len(secret) + 1):
#     match = True

#     for j in range(len(secret)):

#         if sentence[i + j] != secret[j]:
#             match = False

#     if match:
#         positions.append(i)
#         found += 1

# if found > 0:
#     print("Secret word found")
#     print("Starting positions:")

#     for position in positions:
#         print(position)

#     print("Number of occurrences:", found)

# else:
#     print("Secret word not found")

# # # Q25
# n = int(input("Enter n: "))

# for row in range(1, n + 1):

#     for number in range(1, row + 1):

#         if number % 3 == 0 and number % 5 == 0:
#             print("F", end=" ")

#         elif number % 3 == 0:
#             print("T", end=" ")

#         elif number % 2 == 0:
#             print("E", end=" ")    

#         else:
#             print("O", end=" ")

#     print()




#26
# poor=0
# average=0
# good=0
# excellent=0
# outstanding=0
# totalrating=0
# for movie in range(1,11):
#     rating=float(input("enter a rating from 1 to 10 "+str(movie)+":"))
#     if 0<=rating<=3:
#         print("poor")
#         poor+=1
#     elif 3.1<=rating<=5:
#         print("average")
#         average+=1
#     elif 5.1<=rating<=7:
#             print("average")
#             good+=1
#     elif 7.1<=rating<=9:
#             print("average")
#             excellent+=1
#     elif 9.1<=rating<=10:
#             print("average")
#             outstanding+=1
#     totalrating+=rating

# print("poor:",poor)
# print("average:",average)
# print("GOOD:",good)
# print("excellent:",excellent)
# print("outstanding:",outstanding)
# avg=totalrating/10
# print("average rating:",avg)


# #27
# sentence = input("Enter a sentence: ")
# words = sentence



# for i in range(len(words)):
#     frequency = 0

#     for j in range(len(words)):
#         if words[i] == words[j]:
#             frequency += 1

#     already_printed = False

#     for k in range(i):
#         if words[i] == words[k]:
#             already_printed = True

#     if frequency > 1 and already_printed == False:
#         print(words[i], ":", frequency)


# #28
# max_even = -1

# numbers = []

# for i in range(10):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# for i in range(10):
#     text = str(numbers[i])
#     even = 0
#     odd = 0

#     for digit in text:
#         if digit.isdigit():
#             if int(digit) % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1

#     if even > max_even:
#         max_even = even

# print("Numbers with maximum even digits:")

# for i in range(10):
#     text = str(numbers[i])
#     even = 0

#     for digit in text:
#         if digit.isdigit() and int(digit) % 2 == 0:
#             even += 1

#     if even == max_even:
#         print(numbers[i])



# #29
# for i in range(5):
#     email = input("Enter email: ")

#     at_count = 0
#     at_position = -1
#     space_found = False

#     for j in range(len(email)):
#         if email[j] == "@":
#             at_count += 1
#             at_position = j

#         if email[j] == " ":
#             space_found = True

#     valid = True

#     if at_count != 1:
#         valid = False

#     if space_found:
#         valid = False

#     if at_position <= 0:
#         valid = False

#     if at_position == len(email) - 1:
#         valid = False

#     dot_found = False

#     if at_position != -1:
#         for j in range(at_position + 1, len(email)):
#             if email[j] == ".":
#                 dot_found = True

#     if dot_found == False:
#         valid = False

#     if valid:
#         print("Valid")
#     else:
#         print("Invalid")


# #30
# text = input("Enter a string: ")

# same = 0
# different = 0
# both_vowels = 0
# both_digits = 0

# for i in range(len(text)):
#     for j in range(i + 1, len(text)):

#         if text[i] == text[j]:
#             same += 1
#         else:
#             different += 1

#         if text[i].lower() in "aeiou" and text[j].lower() in "aeiou":
#             both_vowels += 1

#         if text[i].isdigit() and text[j].isdigit():
#             both_digits += 1

# print("Same characters:", same)
# print("Different characters:", different)
# print("Both vowels:", both_vowels)
# print("Both digits:", both_digits)




# #31
# passed_students = 0
# failed_students = 0

# highest_percentage = 0
# lowest_percentage = 100

# for student in range(5):

#     total = 0
#     passed = True

#     print("Student", student + 1)

#     for subject in range(5):
#         marks = int(input("Enter marks: "))

#         total += marks

#         if marks < 35:
#             passed = False

#     percentage = total / 5

#     if passed:
#         grade = "Pass"
#         passed_students += 1
#     else:
#         grade = "Fail"
#         failed_students += 1

#     print("Total:", total)
#     print("Percentage:", percentage)
#     print("Grade:", grade)

#     if percentage > highest_percentage:
#         highest_percentage = percentage

#     if percentage < lowest_percentage:
#         lowest_percentage = percentage

# print("Passed students:", passed_students)
# print("Failed students:", failed_students)
# print("Highest percentage:", highest_percentage)
# print("Lowest percentage:", lowest_percentage)



# #32
# secret = input("Enter secret password: ")

# for attempt in range(5):

#     password = input("Enter password: ")

#     matching = 0

#     if len(password) < len(secret):
#         minimum = len(password)
#     else:
#         minimum = len(secret)

#     for i in range(minimum):
#         if password[i] == secret[i]:
#             matching += 1

#     correct = True

#     if len(password) != len(secret):
#         correct = False
#     else:
#         for i in range(len(secret)):
#             if password[i] != secret[i]:
#                 correct = False

#     print("Matching characters:", matching)

#     if correct:
#         print("Correct")



# #33
# code = input("Enter product code: ")

# valid = True

# if len(code) != 8:
#     valid = False

# if valid:
#     for i in range(3):
#         if code[i] < "A" or code[i] > "Z":
#             valid = False

# if valid:
#     for i in range(3, 8):
#         if code[i] < "0" or code[i] > "9":
#             valid = False

# if valid:
#     print("Valid Product Code")
# else:
#     print("Invalid Product Code")



# #34
# n = int(input("Enter n: "))

# for row in range(1, n + 1):

#     for num in range(1, row + 1):

#         prime = True

#         if num < 2:
#             prime = False
#         else:
#             for i in range(2, num):
#                 if num % i == 0:
#                     prime = False

#         if prime:
#             print("P", end=" ")
#         elif num % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")

#     print()





# #35
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# word_count = 0
# character_count = 0

# longest = ""
# shortest = ""

# vowel_start = 0
# vowel_end = 0
# digit_words = 0

# for word in words:

#     word_count += 1
#     character_count += len(word)

#     if len(longest) == 0 or len(word) > len(longest):
#         longest = word

#     if len(shortest) == 0 or len(word) < len(shortest):
#         shortest = word

#     if word[0].lower() in "aeiou":
#         vowel_start += 1

#     if word[-1].lower() in "aeiou":
#         vowel_end += 1

#     has_digit = False

#     for character in word:
#         if character.isdigit():
#             has_digit = True

#     if has_digit:
#         digit_words += 1

# print("Number of words:", word_count)
# print("Number of characters:", character_count)
# print("Longest word:", longest)
# print("Shortest word:", shortest)
# print("Words beginning with vowel:", vowel_start)
# print("Words ending with vowel:", vowel_end)
# print("Words containing digits:", digit_words)




# #36
# total_revenue = 0

# for customer in range(5):

#     print("Customer", customer + 1)

#     subtotal = 0

#     for item in range(3):
#         price = float(input("Enter item price: "))
#         subtotal += price

#     if subtotal >= 2000:
#         discount = subtotal * 15 / 100
#     elif subtotal >= 1000:
#         discount = subtotal * 10 / 100
#     else:
#         discount = 0

#     member = input("Is customer a member? yes/no: ")

#     member_discount = 0

#     if member == "yes":
#         member_discount = subtotal * 5 / 100

#     final_bill = subtotal - discount - member_discount

#     print("Subtotal:", subtotal)
#     print("Discount:", discount)
#     print("Member discount:", member_discount)
#     print("Final bill:", final_bill)

#     total_revenue += final_bill

# print("Total restaurant revenue:", total_revenue)


# #37
# word = input("Enter a word: ")

# print("Forward Pattern:")

# for i in range(len(word)):

#     for j in range(i + 1):
#         print(word[j], end="")

#     print()

# print("Reverse Pattern:")

# for i in range(len(word) - 1, -1, -1):

#     for j in range(i + 1):
#         print(word[j], end="")

#     print()




# #38
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# for i in range(len(words)):

#     frequency = 0

#     for j in range(len(words)):
#         if words[i] == words[j]:
#             frequency += 1

#     already_printed = False

#     for k in range(i):
#         if words[i] == words[k]:
#             already_printed = True

#     if frequency >= 2 and already_printed == False:

#         if frequency == 2:
#             classification = "Repeated"

#         elif frequency <= 4:
#             classification = "Frequently Repeated"

#         else:
#             classification = "Highly Repeated"

#         print(words[i], ":", frequency, "-", classification)






# #39
# total_collection = 0

# for passenger in range(8):

#     age = int(input("Enter age: "))
#     distance = float(input("Enter distance: "))

#     base_fare = distance * 10

#     if age < 5:
#         fare = 0

#     elif age <= 12:
#         fare = base_fare * 50 / 100

#     elif age >= 60:
#         fare = base_fare * 70 / 100

#     else:
#         fare = base_fare

#     print("Passenger", passenger + 1)
#     print("Fare:", fare)

#     total_collection += fare

# print("Total collection:", total_collection)





# #40
# first = input("Enter first string: ")
# second = input("Enter second string: ")

# mirror = True

# if len(first) != len(second):
#     mirror = False

# else:
#     for i in range(len(first)):

#         if first[i] != second[len(second) - 1 - i]:
#             mirror = False

# if mirror:
#     print("Mirror-compatible")
# else:
#     print("Not mirror-compatible")



#41
# for student in range(1,8):
#     for day in range(1,6):
#         A=0
#         P=0
#         attendence=input("enter present/absent student"+ str(student) + "day" + str(day) + ":")
#         if attendence.lower()=="present":
#             P+=1
#         else:
#             A+=1
#     percentage_of_attendence=(P/5)*100
#     if percentage_of_attendence>=90:
#         print("exellent")
#     elif percentage_of_attendence>=75:
#         print("good")
#     else:
#         print("Warning!!-")
#     print("attendence percentage:",percentage_of_attendence)



# # 42.

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# main_sum = 0
# secondary_sum = 0
# even_main = 0
# odd_secondary = 0

# for i in range(4):
#     for j in range(4):

#         # Main diagonal
#         if i == j:
#             main_sum += matrix[i][j]

#             if matrix[i][j] % 2 == 0:
#                 even_main += 1

#         # Secondary diagonal
#         if i + j == 3:
#             secondary_sum += matrix[i][j]

#             if matrix[i][j] % 2 != 0:
#                 odd_secondary += 1

# print("Main diagonal sum:", main_sum)
# print("Secondary diagonal sum:", secondary_sum)
# print("Even values on main diagonal:", even_main)
# print("Odd values on secondary diagonal:", odd_secondary)

# # Compare diagonal sums
# if main_sum > secondary_sum:
#     print("Main diagonal sum is greater.")
# elif main_sum < secondary_sum:
#     print("Secondary diagonal sum is greater.")
# else:
#     print("Both diagonal sums are equal.")

        
#43

# text = input("Enter a word: ")
# password = ""

# for ch in text:

#     if ch in "aeiouAEIOU":
#         password += "@"

#     elif ch >= "0" and ch <= "9":
#         password += "#"

#     elif ch == " ":
#         password += "_"

#     elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
#         password += ch.lower()

#     else:
#         password += "!"

# print("Transformed password:", password)






# 44. Bank Account Risk Analyzer

# balance = 1000
# total_deposits = 0
# total_withdrawals = 0

# n = int(input("Enter number of transactions: "))

# for i in range(n):
#     transaction = input("Enter transaction (D/W): ")
#     amount = int(input("Enter amount: "))

#     if transaction == "D":
#         balance += amount
#         total_deposits += amount

#     elif transaction == "W":
#         balance -= amount
#         total_withdrawals += amount

#     # Check account status
#     if balance < 0:
#         print("Overdraft")
#     elif balance < 500:
#         print("Low Balance")
#     else:
#         print("Normal")

# print("Total deposits:", total_deposits)
# print("Total withdrawals:", total_withdrawals)
# print("Final balance:", balance)



# 45. Word Pattern Matching

# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")

# pattern = ""

# # Compare characters up to the shorter word
# if len(word1) < len(word2):
#     length = len(word1)
# else:
#     length = len(word2)

# for i in range(length):
#     if word1[i] == word2[i]:
#         pattern += "S"
#     else:
#         pattern += "D"

# print("Pattern:", pattern)

# # Check for extra characters
# if len(word1) > len(word2):
#     print("Extra characters in first word:", word1[length:])

# elif len(word2) > len(word1):
#     print("Extra characters in second word:", word2[length:])

# else:
#     print("No extra characters.")





# 46. Number Box Pattern

# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):

#         # Border
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")

#         # Inside positions
#         elif (i + j) % 2 == 0:
#             print("E", end="")

#         else:
#             print("O", end="")

#     print()



#47
# Product Stock Analyzer

# out_of_stock = 0
# critical = 0
# low = 0
# available = 0

# highest_quantity = -1
# highest_product = ""

# for i in range(8):
#     name = input("Enter product name: ")
#     quantity = int(input("Enter quantity: "))

#     # Categorize product
#     if quantity == 0:
#         print("Out of Stock")
#         out_of_stock += 1

#     elif quantity <= 5:
#         print("Critical")
#         critical += 1

#     elif quantity <= 20:
#         print("Low")
#         low += 1

#     else:
#         print("Available")
#         available += 1

#     # Find highest quantity
#     if quantity > highest_quantity:
#         highest_quantity = quantity
#         highest_product = name


# print("Out of Stock:", out_of_stock)
# print("Critical:", critical)
# print("Low:", low)
# print("Available:", available)

# print("Product with highest quantity:", highest_product)
# print("Highest quantity:", highest_quantity)




# 48

# for i in range(10):

#     username = input("Enter username: ")

#     letters = 0
#     digits = 0
#     underscores = 0
#     spaces = 0
#     special = 0

#     for ch in username:

#         if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
#             letters += 1

#         elif ch >= "0" and ch <= "9":
#             digits += 1

#         elif ch == "_":
#             underscores += 1

#         elif ch == " ":
#             spaces += 1

#         else:
#             special += 1

#     # Classification
#     if len(username) < 3 or len(username) > 20 or spaces > 0:
#         status = "Invalid"

#     elif len(username) >= 5 and len(username) <= 15 and special == 0:
#         status = "Clean"

#     else:
#         status = "Acceptable"

#     print("Letters:", letters)
#     print("Digits:", digits)
#     print("Underscores:", underscores)
#     print("Spaces:", spaces)
#     print("Special characters:", special)
#     print("Length:", len(username))
#     print("Status:", status)
    



# 49

# sentences = []

# # Take 10 sentences
# for i in range(10):
#     sentence = input("Enter sentence " + str(i + 1) + ": ")
#     sentences.append(sentence)

# search_word = input("Enter search word: ").lower()

# total_occurrences = 0

# for i in range(10):

#     sentence = sentences[i].lower()
#     word_count = 0

#     # Split sentence into words
#     words = sentence.split()

#     # Search manually using loops
#     for word in words:

#         # Remove common punctuation
#         clean_word = ""

#         for ch in word:
#             if ch >= "a" and ch <= "z":
#                 clean_word += ch

#         if clean_word == search_word:
#             word_count += 1

#     if word_count > 0:
#         print("Sentence", i + 1, "contains the word.")
#         print("Occurrences:", word_count)

#     total_occurrences += word_count

# print("Total occurrences:", total_occurrences)



#50
