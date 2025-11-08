# Please write a program which asks the user for a year, and prints out the next leap year.

# Sample output
# Year: 2023
# The next leap year after 2023 is 2024

# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

# Sample output
# Year: 2024
# The next leap year after 2024 is 2028

year = int(input("Year: "))
leap = year
while True:
    leap += 1
    if (leap % 4 == 0 and leap % 100 != 0) or (leap % 400 == 0):
        break
print(f"The next leap year after {year} is {leap}")
