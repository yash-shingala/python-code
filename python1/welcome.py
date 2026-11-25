
# Q1. Count overlapping occurrences of a substring

S = input()
P = input()

count = 0

for i in range(len(S) - len(P) + 1):
    match = True

    for j in range(len(P)):
        if S[i + j] != P[j]:
            match = False
            break

    if match:
        count += 1

print(count)


# Q2. Compress consecutive characters

S = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        count += 1
    else:
        result += S[i - 1] + str(count)
        count = 1

result += S[-1] + str(count)
print(result)


# Q3. Find the first non-repeating character

S = input()
answer = "-1"

for i in range(len(S)):
    count = 0

    for j in range(len(S)):
        if S[i] == S[j]:
            count += 1

    if count == 1:
        answer = S[i]
        break

print(answer)


# Q4. Check whether two strings are anagrams

S1 = input()
S2 = input()

if len(S1) != len(S2):
    print("no")
else:
    is_anagram = True

    for i in range(len(S1)):
        count1 = 0
        count2 = 0

        for j in range(len(S1)):
            if S1[i] == S1[j]:
                count1 += 1

            if S1[i] == S2[j]:
                count2 += 1

        if count1 != count2:
            is_anagram = False
            break

    if is_anagram:
        print("yes")
    else:
        print("no")


# Q5. Reverse every word in a sentence

S = input()
word = ""
result = ""

for i in range(len(S)):
    if S[i] != " ":
        word = S[i] + word
    else:
        result += word + " "
        word = ""

result += word
print(result)


# Q6. Find the longest word in a sentence

S = input()

longest = ""
word = ""

for i in range(len(S)):
    if S[i] != " ":
        word += S[i]
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

if len(word) > len(longest):
    longest = word

print(longest)


# Q7. Check whether two strings are rotations

S1 = input()
S2 = input()

if len(S1) != len(S2):
    print("no")
else:
    combined = S1 + S1
    found = False

    for i in range(len(S1)):
        if combined[i:i + len(S1)] == S2:
            found = True
            break

    if found:
        print("yes")
    else:
        print("no")


# Q8. Remove consecutive duplicate characters

S = input()
result = S[0]

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        result += S[i]

print(result)


# Q9. Check whether one string is a subsequence

S = input()
P = input()

i = 0
j = 0

while i < len(S) and j < len(P):
    if S[i] == P[j]:
        j += 1

    i += 1

if j == len(P):
    print("yes")
else:
    print("no")


# Q10. Find the longest palindromic substring

S = input()
longest = 1

for i in range(len(S)):
    for j in range(i, len(S)):
        left = i
        right = j
        palindrome = True

        while left < right:
            if S[left] != S[right]:
                palindrome = False
                break

            left += 1
            right -= 1

        if palindrome:
            length = j - i + 1

            if length > longest:
                longest = length

print(longest)






