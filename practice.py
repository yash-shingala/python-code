# num=int(input("enter a number:"))

# for i in range(num):
#     for j in range(num):
#         if j%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#     print()




# def make_counter():
#     count=0
#     def increment():
#         nonlocal count
#         count+=1
#         return count
#     return increment
# counter=make_counter()
# # print(make_counter()())
# # print(make_counter()())
# # print(make_counter()())
# print(counter())
# print(counter())
# print(counter())

# def show(n):
#     if n==0:
#         print("end")
#         return
#     print("start",n)
#     print(show(n-1))
#     print("back",n)
# print(show(2))




# def digit_sum(n):
#     if n < 10:
#         return n
#     return n % 10 + digit_sum(n // 10)
# print(digit_sum(472))