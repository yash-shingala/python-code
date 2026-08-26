# Task 25 - Replace a Word

text = "I am learning Java"

new_text = text.replace("Java", "Python")

print(new_text)




# Task 26 - Multiple Replacements

text = "apple apple apple"

new_text = text.replace("apple", "mango")

print(new_text)




# Task 27 - Limited Replacement

text = "apple apple apple"

new_text = text.replace("apple", "mango", 1)

print(new_text)




# Task 28 - Check Immutability

text = "Python"

text.upper()

print("Original:", text)

text = text.upper()

print("After storing result:", text)