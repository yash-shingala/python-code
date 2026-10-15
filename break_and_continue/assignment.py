
# # Q1
# for i in range(1, 8):
#     if i == 5: 
#         break
#     print(i)
# print("Finished")

# # Q2
# for ch in "skyline":
#     if ch in "aeiou": 
#         break
#     print(ch)

# # Q3
# n = 2
# while n <= 10:
#     print(n)
#     if n == 6: 
#         break
#     n += 2

# # Q4
# limit = int(input())
# for i in range(1, limit + 1):
#     if i == 7: 
#         break
#     print(i, end=" ")

# # Q5
# word = input()
# target = input()
# for ch in word:
#     print(ch, end=" ")
#     if ch == target: 
#         break

# # Q6
# for n in map(int, input().split()):
#     if n < 0: 
#         break
#     print(n, end=" ")

# # Q7
# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3: 
#             break
#         print(row, col)

# # Q8
# sentence = input().split()
# target = input()
# for word in sentence:
#     if word == target:
#         print("Found")
#         break
# else:
#     print("Not found")

# # Q9
# for i in range(1, 7):
#     if i == 4: 
#         continue
#     print(i)

# # Q10
# for ch in "education":
#     if ch in "aeiou": 
#         continue
#     print(ch, end="")

# # Q11
# n = 0
# while n < 5:
#     n += 1
#     if n == 3: 
#         continue
#     print(n)

# # Q12
# n = int(input())
# for i in range(1, n + 1):
#     if i % 3 == 0: 
#         continue
#     print(i, end=" ")

# # Q13
# word, target = input(), input()
# for ch in word:
#     if ch == target: 
#         continue
#     print(ch, end="")

# # Q14
# for mark in map(int, input().split()):
#     if mark < 40: 
#         continue
#     print(mark, end=" ")

# # Q15
# for i in range(1, 5):
#     if i == 2: 
#         continue
#     print("A", i)
#     print("B", i)

# # Q16
# n = 0
# while n < 5:
#     n += 1
#     if n == 3: 
#         continue
#     print(n)

# # Q17
# count = 0
# for ch in input():
#     if ch in "aeiou":
#         continue
#     count += 1
# print(count)

# # Q18
# for i in range(1, 4):
#     print(i)
# else: 
#     print("Done")

# # Q19
# for i in range(1, 5):
#     if i == 2: 
#         continue
#     print(i)
# else: 
#     print("Completed")

# # Q20
# for i in range(1, 5):
#     if i == 3: 
#         break
#     print(i)
# else: 
#     print("Completed")
# print("Outside loop")

# # Q21
# for item in []: 
#     print("Inside")
# else: 
#     print("Else block")

# # Q22
# nums = list(map(int, input().split()))
# target = int(input())
# for n in nums:
#     if n == target:
#         print("Found")
#         break
# else: 
#     print("Not found")

# # Q23
# word, target = input(), input()
# for ch in word:
#     if ch == target:
#         print("Character exists")
#         break
# else: 
#     print("Character missing")

# # Q24
# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else: 
#     print("Prime")

# # Q25
# values = [2, 4, 6, 8]
# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else: 
#     print("All are even")

# # Q26
# # A: A (continue does not stop the loop)
# # B: Nothing (break prevents else)
# # C: C (empty loop finishes normally)

# # Q27
# word = input()
# for i in range(len(word)):
#     for j in range(i + 1, len(word)):
#         if word[i] == word[j]:
#             print(word[i])
#             break
#     else: 
#         continue
#     break
# else: print("No repeated character")

# # Q28
# for i in range(1, 4):
#     if i == 2: 
#         pass
#     print(i)

# # Q29
# x = 10
# if x > 5: 
#     pass
# print("Finished")

# # Q30
# for letter in "cat": 
#     pass
# print("Loop ended")

# # Q31
# for i in range(1, 6):
#     if i % 2 == 0: 
#         pass
#     print(i)

# # Q32
# choice = int(input())
# if choice == 1: 
#     print("Option 1 selected")
# elif choice == 2: 
#     pass
# else: 
#     print("Unknown option")
# print("Program closed")

# # Q33
# # A prints 1 2 3 4
# # B prints 1 2 4

# # Q34
# for i in range(1, 6):
#     if i == 3: 
#         continue
#     print(i, end=" ")

# # Q35
# for i in range(1, 6):
#     if i == 2: 
#         continue
#     if i == 4:
#         break
#     print(i)
# # Output: 1, 3; else does not run.

# # Q36
# nums = list(map(int, input().split()))
# target = int(input())
# for n in nums:
#     if n < 0: 
#         continue
#     if n == target:
#         print("Target found")
#         break
# else: 
#     print("Target not found")

# # Q37
# nums = list(map(int, input().split()))
# for n in nums:
#     if n == 0: 
#         continue
#     if n == -1: 
#         break
#     print(n, end=" ")
# else: 
#     print("All values processed")

# # Q38
# for row in range(1, 4):
#     for col in range(1, 4):
#         if col == 2: 
#             continue
#         if row == 3: 
#             break
#         print(row, col)
#     else: 
#         print("Inner loop completed")

# # Q39
# nums = list(map(int, input().split()))
# for n in nums:
#     if n < 0:
#         continue
#     if n % 4 == 0 and n % 6 == 0:
#         print("Found:", n)
#         break
# else: print("No matching number")

# # Q40
# # 1. break
# # 2. continue
# # 3. for-else
# # 4. pass
# # 5. continue
# # 6. break
# # 7. for-else
# # 8. pass
