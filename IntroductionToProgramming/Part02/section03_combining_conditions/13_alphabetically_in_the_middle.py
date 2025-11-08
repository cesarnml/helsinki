# Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all lowercase.

# Some examples of expected behaviour:

# Sample output
# 1st letter: x
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is p

# Sample output
# 1st letter: C
# 2nd letter: B
# 3rd letter: A
# The letter in the middle is B

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter1 < letter2 < letter3 or letter3 < letter2 < letter1:
    print(f"The letter in the middle is {letter2}")
if letter2 < letter3 < letter1 or letter1 < letter3 < letter2:
    print(f"The letter in the middle is {letter3}")
if letter3 < letter1 < letter2 or letter2 < letter1 < letter3:
    print(f"The letter in the middle is {letter1}")
