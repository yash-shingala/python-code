n = int(input("enter a number:"))

# Q81
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# Q82
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # Q83. 
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# # Q84. 
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# # Q85. 
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print()

# # Q86
# arr = [[1, 2, 3], [4, 5, 6]]
# sums = []
# for row in arr:
#     total = 0
#     for num in row:
#         total += num
#     sums.append(total)
# print(sums)

# # Q87.
# n = 16
# square = False
# if n >= 0:
#     for i in range(n + 1):
#         if i * i == n:
#             square = True
#             break
# print(square)

# # Q88.
# n = 153
# temp = n
# total = 0
# while temp > 0:
#     digit = temp % 10
#     total += digit ** 3
#     temp //= 10
# print(total == n)

# # Q89.
# words = ["hi", "hello", "a"]
# lengths = []
# for word in words:
#     lengths.append(len(word))
# print(lengths)

# # Q90
# words = ["hi", "hello", "hey"]
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)