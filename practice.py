num=int(input("enter a number:"))

for i in range(num):
    for j in range(num):
        if j%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()
