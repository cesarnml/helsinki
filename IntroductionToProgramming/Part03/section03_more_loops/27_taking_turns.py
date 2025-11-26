# Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

# Sample output
# Please type in a number: 5
# 1
# 5
# 2
# 4
# 3

# Sample output
# Please type in a number: 6
# 1
# 6
# 2
# 5
# 3
# 4

number = int(input("Please type in a number: "))

left = 1
right = number

while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1

if left == right:
    print(left)
