
# # Q61. 
# arr = [1, 2, 3]
# result = []
# for x in arr:
#     result.append(x * 2)
# print("Q61:", result)

# # Q62.
# arr = [1, 2, 3]
# result = []
# for x in arr:
#     result.append(x * x)
# print("Q62:", result)

# # Q63.
# arr = [1, 2, 3]
# result = []
# for i in range(len(arr) - 1, -1, -1):
#     result.append(arr[i])
# print("Q63:", result)

# # Q64.
# arr = [1, 2, 3]
# result = []
# for x in arr:
#     result.append(x)
# print("Q64:", result)

# # Q65.
# arr = [1, 2, 3]
# value = 2
# found = False
# for x in arr:
#     if x == value:
#         found = True
# print("Q65:", found)

# # Q66. 
# arr = [10, 20, 30]
# value = 20
# index = -1
# for i in range(len(arr)):
#     if arr[i] == value:
#         index = i
#         break
# print("Q66:", index)

# # Q67. 
# arr = [1, 2, 2, 3, 2]
# value = 2
# count = 0
# for x in arr:
#     if x == value:
#         count += 1
# print("Q67:", count)

# # Q68. 
# arr = [1, 2, 2, 3]
# sorted_array = True
# for i in range(1, len(arr)):
#     if arr[i] < arr[i - 1]:
#         sorted_array = False
#         break
# print("Q68:", sorted_array)

# Q69
# arr = [10, 5, 8, 20]
# largest = float("-inf")
# second = float("-inf")
# for x in arr:
#     if x > largest:
#         second = largest
#         largest = x
#     elif largest > x > second:
#         second = x
# print("Q69:", second)

# Q70
# arr = [10, 5, 8, 20]
# smallest = float("inf")
# second = float("inf")
# for x in arr:
#     if x < smallest:
#         second = smallest
#         smallest = x
#     elif smallest < x < second:
#         second = x
# print("Q70:", second)
