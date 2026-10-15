

# Q1. 
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# Q2.
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i, "x", j, "=", i * j)

# Q3.
# ch = input("Character: ")
# rows = int(input("Rows: "))
# cols = int(input("Columns: "))
# for i in range(rows):
#     for j in range(cols):
#         print(ch, end="")
#     print()

# Q4. 
# rows = int(input("Rows: "))
# cols = int(input("Columns: "))
# for i in range(rows):
#     for j in range(cols):
#         print(f"({i},{j})", end=" ")
#     print()

# Q5.
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(n):
#         print(i, end="")
#     print()

# Q6.
# n = int(input("Enter N: "))
# for i in range(n):
#     for j in range(1, n + 1):
#         print(j, end="")
#     print()

# Q7. 
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# Q8. 
# n = int(input("Enter N: "))
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# Q9. 
# rows = int(input("Rows: "))
# cols = int(input("Columns: "))
# for i in range(rows):
#     for j in range(cols):
#         print("*", end="")
#     print()

# Q10. 
# n = int(input("Enter N: "))
# for i in range(n):
#     for j in range(n):
#         print(j % 2, end="")
#     print()

# Q11. 
# rows = int(input("Rows: "))
# cols = int(input("Columns: "))
# for i in range(rows):
#     for j in range(1, cols + 1):
#         if j % 2 == 0:
#             print(j, end=" ")
#     print()

# Q12. 
# n = int(input("Enter N: "))
# for i in range(n):
#     for j in range(1, n + 1):
#         if j % 2 == 1:
#             print(j, end=" ")
#     print()

# Q13. 
# for i in range(1, 5):
#     for j in range(1, 5):
#         if (i + j) % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")
#     print()

# Q14.
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             print("Same", end=" ")
#         else:
#             print("Different", end=" ")
#     print()

# Q15. Diagonal Values
# n = int(input("Enter N: "))
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()

# Q16. Number Divisibility Grid
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i % j == 0:
#             print("X", end=" ")
#         else:
#             print("-", end=" ")
#     print()

# Q17. Multiples Detector
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j % i == 0:
#             print(j, end=" ")
#     print()

# Q18. Pair Sum Filter
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j > n:
#             print(i, j)

# Q19. Pair Product Filter
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         product = i * j
#         if product % 2 == 0:
#             print(i, j, product)

# Q20. Special Coordinate
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             print("SPECIAL", end=" ")
#         elif i + j == n:
#             print("PAIR", end=" ")
#         else:
#             print("NORMAL", end=" ")
#     print()

# Q21. Character Repetition
# word = input("Enter a word: ")
# for ch in word:
#     for j in range(3):
#         print(ch, end="")
#     print()

# Q22. Character with Position
# word = input("Enter a word: ")
# for ch in word:
#     for j in range(3):
#         print(ch, j)

# Q23. Compare Every Character
# word = input("Enter a word: ")
# for a in word:
#     for b in word:
#         if a == b:
#             print(a, "/", b, "is Same")
#         else:
#             print(a, "/", b, "is Different")

# Q24. Character Matching
# first = input("First string: ")
# second = input("Second string: ")
# for a in first:
#     for b in second:
#         if a == b:
#             print(a, b)

# Q25. Count Matching Character Comparisons
# first = input("First string: ")
# second = input("Second string: ")
# total = 0
# for a in first:
#     for b in second:
#         if a == b:
#             total += 1
# print(total)

# Q26. Character Frequency Without count()
# word = input("Enter a word: ")
# for i in range(len(word)):
#     already_seen = False
#     for k in range(i):
#         if word[k] == word[i]:
#             already_seen = True
#     if not already_seen:
#         frequency = 0
#         for ch in word:
#             if ch == word[i]:
#                 frequency += 1
#         print(word[i], "=", frequency)

