# The program below takes inputs from the user and calculates the sum until the user enters a negative number.
# When the user enters negative a number, the break statement is executed which terminates the loop.

sum = 0

# boolean expression is True
while True:
    n = input("Enter a number: ")
    n = float(n)  # Converting to float

    if n < 0:   # check if number is negative 
        break 
    sum += n 

print("sum =", sum)

