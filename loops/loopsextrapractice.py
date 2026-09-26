# for i in range(4):
#     for loop in range(1,6):
#         print("*",end=" ")
#     print()
##or
# for i in range(4):
#     for loop in range(1,6):
#         print("*",end=" ")
#     print("")




# for row in range(0,4):
#     for column in range(0,row+1):
#         print("*", end=" ")
#     print()
##or
# for i in range(0,4):
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()
##or
# for i in range(0,4):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# for i in range(4,0,-1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()
#or
# for i in range(3,0,-1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
          
# for i in range(1,6):
#     for j in range(0,5-i):
#         print(" ",end="")

#     for k in range(1,i+1):
#         print("*",end="")
#     print()
#     *
#    **
#   ***
#  ****
# *****



# num=int(input("enter a number:"))
# for i in range(1,num):
#     for j in range(0,num-i):
#         print(" ",end="")

#     for k in range(1,i+1):
#         print("*",end="")
#     print()





# for i in range(1,5):
#     for j in range(0,i-1):
#         print(" ",end="")

#     for k in range(0,5-i):
#         print("*",end="")
#     print()
# ****
#  ***
#   **
#    *





#pyramid.py
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()
#     *
#    ***
#   *****
#  *******
# *********