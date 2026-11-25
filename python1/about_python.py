
# word = input("Enter a word: ")
# for i in range(len(word)):
#     already_seen = False
#     for k in range(i):
#         if word[k] == word[i]:
#             already_seen = True
#     if not already_seen:
#         count = 0
#         for ch in word:
#             if ch == word[i]:
#                 count += 1
#         print(word[i], "=", count)



# str = "a1b3c2"
# str2 = ""

# for i in range(0, len(str), 2):
#     letter = str[i]
#     num = int(str[i + 1])

#     for j in range(num):
#         str2 += letter

# print(str2)



sentence = input("Enter a string: ")
word = input("Enter a word to search: ")
found = False
for i in range(len(sentence)):
    count = 0
    for j in range(len(word)):
        if i + j < len(sentence) and sentence[i + j] == word[j]:
            count = count + 1
        else:
            break

    if count == len(word):
        found = True
        break

if found == True:
    print("Word found in the string")
else:
    print("Word not found in the string")
