#task37
#A
text = "Python"
print(text[20])


text = "Python"
print(text[0])


#B
text = "Python"
text[0] = "J"


text = "Python"
text = "J" + text[1:]

print(text)


#C
age = 20
print("Age: " + age)


age = 20
print("Age: " + str(age))



#D
text = "Python"
print(text.index("Java"))

text = "Python"

if "Java" in text:
    print(text.index("Java"))
else:
    print("Java was not found")