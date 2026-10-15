
# # Q71
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 != 0:
#         result.append(n)
# print(result)

# # Q72
# numbers = [1, 2, 2, 3, 3, 3]
# result = []
# for n in numbers:
#     if n not in result:
#         result.append(n)
# print(result)

# # Q73
# arr1 = [1, 2]
# arr2 = [3, 4]
# result = []
# for n in arr1:
#     result.append(n)
# for n in arr2:
#     result.append(n)
# print(result)

# # Q74
# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5]
# result = []
# for n in arr1:
#     if n in arr2 and n not in result:
#         result.append(n)
# print(result)

# # Q75
# numbers = [1, 2, 3, 4]
# if len(numbers) > 0:
#     result = [numbers[-1]]
#     for i in range(len(numbers) - 1):
#         result.append(numbers[i])
# else:
#     result = []
# print(result)

# # Q76
# numbers = [1, 2, 3, 4]
# if len(numbers) > 0:
#     result = []
#     for i in range(1, len(numbers)):
#         result.append(numbers[i])
#     result.append(numbers[0])
# else:
#     result = []
# print(result)

# # Q77
# numbers = [1, 2, 3, 4, 5]
# total = 0
# count = 0
# if len(numbers) > 0:
#     for n in numbers:
#         total += n
#     average = total / len(numbers)
#     for n in numbers:
#         if n > average:
#             count += 1
# print(count)

# # Q78
# numbers = [-5, -1, 3, 7, -2]
# largest = None
# smallest = None
# for n in numbers:
#     if n > 0 and (largest is None or n > largest):
#         largest = n
#     elif n < 0 and (smallest is None or n < smallest):
#         smallest = n
# print("Largest positive:", largest)
# print("Smallest negative:", smallest)

# # Q79
# numbers = [0, 1, 0, 1, 1]
# zeros = 0
# ones = 0
# for n in numbers:
#     if n == 0:
#         zeros += 1
#     else:
#         ones += 1
# print("Zeros:", zeros)
# print("Ones:", ones)

# # Q80
# numbers = [1, 2, 3, 4, 5]
# evens = []
# odds = []
# for n in numbers:
#     if n % 2 == 0:
#         evens.append(n)
#     else:
#         odds.append(n)
# print("Evens:", evens)
# print("Odds:", odds)