# Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# a
# y
# i
# h

string = input("Please type in a string: ")
length = len(string)

while length > 0:
    print(string[length - 1])
    length -= 1
