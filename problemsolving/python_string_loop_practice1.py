#1.
# str=input("Enter a string: ")
# target=input("Enter a target sub string: ")
# found=False
# for i in range(len(str)):
#     count=0
#     for j in range(len(target)):
#         if i+j<len(str) and str[i+j]==target[j]:
#             count=count+1
#         else:
#             break

#     if count==len(target):
#         found=True
#         break

# if found:
#     print("Caught!")
# else:
#     print("Escaped!")



#2.
# S = input()
# result = ""
# i = 0
# while i < len(S):
#     letter = S[i]
#     count = int(S[i + 1])
#     for j in range(count):
#         result = result + letter

#     i = i + 2
# print(result)



#3
# def is_palindrome(S):
#     length = len(S)
#     for i in range(length // 2):
#         if S[i] != S[length - 1 - i]:
#             return False
#     return True

# def check_palindrome(N, S):
#     half = N // 2
#     first = S[:half]
#     second = S[half:]

#     if is_palindrome(first) and is_palindrome(second):
#         print("yes")
#     else:
#         print("no")

# N = int(input("enter the length of the string: "))
# S = input("eneter a string: ")
# check_palindrome(N, S)




#4
# S = input("enter a string: ")
# C = input("enter a character: ")
# count = 0
# for ch in S:
#     if ch == C:
#         count = count + 1
# print(count)



#5
# S = input("enter a string: ")
# result = ""
# for i in range(len(S) - 1, -1, -1):
#     result = result + S[i]
# print(result)



#6
# S = input("eneter a string: ")
# palindrome = True
# i = 0
# j = len(S) - 1

# while i < j:
#     if S[i] != S[j]:
#         palindrome = False
#         break
#     i = i + 1
#     j = j - 1

# if palindrome:
#     print("yes")
# else:
#     print("no")




#7
# S = input("eneter a string: ")
# count = 0
# for ch in S:
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#         count = count + 1
# print(count)



#8
# S = input("eneter a string: ")
# count = 0
# for ch in S:
#     if ch >= "0" and ch <= "9":
#         count = count + 1
# print(count)


#9
# S = input("enter a string: ")
# C = input("enter a character: ")
# position = -1
# for i in range(len(S)):
#     if S[i] == C:
#         position = i
#         break
# print(position)



#10
# S = input("enter a string: ")
# C = input("enter a character: ")
# result = ""
# for ch in S:
#     if ch != C:
#         result = result + ch
# print(result)