# Section:A
#1.
# 2
# 1
# Stop
# 1
# 2


# 2.
# if n == 0:
#     return 0



# 3.
# incorrect: count(n + 1)
# correct: count(n - 1)


# 4.
# o.p:- None
# Reason: The recursive calculation is performed but never returned. Python automatically returns None when a function has no return statement.



# Section:B

#5.
# def countdown(n):
#     if n == 0:
#         print("Done!")
#         return
#     print(n)
#     countdown(n - 1)
# countdown(3)
# countdown(0)




#6.
# def count_up(n):
#     if n == 0:
#         return
#     count_up(n - 1)
#     print(n)
# count_up(4)
# count_up(0)



#7.
# def sum_to(n):
#     if n == 0:
#         return 0
#     return n + sum_to(n - 1)

# print(sum_to(5)) 
# print(sum_to(0)) 





#8
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(4))  
# print(factorial(0))  




#9
# def digit_sum(n):
#     if n == 0:
#         return 0
#     return (n % 10) + digit_sum(n // 10)

# print(digit_sum(583))  
# print(digit_sum(7))   
# print(digit_sum(0))   




#10
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)

# print(power(2, 5))  
# print(power(9, 0))  
# print(power(3, 1)) 




#11
# def count_digits(n):
#     if n < 10:
#         return 1
#     return 1 + count_digits(n // 10)

# print(count_digits(5382)) 
# print(count_digits(6))     
# print(count_digits(0))     




#12
# def reverse_text(text):
#     if text == "":
#         return ""
#     return reverse_text(text[1:]) + text[0]

# print(reverse_text("cat"))  
# print(reverse_text("a"))    
# print(reverse_text(""))     





#13
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0))  
# print(fibonacci(1))  
# print(fibonacci(6))  




#14
# def max_digit(n):
#     if n < 10:
#         return n
#     last = n % 10
#     remaining = max_digit(n // 10)
#     if last > remaining:
#         return last
#     else:
#         return remaining

# print(max_digit(4729)) 
# print(max_digit(555))   
# print(max_digit(0))     





#15
# mystery(0) = 0
# mystery(1) = 1

# mystery(2) = mystery(1) + mystery(0)
#            = 1 + 0
#            = 1

# mystery(3) = mystery(2) + mystery(1)
#            = 1 + 1
#            = 2

# mystery(4) = mystery(3) + mystery(2)
#            = 2 + 1
#            = 3



# Section:D

#16
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(0))  
# print(factorial(4))  




#17
# def stop_at_zero(n):
#     if n == 0:
#         return
#     print(n)
#     stop_at_zero(n - 1)

# stop_at_zero(5)