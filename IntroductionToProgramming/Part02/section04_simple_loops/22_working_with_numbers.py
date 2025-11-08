# Pre-task
# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

# Sample output
# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

# Part 1: Count
# After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

# You will need a new variable here to keep track of the numbers typed in.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4

# Part 2: Sum
# The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

# The program should now print out the following:

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34

print("Please type in integer numbers. Type in 0 to finish.")

count = 0
sum = 0
mean = 0
pos_count = 0
neg_count = 0

while True:
    num = int(input("Number: "))
    if num == 0:
        break
    else:
        count += 1
        sum += num
        if num > 0:
            pos_count += 1
        else:
            neg_count += 1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / count}")
print(f"Positive numbers {pos_count}")
print(f"Negative numbers {neg_count}")
