# Task 40 - Student Information

# Taking input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
city = input("Enter your city: ").strip()
course = input("Enter your course: ").strip()
age = int(input("Enter your age: "))

# Create full name
full_name = first_name + " " + last_name

# Display name information
print("\n--- Student Information ---")

print("Full name:", full_name)
print("Title case:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length of full name:", len(full_name))

if full_name:
    print("First character:", full_name[0])
    print("Last character:", full_name[-1])

# Display city and course
print("City:", city)
print("Course:", course)

# Display age using f-string
print(f"Age: {age}")

# Check whether course contains Python
print("Course contains Python:", "Python" in course)

# Replace one word in course name
replacement_word = input("Enter a word to replace in the course: ").strip()
new_word = input("Enter the new word: ").strip()

if replacement_word:
    updated_course = course.replace(replacement_word, new_word)
else:
    updated_course = course

print("Updated course:", updated_course)

# Count words in course
print("Number of words in course:", len(course.split()))