# Q27. Vowel-Consonant Classification
# word = input("Enter a word: ")
# vowels = "AEIOUaeiou"
# for ch in word:
#     is_vowel = False
#     for v in vowels:
#         if ch == v:
#             is_vowel = True
#     if is_vowel:
#         print(ch, "= Vowel")
#     elif ch.isalpha():
#         print(ch, "= Consonant")

# Q28. Common Characters (no set)
# first = input("First string: ")
# second = input("Second string: ")
# for i in range(len(first)):
#     found = False
#     for ch in second:
#         if first[i] == ch:
#             found = True
#     earlier = False
#     for k in range(i):
#         if first[k] == first[i]:
#             earlier = True
#     if found and not earlier:
#         print(first[i])

# Q29. Character Pair Generator
# word = input("Enter a word: ")
# for a in word:
#     for b in word:
#         print(a, b)

# Q30. Different Character Pairs
# word = input("Enter a word: ")
# for i in range(len(word)):
#     for j in range(len(word)):
#         if i != j:
#             print(word[i], word[j])

# Q31. Same or Different Pair
# word = input("Enter a word: ")
# for a in word:
#     for b in word:
#         if a == b:
#             print(a, b, "Same")
#         else:
#             print(a, b, "Different")

# Q32. Vowel-Consonant Pair
# word = input("Enter a word: ")
# vowels = "AEIOUaeiou"
# for a in word:
#     for b in word:
#         if a in vowels and b.isalpha() and b not in vowels:
#             print(a, b)

# Q33. Same Case Pair
# word = input("Enter a word: ")
# for a in word:
#     for b in word:
#         if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
#             print(a, b)

# Q34. ASCII Difference
# word = input("Enter a word: ")
# for a in word:
#     for b in word:
#         print(a, b, "->", abs(ord(a) - ord(b)))

# Q35. ASCII Relationship
# word = input("Enter a word: ")
# for a in word:
#     for b in word:
#         if ord(a) < ord(b):
#             result = "Increasing"
#         elif ord(a) > ord(b):
#             result = "Decreasing"
#         else:
#             result = "Same"
#         print(a, b, result)




# Q36. Compare Words
# words = input("Enter a sentence: ").split()
# for a in words:
#     for b in words:
#         print(a, b)

# Q37. Same-Length Word Pairs
# words = input("Enter words: ").split()
# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         if len(words[i]) == len(words[j]):
#             print(words[i], words[j])

# Q38. Common Starting Character
# words = input("Enter words: ").split()
# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         if words[i][0] == words[j][0]:
#             print(words[i], words[j])

# Q39. Common Ending Character
# words = input("Enter words: ").split()
# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         if words[i][-1] == words[j][-1]:
#             print(words[i], words[j])

# Q40. Word Pairs Sharing at Least One Character (no set)
# words = input("Enter words: ").split()
# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         common = False
#         for a in words[i]:
#             for b in words[j]:
#                 if a == b:
#                     common = True
#         if common:
#             print(words[i], words[j])

# Q41. Word Length Difference
# words = input("Enter words: ").split()
# for a in words:
#     for b in words:
#         difference = len(a) - len(b)
#         if difference < 0:
#             difference = -difference
#         print(a, b, "difference =", difference)

# Q42. Longest and Shortest Word (no max/min)
# words = input("Enter words: ").split()
# longest = words[0]
# shortest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word
#     if len(word) < len(shortest):
#         shortest = word
# print("Longest =", longest)
# print("Shortest =", shortest)

# Q43. Growing Inner Loop
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Q44. Shrinking Inner Loop
# n = int(input("N: "))
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Q45. Multiplication Triangle
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i * j, end=" ")
#     print()

# Q46. Conditional Dynamic Loop — print even inner values
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(j, end=" ")
#     print()

# Q47. Dynamic Range Based on Input
# n = int(input("N: "))
# for i in range(n):
#     for j in range(i):
#         print(j, end=" ")
#     print()

# Q48. Reverse Dynamic Range
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# Q49. Factors of Every Number
# n = int(input("N: "))
# for number in range(1, n + 1):
#     print(number, "->", end=" ")
#     for divisor in range(1, number + 1):
#         if number % divisor == 0:
#             print(divisor, end=" ")
#     print()

