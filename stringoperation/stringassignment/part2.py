text = "Python"

print(text[0])
print(text[3])
print(text[-1])
print(text[-2])
P
h
n
o



text = "Programming"

print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])
Prog
gramm
Progr
amming




text = "Python"

print(text[::2])
print(text[1::2])
print(text[::-1])
Pto
yhn
nohtyP



text = "Hello World"

print(len(text))
print(text[5])
print(text[-1])
11
 
d




text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)
True
False
True



text = "banana"

print(text.find("a"))
print(text.find("z"))
print(text.count("a"))
1
-1
3



text = "Python"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())
PYTHON
python
Python
Python
pYTHON




text = "I like Java"

print(text.replace("Java", "Python"))
I like Python # type: ignore





text = "Hello"

print(text + " World")
print(text * 3)
HelloWorld # type: ignore
HelloHelloHello








