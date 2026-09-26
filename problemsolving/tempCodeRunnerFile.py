matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

main_sum = 0
secondary_sum = 0
even_main = 0
odd_secondary = 0

for i in range(4):
    for j in range(4):

        # Main diagonal
        if i == j:
            main_sum += matrix[i][j]

            if matrix[i][j] % 2 == 0:
                even_main += 1

        # Secondary diagonal
        if i + j == 5:
            secondary_sum += matrix[i][j]

            if matrix[i][j] % 2 != 0:
                odd_secondary += 1

print("Main diagonal sum:", main_sum)
print("Secondary diagonal sum:", secondary_sum)
print("Even values on main diagonal:", even_main)
print("Odd values on secondary diagonal:", odd_secondary)

# Compare diagonal sums
if main_sum > secondary_sum:
    print("Main diagonal sum is greater.")
elif main_sum < secondary_sum:
    print("Secondary diagonal sum is greater.")
else:
    print("Both diagonal sums are equal.")