# Q50. Perfect Numbers Up to N
# n = int(input("N: "))
# for number in range(2, n + 1):
#     total = 0
#     for divisor in range(1, number):
#         if number % divisor == 0:
#             total += divisor
#     if total == number:
#         print("Perfect:", number)

# Q51. Prime Numbers Using Nested Loops
# n = int(input("N: "))
# for number in range(2, n + 1):
#     factors = 0
#     for divisor in range(1, number + 1):
#         if number % divisor == 0:
#             factors += 1
#     if factors == 2:
#         print(number, end=" ")

# Q52. Prime Factor Display (factors of each prime)
# n = int(input("N: "))
# for number in range(2, n + 1):
#     factors = 0
#     for d in range(1, number + 1):
#         if number % d == 0:
#             factors += 1
#     if factors == 2:
#         print(number, "->", end=" ")
#         for d in range(1, number + 1):
#             if number % d == 0:
#                 print(d, end=" ")
#         print()

# Q53. Common Factors
# a = int(input("A: "))
# b = int(input("B: "))
# for d in range(1, a + 1):
#     if a % d == 0 and b % d == 0:
#         print(d, end=" ")

# Q54. Common Multiples up to a Limit
# a = int(input("A: "))
# b = int(input("B: "))
# limit = int(input("Limit: "))
# for x in range(1, limit + 1):
#     if x % a == 0 and x % b == 0:
#         print(x, end=" ")

# Q55. Pair With Greatest Product (positive values 1..N)
# n = int(input("N: "))
# best_i = 1
# best_j = 1
# best_product = 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i * j > best_product:
#             best_product = i * j
#             best_i = i
#             best_j = j
# print("Pair =", best_i, best_j)
# print("Product =", best_product)

# Q56. Pair With Target Sum
# n = int(input("N: "))
# target = int(input("Target: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j == target:
#             print(i, j)

# Q57. Right Triangle
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

# Q58. Number Triangle
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# Q59. Repeated Number Triangle
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end="")
#     print()

# Q60. Inverted Triangle
# n = int(input("N: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

# Q61. Right-Aligned Triangle
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

# Q62. Number Pyramid
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         print(j, end="")
#     print()

# Q63. Repeated Number Pyramid
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print(i, end="")
#     print()

# Q64. Inverted Number Pyramid
# n = int(input("N: "))
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         print(j, end="")
#     print()

# Q65. Diamond Pattern
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# Q66. Hollow Rectangle
# rows = int(input("Rows: "))
# cols = int(input("Columns: "))
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# Q67. Hollow Triangle
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         if j == 0 or j == i - 1 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# Q68. Number Border Pattern
# n = int(input("N: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("1", end="")
#         else:
#             print("0", end="")
#     print()

# Q69. Diagonal Cross
# n = int(input("N: "))
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# Q70. Number and Character Grid
# word = input("Word: ")
# n = int(input("N: "))
# for i in range(n):
#     for j in range(1, n + 1):
#         if i < len(word):
#             print(word[i] + str(j), end=" ")
#     print()

# Q71. Character + ASCII Filter
# word = input("Word: ")
# for a in word:
#     for b in word:
#         difference = ord(a) - ord(b)
#         if difference < 0:
#             difference = -difference
#         if difference > 5:
#             print(a, b)

# Q72. Word Pair Analyzer
# words = input("Enter words: ").split()
# for a in words:
#     for b in words:
#         if a[0] == b[0]:
#             comparison = "Same"
#         else:
#             comparison = "Different"
#         print(a, len(a), b, len(b), comparison)

# Q73. Student Marks Matrix (3 students, 4 subjects)
# for student in range(1, 4):
#     total = 0
#     for subject in range(1, 5):
#         mark = int(input("Enter mark: "))
#         total += mark
#     print("Student", student, "Total =", total, "Average =", total / 4)

