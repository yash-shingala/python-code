# Task 39 - Sentence Analyzer

sentence = input("Enter a sentence: ")

print("\nOriginal sentence:", sentence)
print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))

if sentence:
    print("First character:", sentence[0])
    print("Last character:", sentence[-1])
else:
    print("The sentence is empty.")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Contains 'Python':", "Python" in sentence)

character = input("Enter a character to count: ")

print(
    "Number of times the character occurs:",
    sentence.count(character)
)