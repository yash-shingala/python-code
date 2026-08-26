# Task 20 - Membership

text = "Python is a programming language"

print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)



# Task 21 - find()

text = "Python is a programming language"

print("Python:", text.find("Python"))
print("programming:", text.find("programming"))
print("language:", text.find("language"))
print("Java:", text.find("Java"))




# Task 22 - index()

text = "Python is a programming language"

print("Python:", text.index("Python"))
print("programming:", text.index("programming"))
print("language:", text.index("language"))

try:
    print("Java:", text.index("Java"))
except ValueError:
    print("Java: ValueError - substring not found")






# Task 23 - Count Characters

text = "banana"

print("a:", text.count("a"))
print("n:", text.count("n"))
print("b:", text.count("b"))






# Task 24 - Starts and Ends

filename = "student_notes.pdf"

print("Starts with student:", filename.startswith("student"))
print("Ends with .pdf:", filename.endswith(".pdf"))
print("Ends with .txt:", filename.endswith(".txt"))