# Q74. Multiplication Table Matrix
# n = int(input("N: "))
# for i in range(1, n + 1):
#     print("Table of", i)
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

# Q75. Attendance Checker
# for student in range(1, 3):
#     present = 0
#     absent = 0
#     for day in range(4):
#         status = input("Enter P/A: ").upper()
#         if status == "P":
#             present += 1
#         else:
#             absent += 1
#     print("Student", student, "Present =", present, "Absent =", absent)

# Q76. Mini Seating System
# rows = int(input("Rows (up to 26): "))
# cols = int(input("Columns: "))
# for i in range(rows):
#     for j in range(1, cols + 1):
#         print(chr(65 + i) + str(j), end=" ")
#     print()

# Q77. Ticket Price Grid (odd seat 100, even seat 150)
# rows = int(input("Rows: "))
# seats = int(input("Seats per row: "))
# for i in range(rows):
#     for j in range(1, seats + 1):
#         if j % 2 == 1:
#             print(100, end=" ")
#         else:
#             print(150, end=" ")
#     print()

# Q78. Classroom Attendance Summary
# attendance = []
# for student in range(2):
#     row = []
#     for day in range(4):
#         row.append(input("Enter P/A: ").upper())
#     attendance.append(row)
# best_student = 0
# best_count = -1
# for i in range(2):
#     present = 0
#     for j in range(4):
#         if attendance[i][j] == "P":
#             present += 1
#     print("Student", i + 1, "Present =", present)
#     if present > best_count:
#         best_count = present
#         best_student = i + 1
# print("Highest attendance: Student", best_student)

# Q79. Duplicate Character Detector
# word = input("Word: ")
# for i in range(len(word)):
#     repeated = False
#     for j in range(i):
#         if word[i] == word[j]:
#             repeated = True
#     if not repeated:
#         frequency = 0
#         for ch in word:
#             if ch == word[i]:
#                 frequency += 1
#         if frequency > 1:
#             print(word[i])

# Q80. First Repeated Character
# word = input("Word: ")
# answer = ""
# for i in range(len(word)):
#     for j in range(i):
#         if word[i] == word[j] and answer == "":
#             answer = word[i]
# if answer == "":
#     print("No repeated character")
# else:
#     print(answer)

# Q81. Remove Duplicate Characters
# word = input("Word: ")
# result = ""
# for ch in word:
#     already_seen = False
#     for old in result:
#         if ch == old:
#             already_seen = True
#     if not already_seen:
#         result += ch
# print(result)

# Q82. Anagram Checker (case-sensitive, ignores spaces only if removed)
# first = input("First word: ").replace(" ", "")
# second = input("Second word: ").replace(" ", "")
# if len(first) != len(second):
#     print("Not anagram")
# else:
#     matched = True
#     for ch in first:
#         count_first = 0
#         count_second = 0
#         for a in first:
#             if a == ch:
#                 count_first += 1
#         for b in second:
#             if b == ch:
#                 count_second += 1
#         if count_first != count_second:
#             matched = False
#     if matched:
#         print("Anagram")
#     else:
#         print("Not anagram")

# Q83. Common Words
# first = input("First sentence: ").split()
# second = input("Second sentence: ").split()
# for i in range(len(first)):
#     found = False
#     for word in second:
#         if first[i] == word:
#             found = True
#     earlier = False
#     for k in range(i):
#         if first[k] == first[i]:
#             earlier = True
#     if found and not earlier:
#         print(first[i])

# Q84. Duplicate Words
# words = input("Sentence: ").split()
# for i in range(len(words)):
#     earlier = False
#     for j in range(i):
#         if words[i] == words[j]:
#             earlier = True
#     frequency = 0
#     for word in words:
#         if word == words[i]:
#             frequency += 1
#     if frequency > 1 and not earlier:
#         print(words[i])

