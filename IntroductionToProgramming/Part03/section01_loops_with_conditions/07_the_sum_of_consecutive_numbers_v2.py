# Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3

# Sample output
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10

# Sample output
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

# You may assume the number typed in by the user is always equal to 2 or higher.

sum = 0
num = 1
calculation = "The consecutive sum: "
limit = int(input("Limit: "))

while sum < limit:
    sum += num
    calculation += f"{num} "
    num += 1
    if sum < limit:
        calculation += "+ "
print(f"{calculation} = {sum}")


# model solution (the inner if loop is a code-smell in my solution)
# limit = int(input("Limit: "))
# number = 1
# sum = 1
# numbers = "1"
# while sum < limit:
#     number += 1
#     sum += number
#     # note that f-string can also be used like this
#     numbers += f" + {number}"
# print(f"The consecutive sum: {numbers} = {sum}")
