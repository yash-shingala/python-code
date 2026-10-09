
# # LEVEL 5 



# # Q41

# text = "  this   is   spaced  "

# words = text.split()
# count = len(words)

# print(count)


# # Q42. 

# text = "banana"

# new_text = text.replace("a", "e")

# print(new_text)


# # Q43. 

# text = "hello"
# ch = "e"

# found = False

# for character in text:
#     if character == ch:
#         found = True

# if found:
#     print(True)
# else:
#     print(False)


# # Q44. 

# text1 = "hello"
# text2 = "hello"

# if text1 == text2:
#     print(True)
# else:
#     print(False)


# # Q45. 

# text = "abc123"
# count = 0

# for character in text:
#     if character >= "0" and character <= "9":
#         count = count + 1

# print(count)


# # Q46. 
# text = "HeLLo"
# count = 0

# for character in text:
#     if character >= "A" and character <= "Z":
#         count = count + 1

# print(count)


# # Q47. 

# text = "HeLLo"
# count = 0

# for character in text:
#     if character >= "a" and character <= "z":
#         count = count + 1

# print(count)


# # Q48

# text = "JavaScript"
# new_text = ""

# for character in text:
#     if character != "a" and character != "e" and character != "i" and character != "o" and character != "u" and character != "A" and character != "E" and character != "I" and character != "O" and character != "U":
#         new_text = new_text + character

# print(new_text)


# # Q49. 

# text = "abc123"
# new_text = ""

# for character in text:
#     if character < "0" or character > "9":
#         new_text = new_text + character

# print(new_text)


# # Q50. 

# text = "HeLLo"
# new_text = ""

# for character in text:
#     if character >= "a" and character <= "z":
#         new_text = new_text + character.upper()
#     elif character >= "A" and character <= "Z":
#         new_text = new_text + character.lower()
#     else:
#         new_text = new_text + character

# print(new_text)