# Q85. Unique Words
# words = input("Sentence: ").split()
# for i in range(len(words)):
#     frequency = 0
#     for word in words:
#         if word == words[i]:
#             frequency += 1
#     if frequency == 1:
#         print(words[i])

# Q86. Palindrome Word Analyzer (no slicing)
# words = input("Words: ").split()
# for word in words:
#     palindrome = True
#     for i in range(len(word) // 2):
#         if word[i] != word[len(word) - 1 - i]:
#             palindrome = False
#     if palindrome:
#         print(word, "is a palindrome")

# Q87. Longest Palindromic Word
# words = input("Words: ").split()
# longest = ""
# for word in words:
#     palindrome = True
#     for i in range(len(word) // 2):
#         if word[i] != word[len(word) - 1 - i]:
#             palindrome = False
#     if palindrome and len(word) > len(longest):
#         longest = word
# print(longest if longest != "" else "No palindrome")

# Q88. Maximum Common Character Frequency
# first = input("First string: ")
# second = input("Second string: ")
# best_char = ""
# best_frequency = 0
# for ch in first:
#     already_seen = False
#     for old in first:
#         if old == ch:
#             break
#     for i in range(len(first)):
#         if first[i] == ch:
#             for j in range(i):
#                 if first[j] == ch:
#                     already_seen = True
#     if not already_seen:
#         f1 = 0
#         f2 = 0
#         for a in first:
#             if a == ch:
#                 f1 += 1
#         for b in second:
#             if b == ch:
#                 f2 += 1
#         if f1 > 0 and f2 > 0 and f1 + f2 > best_frequency:
#             best_frequency = f1 + f2
#             best_char = ch
# print("Character =", best_char, "Frequency total =", best_frequency)

# Q89. Most Repeated Character
# word = input("Word: ")
# best_char = ""
# best_count = 0
# for i in range(len(word)):
#     earlier = False
#     for j in range(i):
#         if word[j] == word[i]:
#             earlier = True
#     if not earlier:
#         frequency = 0
#         for ch in word:
#             if ch == word[i]:
#                 frequency += 1
#         if frequency > best_count:
#             best_count = frequency
#             best_char = word[i]
# print(best_char)

# Q90. Second Most Repeated Character; ties are allowed
# word = input("Word: ")
# first_count = 0
# second_count = 0
# first_char = ""
# second_chars = ""
# for i in range(len(word)):
#     earlier = False
#     for j in range(i):
#         if word[j] == word[i]:
#             earlier = True
#     if not earlier:
#         frequency = 0
#         for ch in word:
#             if ch == word[i]:
#                 frequency += 1
#         if frequency > first_count:
#             second_count = first_count
#             second_chars = first_char
#             first_count = frequency
#             first_char = word[i]
#         elif frequency == first_count:
#             if second_chars == "":
#                 second_count = frequency
#                 second_chars = word[i]
#         elif frequency > second_count:
#             second_count = frequency
#             second_chars = word[i]
# print("Highest:", first_char, first_count)
# print("Second level:", second_chars, second_count)

# Q91. Word Pair With Maximum Common Characters (distinct shared letters)
# words = input("Enter words: ").split()
# best_a = ""
# best_b = ""
# best_count = -1
# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         common_count = 0
#         for ch in words[i]:
#             found = False
#             for other in words[j]:
#                 if ch == other:
#                     found = True
#             earlier = False
#             for old in words[i]:
#                 if old == ch:
#                     break
#             for k in range(words[i].index(ch)):
#                 if words[i][k] == ch:
#                     earlier = True
#             if found and not earlier:
#                 common_count += 1
#         if common_count > best_count:
#             best_count = common_count
#             best_a = words[i]
#             best_b = words[j]
# print(best_a, best_b, "Common characters =", best_count)

# Q92. Number Pair With Common Digits
# a = input("First number: ")
# b = input("Second number: ")
# common = 0
# for x in a:
#     found = False
#     for y in b:
#         if x == y:
#             found = True
#     if found:
#         common += 1
# print("Common digit count =", common)

