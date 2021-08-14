# The program below prints only the positive numbers in a list.

numbers = [1, 4, -100, 5, -9]

for val in numbers:
    if val <= 0:         # condition for negative number
        continue
    print(val)

print('This is outside the loop.')