# # 1.
# def even(n, position=1):
#     if n == 0:
#         return 0
#     digit = n % 10
#     if position % 2 == 0:
#         return digit + even(n // 10, position + 1)
#     return even(n // 10, position + 1)
# print(even(583246))  



# # 2. 
# def reverse(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse(n // 10, rev * 10 + n % 10)
# print(reverse(4827))   


# # 3.
# def palindrome(s, start, end):
#     if start >= end:
#         return True
#     if s[start] != s[end]:
#         return False
#     return palindrome(s, start + 1, end - 1)

# s = "level"
# print(palindrome(s, 0, len(s) - 1))  # True




# # 4. 
# def count_char(s, ch):
#     if s == "":
#         return 0
#     if s[0] == ch:
#         return 1 + count_char(s[1:], ch)
#     return count_char(s[1:], ch)

# print(count_char("programming", "m"))  # 2




# # 5.
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# print(gcd(48, 18))  # 6


# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# def gcd(c, d,num):
#     if c%num==0 and d%num==0:
#         return num
#     return gcd(c,d,num-1)
# num=min(a,b)
# print(gcd(a, b,num)) 




# # 6. 
# def is_prime(n, divisor=2):
#     if n == divisor:
#         return True
#     if n % divisor == 0:
#         return False
#     return is_prime(n, divisor + 1)
# print(is_prime(29))  



# # 7.
# def remove(s, ch):
#     if s == "":
#         return ""
#     if s[0] == ch:
#         return remove(s[1:], ch)
#     return s[0] + remove(s[1:], ch)
# print(remove_char("mississippi", "s")) 



# # 8. 
# def binary(n):
#     if n < 2:
#         return str(n)
#     return binary(n // 2) + str(n % 2)
# printbinary(13))  



# # 9. 
# def digit(s):
#     if s == "":
#         return True
#     if s[0] < '0' or s[0] > '9':
#         return False
#     return digit(s[1:])
# print(digit("5029e1"))  




# # 10. 
# def main(n):
#     if n<10:
#         return n
#     def sum(n):
#         if n == 0:
#             return 0
#         return n % 10 + sum(n // 10)
#     a=sum(n)
#     if a>10:
#         b=main(a)
#     else:
#         return a
#     return b
# print(main(9875))