# Q93. Digit Pair Analyzer
# number = input("Enter number: ")
# for a in number:
#     for b in number:
#         if int(a) < int(b):
#             print(a, b, "Increasing")
#         elif int(a) > int(b):
#             print(a, b, "Decreasing")
#         else:
#             print(a, b, "Same")

# Q94. Armstrong Numbers in a Range
# n = int(input("N: "))
# for number in range(1, n + 1):
#     digits = str(number)
#     total = 0
#     for digit in digits:
#         total += int(digit) ** len(digits)
#     if total == number:
#         print(number, end=" ")

# Q95. Prime Pair Generator: distinct pairs i < j, prime sum
# n = int(input("N: "))
# for i in range(2, n + 1):
#     for j in range(i + 1, n + 1):
#         total = i + j
#         factors = 0
#         for d in range(1, total + 1):
#             if total % d == 0:
#                 factors += 1
#         if factors == 2:
#             print(i, "+", j, "=", total)

# Q96. Restaurant Table Availability (1=available, 0=occupied)
# rows = int(input("Rows: "))
# cols = int(input("Tables per row: "))
# available = 0
# occupied = 0
# for i in range(rows):
#     row_available = 0
#     for j in range(cols):
#         status = int(input("Enter 1 available / 0 occupied: "))
#         if status == 1:
#             available += 1
#             row_available += 1
#         else:
#             occupied += 1
#     print("Row", i + 1, "available =", row_available)
# print("Available =", available, "Occupied =", occupied)

# Q97. Cinema Seat Booking (O=open, B=booked)
# rows = int(input("Rows: "))
# cols = int(input("Seats per row: "))
# open_total = 0
# booked_total = 0
# best_row = 1
# best_open = -1
# for i in range(rows):
#     row_open = 0
#     for j in range(cols):
#         seat = input("O or B: ").upper()
#         if seat == "O":
#             open_total += 1
#             row_open += 1
#         else:
#             booked_total += 1
#     print("Row", i + 1, "open =", row_open)
#     if row_open > best_open:
#         best_open = row_open
#         best_row = i + 1
# print("Open =", open_total, "Booked =", booked_total)
# print("Most open seats: Row", best_row)

# Q98. Shopping Cart Price Matrix
# customers = int(input("Customers: "))
# products = int(input("Products: "))
# prices = []
# for j in range(products):
#     prices.append(float(input("Price of product: ")))
# product_totals = [0] * products
# for i in range(customers):
#     bill = 0
#     for j in range(products):
#         quantity = int(input("Quantity: "))
#         bill += quantity * prices[j]
#         product_totals[j] += quantity
#     print("Customer", i + 1, "total =", bill)
# print("Product quantities:", product_totals)

# Q99. Exam Marks Analyzer
# students = int(input("Students: "))
# subjects = int(input("Subjects: "))
# highest_total = -1
# highest_student = 0
# for i in range(students):
#     total = 0
#     for j in range(subjects):
#         total += int(input("Mark: "))
#     print("Student", i + 1, "total =", total)
#     if total > highest_total:
#         highest_total = total
#         highest_student = i + 1
# print("Highest total: Student", highest_student, highest_total)

# Q100. Bus Seat Reservation (1=booked, 0=available)
# rows = int(input("Rows: "))
# available = 0
# booked = 0
# full_rows = 0
# for i in range(rows):
#     row_booked = 0
#     for j in range(2):
#         status = int(input("Enter 1 booked / 0 available: "))
#         if status == 1:
#             booked += 1
#             row_booked += 1
#         else:
#             available += 1
#     if row_booked == 2:
#         full_rows += 1
# print("Available =", available, "Booked =", booked)
# print("Fully booked rows =", full_rows)

# Q101. Pattern + Condition Challenge (A main diagonal, B opposite; center A priority)
# n = int(input("N: "))
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print("A", end=" ")
#         elif i + j == n - 1:
#             print("B", end=" ")
#         else:
#             print("-", end=" ")
#     print()

