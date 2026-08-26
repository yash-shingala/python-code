# Task 38 - Name Processor

original_name = input("Enter your full name: ")

cleaned_name = original_name.strip()

print("\nOriginal input:", original_name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))

if cleaned_name:
    print("First character:", cleaned_name[0])
    print("Last character:", cleaned_name[-1])

    character = input("Enter a character to search for: ")

    print(
        "Character exists:",
        character in cleaned_name
    )
else:
    print("The name is empty.")





    