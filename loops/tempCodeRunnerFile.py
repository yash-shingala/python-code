number=int(input("enter a number:"))

while number>0:
    digit=number%10
    print(digit,end="")
    number=number//10