# Q102. Character Pyramid (progressively larger prefixes, centered)
# word = input("Word: ")
# for i in range(1, len(word) + 1):
#     print(" " * (len(word) - i) + word[:i])

# Q103. Word Pyramid
# words = input("Sentence: ").split()
# for i in range(1, len(words) + 1):
#     for j in range(i):
#         print(words[j], end=" ")
#     print()

# Q104. Reverse Word Pyramid
# words = input("Sentence: ").split()
# for i in range(len(words), 0, -1):
#     for j in range(i):
#         print(words[j], end=" ")
#     print()

# Q105. Word Length Pattern
# words = input("Sentence: ").split()
# for word in words:
#     print(word, "*" * len(word))

# Q106. Character Frequency Pattern (no count)
# word = input("Word: ")
# for i in range(len(word)):
#     earlier = False
#     for j in range(i):
#         if word[j] == word[i]:
#             earlier = True
#     if not earlier:
#         frequency = 0
#         for ch in word:
#             if ch == word[i]:
#                 frequency += 1
#         print(word[i], "*" * frequency)

# Q107. Number Triangle With Conditions
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i == j:
#             print("X", end=" ")
#         elif j % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")
#     print()

# Q108. Multiplication Pattern Challenge
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         value = i * j
#         if value % 15 == 0:
#             print("Z", end=" ")
#         elif value % 3 == 0:
#             print("X", end=" ")
#         elif value % 5 == 0:
#             print("Y", end=" ")
#         else:
#             print(value, end=" ")
#     print()

# Q109. Student Performance Matrix (totals, averages, pass/fail, high/low)
# n = int(input("Students: "))
# m = int(input("Subjects: "))
# highest = -1
# highest_student = 0
# lowest = None
# lowest_student = 0
# for i in range(n):
#     total = 0
#     passed = True
#     for j in range(m):
#         mark = int(input("Mark: "))
#         total += mark
#         if mark < 35:
#             passed = False
#         if lowest is None or mark < lowest:
#             lowest = mark
#             lowest_student = i + 1
#     print("Student", i + 1, "Total =", total, "Average =", total / m,
#           "Result =", "Pass" if passed else "Fail")
#     if total > highest:
#         highest = total
#         highest_student = i + 1
# print("Highest total student =", highest_student, highest)
# print("Lowest individual mark =", lowest, "Student", lowest_student)

# Q110. Matrix Border and Diagonal Analyzer
# n = int(input("Square matrix size: "))
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(int(input("Value: ")))
#     matrix.append(row)
# total = border = main_diag = other_diag = 0
# for i in range(n):
#     for j in range(n):
#         value = matrix[i][j]
#         total += value
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             border += value
#         if i == j:
#             main_diag += value
#         if i + j == n - 1:
#             other_diag += value
# print("Total =", total, "Border =", border)
# print("Main diagonal =", main_diag, "Opposite diagonal =", other_diag)
# print("Inner =", total - border)

# Q111. Matrix Comparison
# n = int(input("N: "))
# a = []
# b = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(int(input("A value: ")))
#     a.append(row)
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(int(input("B value: ")))
#     b.append(row)
# equal = different = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == b[i][j]:
#             equal += 1
#         else:
#             different += 1
# print("Equal positions =", equal, "Different positions =", different)

# Q112. Matrix Addition
# n = int(input("Rows: "))
# m = int(input("Columns: "))
# a = []
# b = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(int(input("A value: ")))
#     a.append(row)
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(int(input("B value: ")))
#     b.append(row)
# for i in range(n):
#     for j in range(m):
#         print(a[i][j] + b[i][j], end=" ")
#     print()

