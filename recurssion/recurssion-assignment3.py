
# 1
# def messages(message, n):
#     if n == 0:             
#         return
#     print(message)
#     messages(message, n - 1)
# messages("Hello", 3)


# 2. 
# def even(n, num=2):
#     if num%2==0:
#             print(num, end=" ")
#     if num == n:         
#         return
#     even(n, num+1)
# even(10)
# print()


# # 3. 
# def odd(n):
#     if n < 1:               
#         return 0
#     if n % 2 != 0:
#         return n + odd(n - 1)
#     return odd(n - 1)
# print(odd(7))


# # 4.
# def digit(number, num):
#     if number == 0:         # Base case
#         return 0
#     lastdigit = number % 10
#     if lastdigit == num:
#         return 1 + digit(number // 10, num)
#     return digit(number // 10, num)
# print(digit(52525, 5))


# # 5. 
# def product(number):
#     if number < 10:         
#         return number
#     lastdigit = number % 10
#     return lastdigit * product(number // 10)
# print(product(234))


# # 6. 
# def first(number):
#     if number < 10:        
#         return number
#     return first(number // 10)
# print(first(5837))


# # 7.
# def digit(number, num):
#     if number == 0:         
#         return False
#     if number % 10 == num:
#         return True
#     return digit(number // 10, num)
# print(digit(4826, 8))


# # 8. 
# def length(word):
#     if word == "":          
#         return 0
#     return 1 + length(word[1:])
# print(length("coding"))


# # 9. 
# def vowels(word):
#     if word == "":          
#         return 0
#     if word[0] in "aeiou":
#         return 1 + vowels(word[1:])
#     return vowels(word[1:])
# print(vowels("education"))


# # 10.
# def palendrome(word):
#     def check(left, right):
#         if left >= right:  
#             return True
#         if word[left] != word[right]:
#             return False
#         return check(left + 1, right - 1)
7#     return check(0, len(word) -1)

# print(palendrome("level"))
