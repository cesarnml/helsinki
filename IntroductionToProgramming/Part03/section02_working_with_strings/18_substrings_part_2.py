# Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

# Sample output
# Please type in a string: test
# t
# st
# est
# test

string = input("Please type in a string: ")
start_index = len(string) - 1

while start_index >= 0:
    print(string[start_index:])
    start_index -= 1