# Q113. Matrix Multiplication (A is rows×middle, B is middle×cols)
# rows = int(input("A rows: "))
# middle = int(input("A columns / B rows: "))
# cols = int(input("B columns: "))
# a = []
# b = []
# for i in range(rows):
#     row = []
#     for j in range(middle):
#         row.append(int(input("A value: ")))
#     a.append(row)
# for i in range(middle):
#     row = []
#     for j in range(cols):
#         row.append(int(input("B value: ")))
#     b.append(row)
# result = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         total = 0
#         for k in range(middle):
#             total += a[i][k] * b[k][j]
#         row.append(total)
#     result.append(row)
# for row in result:
#     for value in row:
#         print(value, end=" ")
#     print()

# Q114. Tic-Tac-Toe Board Analyzer
# board = []
# for i in range(3):
#     board.append(input("Enter 3 symbols (e.g. X O -), separated by spaces: ").upper().split())
# winner = ""
# for i in range(3):
#     if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
#         winner = board[i][0]
#     if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
#         winner = board[0][i]
# if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
#     winner = board[0][0]
# if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
#     winner = board[0][2]
# if winner:
#     print(winner, "wins")
# else:
#     empty = False
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == "-":
#                 empty = True
#     print("Incomplete" if empty else "Draw")

# Q115. Word Search Grid
# rows = int(input("Rows: "))
# cols = int(input("Columns: "))
# grid = []
# for i in range(rows):
#     grid.append(input("Enter row characters without spaces: "))
# target = input("Target character: ")
# for i in range(rows):
#     for j in range(cols):
#         if grid[i][j] == target:
#             print("Found at row", i, "column", j)

# Q116. Password Character Analyzer
# password = input("Password: ")
# upper = lower = digits = special = 0
# for ch in password:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     elif ch.isdigit():
#         digits += 1
#     else:
#         special += 1
# print("Uppercase =", upper, "Lowercase =", lower)
# print("Digits =", digits, "Special =", special)

# Q117. Mini Inventory System
# products = int(input("Products: "))
# stores = int(input("Stores: "))
# store_totals = [0] * stores
# for i in range(products):
#     product_total = 0
#     for j in range(stores):
#         stock = int(input("Stock: "))
#         product_total += stock
#         store_totals[j] += stock
#     print("Product", i + 1, "total =", product_total)
# for j in range(stores):
#     print("Store", j + 1, "total =", store_totals[j])

# Q118. Cricket Score Matrix
# players = int(input("Players: "))
# matches = int(input("Matches: "))
# highest = -1
# best_player = 0
# for i in range(players):
#     total = 0
#     for j in range(matches):
#         total += int(input("Runs: "))
#     print("Player", i + 1, "total =", total)
#     if total > highest:
#         highest = total
#         best_player = i + 1
# print("Highest scorer: Player", best_player, highest)

# Q119. Electricity Usage Analyzer
# houses = int(input("Houses: "))
# months = int(input("Months: "))
# month_totals = [0] * months
# highest_month = 0
# highest_usage = -1
# for i in range(houses):
#     total = 0
#     for j in range(months):
#         usage = int(input("Usage: "))
#         total += usage
#         month_totals[j] += usage
#     print("House", i + 1, "total =", total)
# for j in range(months):
#     if month_totals[j] > highest_usage:
#         highest_usage = month_totals[j]
#         highest_month = j + 1
# print("Highest total usage month =", highest_month, highest_usage)

# Q120. Final Multi-Level Data Analyzer (student totals, averages, subject totals, pass/fail)
# n = int(input("Students: "))
# m = int(input("Subjects: "))
# subject_totals = [0] * m
# highest_total = -1
# best_student = 0
# for i in range(n):
#     total = 0
#     passed = True
#     for j in range(m):
#         mark = int(input("Mark: "))
#         total += mark
#         subject_totals[j] += mark
#         if mark < 35:
#             passed = False
#     print("Student", i + 1, "total =", total, "average =", total / m,
#           "result =", "Pass" if passed else "Fail")
#     if total > highest_total:
#         highest_total = total
#         best_student = i + 1
# for j in range(m):
#     print("Subject", j + 1, "total =", subject_totals[j])
# print("Highest total: Student", best_student, highest_total)

