# # Q21. 

# n = int(input("Enter number: "))

# if n == 0:
#     count = 1
# else:
#     n = abs(n)
#     count = 0

#     while n > 0:
#         count = count + 1
#         n = n // 10

# print("Number of digits:", count)


# # Q22. 

# n = int(input("Enter number: "))
# n = abs(n)
# sum_digits = 0

# while n > 0:
#     digit = n % 10
#     sum_digits = sum_digits + digit
#     n = n // 10

# print("Sum of digits:", sum_digits)


# # Q23

# n = int(input("Enter number: "))
# n = abs(n)

# if n == 0:
#     product = 0
# else:
#     product = 1

#     while n > 0:
#         digit = n % 10
#         product = product * digit
#         n = n // 10

# print("Product of digits:", product)


# # Q24

# n = int(input("Enter number: "))
# original = n
# sign = 1

# if n < 0:
#     sign = -1
#     n = -n

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# reverse = reverse * sign
# print("Reverse:", reverse)


# # Q25

# n = int(input("Enter number: "))
# original = n

# if n < 0:
#     n = -n
#     original = -original

# reverse = 0
# temp = n

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp = temp // 10

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Q26. 

# n = int(input("Enter number: "))
# i = 2
# is_prime = True

# if n < 2:
#     is_prime = False
# else:
#     while i < n:
#         if n % i == 0:
#             is_prime = False
#             break
#         i = i + 1

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")


# Q27. 

# N = int(input("Enter N: "))
# num = 2

# while num <= N:
#     i = 2
#     is_prime = True

#     while i < num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i = i + 1

#     if is_prime:
#         print(num, end=" ")

#     num = num + 1


# # Q28. 

# N = int(input("\nEnter N: "))

# a = 0
# b = 1
# count = 0

# while count < N:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     count = count + 1


# # Q29. 

# a = int(input("\nEnter a: "))
# b = int(input("Enter b: "))

# a = abs(a)
# b = abs(b)

# gcd = 1
# i = 1

# while i <= a and i <= b:
#     if a % i == 0 and b % i == 0:
#         gcd = i
#     i = i + 1

# print("GCD:", gcd)


# # Q30. 

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))



# if a == 0 or b == 0:
#     lcm = 0
# else:
#     if a > b:
#         lcm = a
#     else:
#         lcm = b

#     while lcm % a != 0 or lcm % b != 0:
#         lcm = lcm + 1

# print("LCM:", lcm)